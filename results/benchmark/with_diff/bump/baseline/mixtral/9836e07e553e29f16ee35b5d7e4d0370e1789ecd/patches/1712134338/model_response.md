Here is a fixed version of the `failsOnDigestMismatch()` method that should resolve the error:
```java
@Test
void failsOnDigestMismatch() {
    final InMemoryStorage storage = new InMemoryStorage();
    final AstoBlobs blobs = new AstoBlobs(
        storage, new DefaultLayout(), new RepoName.Simple("any")
    );
    final String digest = "123";
    blobs.put(
        new CheckedBlobSource(new Content.From("data".getBytes()), new Digest.Sha256(digest))
    ).toCompletableFuture().handle(
        (blob, throwable) -> {
            MatcherAssert.assertThat(
                "Exception thrown",
                throwable,
                new IsNot<>(new IsNull<>())
            );
            MatcherAssert.assertThat(
                "Exception is InvalidDigestException",
                Throwables.getRootCause(throwable),
                new IsInstanceOf(InvalidDigestException.class)
            );
            MatcherAssert.assertThat(
                "Exception message contains calculated digest",
                Throwables.getRootCause(throwable).getMessage(),
                new StringContains(
                    new StringValue(
                        "3a6eb0790f39ac87c94f3856b2dd2c5d110e6811602261a9a923d3bb23adc8b7"
                    )
                )
            );
            MatcherAssert.assertThat(
                "Exception message contains expected digest",
                Throwables.getRootCause(throwable).getMessage(),
                new StringContains(
                    new StringValue(digest)
                )
            );
            return CompletableFuture.allOf();
        }
    ).join();
}
```
The error was caused by the `StringContains` matcher receiving two arguments instead of one. To fix this, I have wrapped the expected strings in a `StringValue` object.

Additionally, I have imported the following classes at the beginning of the file:
```java
import static org.hamcrest.MatcherAssert.assertThat;
import static org.hamcrest.Matchers.instanceOf;
import static org.mockito.Mockito.times;
import static org.mockito.Mockito.verify;
import static org.mockito.Mockito.when;

import java.nio.charset.StandardCharsets;
import org.hamcrest.Matcher;
import org.hamcrest.core.IsInstanceOf;
import org.hamcrest.core.IsNot;
import org.hamcrest.core.StringContains;
import org.hamcrest.core.StringValue;
import org.mockito.ArgumentMatchers;
import org.mockito.Mockito;
import org.testng.annotations.Test;
import io.reactivex.CompletableFuture;
import io.reactivex.Single;
import com.artipie.asto.CheckedBlobSource;
import com.artipie.asto.Content;
import com.artipie.asto.Key;
import com.artipie.asto.Storage;
import com.artipie.asto.ext.InMemoryStorage;
import com.artipie.asto.memory.MemoryPath;
import com.artipie.asto.test.TestResource;
import com.artipie.docker.asto.AstoBlobs;
import com.artipie.docker.digest.Blobs;
import com.artipie.docker.digest.Digest.Sha256;
import com.artipie.docker.digest.Layout;
import com.artipie.docker.digest.Manifest;
import com.artipie.docker.digest.Manifest.V22;
import com.artipie.docker.digest.Repositories;
import com.artipie.docker.digest.Repositories.Simple;
import com.artipie.docker.http.SliceKey;
import com.artipie.http.Slice;
import com.artipie.http.auth.Auth;
import com.artipie.http.auth.Roles;
import com.artipie.http.slice.SliceSingle;
import com.artipie.http.ssl.Ssl;
```
These imports might already be present in your code, but I have included them here for completeness.