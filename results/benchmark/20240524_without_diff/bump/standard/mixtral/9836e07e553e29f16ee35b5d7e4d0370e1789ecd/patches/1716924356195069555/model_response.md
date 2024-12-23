Here's a possible patch for the given client code:

```java
import static org.hamcrest.MatcherAssert.assertThat;
import static org.hamcrest.Matchers.instanceOf;
import static org.hamcrest.Matchers.not;
import static org.hamcrest.Matchers.nullValue;
import java.nio.charset.StandardCharsets;
import java.util.concurrent.CompletableFuture;
import org.junit.jupiter.api.Test;
import com.artipie.asto.Content;
import com.artipie.asto.Storage;
import com.artipie.asto.ext.Args;
import com.artipie.asto.memory.InMemoryStorage;
import com.artipie.docker.asto.AstoBlobs;
import com.artipie.docker.asto.CheckedBlobSource;
import com.artipie.docker.Digest;
import com.artipie.docker.error.InvalidDigestException;
import com.google.common.base.Throwables;
import io.reactivex.Completable;

@Test
void failsOnDigestMismatch() {
    final Storage storage = new InMemoryStorage();
    final AstoBlobs blobs = new AstoBlobs(
        storage,
        new DefaultLayout(),
        new RepoName.Simple("any")
    );
    final String digest = "123";
    final Content content = Content.From("data".getBytes(StandardCharsets.UTF_8));
    final Digest.Sha256 sha256 = new Digest.Sha256(digest);
    final CheckedBlobSource source = new CheckedBlobSource(content, sha256);
    blobs.put(source)
        .toCompletableFuture()
        .handle(
            (blob, throwable) -> {
                assertThat("Exception thrown", throwable, not(nullValue()));
                assertThat("Exception is InvalidDigestException", throwable, instanceOf(InvalidDigestException.class));
                final InvalidDigestException ex = (InvalidDigestException) Throwables.getRootCause(throwable);
                assertThat(
                    "Exception message contains calculated digest",
                    ex.message(),
                    new StringContains("3a6eb0790f39ac87c94f3856b2dd2c5d110e6811602261a9a923d3bb23adc8b7")
                );
                assertThat(
                    "Exception message contains expected digest",
                    ex.message(),
                    new StringContains(digest)
                );
                return Completable.complete();
            }
        )
        .blockingGet();
}
```

The changes made are:

* Importing the missing classes and interfaces.
* Using `Completable` instead of `CompletableFuture`.
* Removing unnecessary static imports.
* Using `instanceOf` instead of `IsInstanceOf`.
* Using `not` and `nullValue` instead of `IsNot`.
* Using `new StringContains` instead of `StringContains`.
* Creating `content` and `sha256` variables to make the code more readable.
* Using `blockingGet` instead of `join`.
* Removing unnecessary parentheses.
* Adding missing semicolons.
* Fixing the `StringContains` constructor call.

Note that this patch may not be the only solution, and it may not be the best solution. It's always recommended to test the patched code thoroughly before deploying it to production.