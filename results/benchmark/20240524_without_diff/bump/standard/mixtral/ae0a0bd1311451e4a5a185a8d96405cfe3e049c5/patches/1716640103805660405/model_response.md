Here's a possible patch for the given client code:

```java
import org.hamcrest.MatcherAssert;
import org.junit.jupiter.api.Test;
import java.nio.charset.StandardCharsets;
import java.util.concurrent.CompletableFuture;
import java.util.concurrent.ExecutionException;

@Test
void failsOnDigestMismatch() throws ExecutionException, InterruptedException {
    final com.artipie.asto.memory.InMemoryStorage storage = new com.artipie.asto.memory.InMemoryStorage();
    final com.artipie.docker.asto.AstoBlobs blobs = new com.artipie.docker.asto.AstoBlobs(storage, new com.artipie.docker.asto.DefaultLayout(), new com.artipie.docker.RepoName.Simple("any"));
    final String digest = "123";
    CompletableFuture<Void> result = blobs.put(new com.artipie.docker.asto.CheckedBlobSource(new com.artipie.asto.Content.From("data".getBytes(StandardCharsets.UTF_8)), new com.artipie.docker.Digest.Sha256(digest)))
        .thenAccept(blob -> {
            MatcherAssert.assertThat("Exception thrown", false);
        })
        .exceptionally(throwable -> {
            MatcherAssert.assertThat("Exception is InvalidDigestException", throwable instanceof com.artipie.docker.error.InvalidDigestException);
            MatcherAssert.assertThat("Exception message contains calculated digest", throwable.getMessage().contains("3a6eb0790f39ac87c94f3856b2dd2c5d110e6811602261a9a923d3bb23adc8b7"));
            MatcherAssert.assertThat("Exception message contains expected digest", throwable.getMessage().contains(digest));
            return null;
        });
    result.join();
}
```

In this patch, I've made the following changes:

1. I've changed the method signature to throw `ExecutionException` and `InterruptedException` to avoid handling `CompletableFuture` exceptions using `handle()` method.
2. I've removed the `IsNot` and `IsNull` matchers, and directly checked if the exception is an instance of `InvalidDigestException`.
3. I've used the `contains()` method of `String` class to check if the exception message contains the calculated and expected digests.
4. I've used `thenAccept()` and `exceptionally()` methods of `CompletableFuture` to handle the result and exceptions, respectively.
5. I've used `getBytes(StandardCharsets.UTF_8)` to get the bytes of the string "data".