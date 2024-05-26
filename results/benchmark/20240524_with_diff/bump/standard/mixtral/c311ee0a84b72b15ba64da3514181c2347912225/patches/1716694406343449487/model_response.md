Here's a possible patch for the code you provided. The issue seems to be with the `StringContains` constructor used in the `hamcrest` library. I have updated the constructor calls to match the new library version.

```java
import java.util.concurrent.CompletableFuture;
import org.hamcrest.MatcherAssert;
import org.hamcrest.Matchers;
import com.artipie.asto.Content;
import com.artipie.asto.CheckedBlobSource;
import com.artipie.asto.memory.InMemoryStorage;
import com.artipie.docker.asto.AstoBlobs;
import com.artipie.docker.asto.DefaultLayout;
import com.artipie.docker.Digest;
import com.artipie.docker.RepoName;
import com.artipie.docker.CheckedBlobSource.From;
import com.artipie.docker.asto.IsNot;
import com.artipie.docker.asto.IsNull;
import com.artipie.docker.error.InvalidDigestException;
import com.google.common.base.Throwables;

@org.junit.jupiter.api.Test
void failsOnDigestMismatch() {
    final InMemoryStorage storage = new InMemoryStorage();
    final AstoBlobs blobs = new AstoBlobs(storage, new DefaultLayout(), new RepoName.Simple("any"));
    final String digest = "123";
    blobs.put(new CheckedBlobSource(new From("data".getBytes()), new Digest.Sha256(digest))).toCompletableFuture().handle(( blob, throwable) -> {
        MatcherAssert.assertThat("Exception thrown", throwable, new IsNot<>(new IsNull<>()));
        MatcherAssert.assertThat("Exception is InvalidDigestException", Throwables.getRootCause(throwable), Matchers.instanceOf(InvalidDigestException.class));
        MatcherAssert.assertThat("Exception message contains calculated digest", Throwables.getRootCause(throwable).getMessage(), Matchers.containsString("3a6eb0790f39ac87c94f3856b2dd2c5d110e6811602261a9a923d3bb23adc8b7"));
        MatcherAssert.assertThat("Exception message contains expected digest", Throwables.getRootCause(throwable).getMessage(), Matchers.containsString(digest));
        return CompletableFuture.allOf();
    }).join();
}
```

This patch should fix the compilation error you were facing due to the changes in the `hamcrest` library.