Here's a possible patch for the failing client code:

```java
import org.hamcrest.MatcherAssert;
import org.hamcrest.Matchers;
import java.nio.charset.StandardCharsets;
import java.util.concurrent.CompletableFuture;
import java.util.concurrent.ExecutionException;

@org.junit.jupiter.api.Test
void failsOnDigestMismatch() throws ExecutionException, InterruptedException {
    final com.artipie.asto.memory.InMemoryStorage storage = new com.artipie.asto.memory.InMemoryStorage();
    final com.artipie.docker.asto.AstoBlobs blobs = new com.artipie.docker.asto.AstoBlobs(storage, new com.artipie.docker.asto.DefaultLayout(), new com.artipie.docker.RepoName.Simple("any"));
    final String digest = "123";
    CompletableFuture<Void> putFuture = blobs.put(new com.artipie.docker.asto.CheckedBlobSource(new com.artipie.asto.Content.From("data".getBytes(StandardCharsets.UTF_8)), new com.artipie.docker.Digest.Sha256(digest)));
    putFuture.toCompletableFuture().get();
    MatcherAssert.assertThat("Exception thrown", putFuture.isCompletedExceptionally());
    MatcherAssert.assertThat("Exception is InvalidDigestException", putFuture.exceptionally(Throwable::getCause).get(), Matchers.instanceOf(com.artipie.docker.error.InvalidDigestException.class));
    MatcherAssert.assertThat("Exception message contains calculated digest", putFuture.exceptionally(Throwable::getCause).get().getMessage(), Matchers.stringContainsInOrder(digest, "3a6eb0790f39ac87c94f3856b2dd2c5d110e6811602261a9a923d3bb23adc8b7"));
}
```

In this patch, I changed the way the `StringContains` matcher is used, by using `stringContainsInOrder` method instead. I also added some imports and exception handling to make the code more readable and concise.