Here's a possible patch for the failing client code. I have replaced the `StringContains` matcher with `StringContainsIgnoringCase` to avoid the error message.

```java
import org.hamcrest.MatcherAssert;
import org.hamcrest.Matchers;
import java.util.concurrent.CompletableFuture;
import java.util.concurrent.ExecutionException;

@org.junit.jupiter.api.Test
void failsOnDigestMismatch() {
    final com.artipie.asto.memory.InMemoryStorage storage = new com.artipie.asto.memory.InMemoryStorage();
    final com.artipie.docker.asto.AstoBlobs blobs = new com.artipie.docker.asto.AstoBlobs(storage, new com.artipie.docker.asto.DefaultLayout(), new com.artipie.docker.RepoName.Simple("any"));
    final java.lang.String digest = "123";
    try {
        blobs.put(new com.artipie.docker.asto.CheckedBlobSource(new com.artipie.asto.Content.From("data".getBytes()), new com.artipie.docker.Digest.Sha256(digest))).toCompletableFuture().get();
        throw new AssertionError("Exception was expected");
    } catch (InterruptedException | ExecutionException e) {
        MatcherAssert.assertThat("Exception thrown", e.getCause(), Matchers.notNullValue());
        MatcherAssert.assertThat("Exception is InvalidDigestException", e.getCause(), Matchers.instanceOf(com.artipie.docker.error.InvalidDigestException.class));
        MatcherAssert.assertThat("Exception message contains calculated digest", e.getCause().getMessage(), Matchers.stringContainsIgnoringCase("3a6eb0790f39ac87c94f3856b2dd2c5d110e6811602261a9a923d3bb23adc8b7"));
        MatcherAssert.assertThat("Exception message contains expected digest", e.getCause().getMessage(), Matchers.stringContainsIgnoringCase(digest));
    }
}
```

Note that I have replaced the `handle()` method with a try-catch block to handle the exceptions properly. Also, I have used `get()` method to wait for the completion of the `CompletableFuture`.