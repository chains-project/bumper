Here's the fixed failsOnDigestMismatch method using the StringContains constructor that takes a single String argument:

```java
import org.hamcrest.MatcherAssert;
import org.hamcrest.core.IsInstanceOf;
import org.hamcrest.core.IsNot;
import org.hamcrest.core.StringContains;
import org.junit.jupiter.api.Test;
import com.artipie.asto.Content;
import com.artipie.asto.CheckedBlobSource;
import com.artipie.asto.memory.InMemoryStorage;
import com.artipie.docker.asto.AstoBlobs;
import com.artipie.docker.asto.DefaultLayout;
import com.artipie.docker.Digest;
import com.artipie.docker.RepoName;
import com.artipie.docker.error.InvalidDigestException;
import java.util.concurrent.CompletableFuture;
import java.util.concurrent.ExecutionException;

@Test
void failsOnDigestMismatch() throws ExecutionException, InterruptedException {
    final InMemoryStorage storage = new InMemoryStorage();
    final AstoBlobs blobs = new AstoBlobs(storage, new DefaultLayout(), new RepoName.Simple("any"));
    final String digest = "123";
    blobs.put(new CheckedBlobSource(Content.From("data".getBytes()), new Digest.Sha256(digest)))
         .toCompletableFuture()
         .handle(( blob, throwable) -> {
             MatcherAssert.assertThat("Exception thrown", throwable, new IsNot<>(new IsNull<>()));
             MatcherAssert.assertThat("Exception is InvalidDigestException", throwable.getCause(), new IsInstanceOf(InvalidDigestException.class));
             MatcherAssert.assertThat("Exception message contains calculated digest", throwable.getCause().getMessage(), new StringContains("3a6eb0790f39ac87c94f3856b2dd2c5d110e6811602261a9a923d3bb23adc8b7"));
             MatcherAssert.assertThat("Exception message contains expected digest", throwable.getCause().getMessage(), new StringContains(digest));
             return CompletableFuture.allOf();
         })
         .join();
}
```

This version of the method uses the one-argument StringContains constructor to avoid the compile error.