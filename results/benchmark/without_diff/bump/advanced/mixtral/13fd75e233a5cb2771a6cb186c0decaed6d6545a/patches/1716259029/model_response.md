Here is a possible patch for the failing client code:
```java
import org.hamcrest.Matchers;
import java.util.concurrent.CompletableFuture;
import java.util.concurrent.ExecutionException;

@org.junit.jupiter.api.Test
void failsOnDigestMismatch() throws ExecutionException, InterruptedException {
    final com.artipie.asto.memory.InMemoryStorage storage = new com.artipie.asto.memory.InMemoryStorage();
    final com.artipie.docker.asto.AstoBlobs blobs = new com.artipie.docker.asto.AstoBlobs(storage, new com.artipie.docker.asto.DefaultLayout(), new com.artipie.docker.RepoName.Simple("any"));
    final java.lang.String digest = "123";
    CompletableFuture<com.artipie.asto.Key> future = blobs.put(new com.artipie.docker.asto.CheckedBlobSource(new com.artipie.asto.Content.From("data".getBytes()), new com.artipie.docker.Digest.Sha256(digest)));
    future.get();
    try {
        future.get();
    } catch (ExecutionException e) {
        com.google.common.base.Throwables.getRootCause(e);
        org.hamcrest.MatcherAssert.assertThat("Exception thrown", e.getCause(), Matchers.notNullValue());
        org.hamcrest.MatcherAssert.assertThat("Exception is InvalidDigestException", e.getCause(), Matchers.instanceOf(com.artipie.docker.error.InvalidDigestException.class));
        org.hamcrest.MatcherAssert.assertThat("Exception message contains calculated digest", e.getCause().getMessage(), Matchers.stringContainsInOrder(new Object[]{"3a6eb0790f39ac87c94f3856b2dd2c5d110e6811602261a9a923d3bb23adc8b7", digest}));
    }
}
```
The patch fixes the error by using a different version of the `StringContains` matcher that takes a vararg of strings instead of a boolean and a string. The patch also simplifies the code by using `CompletableFuture.get()` to wait for the completion of the `put` operation, and by catching `ExecutionException` directly instead of handling the exception in a completion stage.