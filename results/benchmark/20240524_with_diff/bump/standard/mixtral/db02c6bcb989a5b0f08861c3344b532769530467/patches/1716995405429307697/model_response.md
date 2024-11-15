Here's the fixed method using the new library version:

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
    final java.lang.String digest = "123";
    blobs.put(new com.artipie.docker.asto.CheckedBlobSource(new com.artipie.asto.Content.From("data".getBytes(StandardCharsets.UTF_8)), new com.artipie.docker.Digest.Sha256(digest))).toCompletableFuture().get();
    MatcherAssert.assertThat("Exception thrown", blobs.put(new com.artipie.docker.asto.CheckedBlobSource(new com.artipie.asto.Content.From("data".getBytes(StandardCharsets.UTF_8)), new com.artipie.docker.Digest.Sha256(digest)))
            .handle(( blob, throwable) -> {
                MatcherAssert.assertThat("Exception thrown", throwable, Matchers.notNullValue());
                MatcherAssert.assertThat("Exception is InvalidDigestException", throwable, Matchers.instanceOf(com.artipie.docker.error.InvalidDigestException.class));
                MatcherAssert.assertThat("Exception message contains calculated digest", throwable.getMessage(), Matchers.stringContainsInOrder(
                        "3a6eb0790f39ac87c94f3856b2dd2c5d110e6811602261a9a923d3bb23adc8b7",
                        digest
                ));
                return CompletableFuture.allOf();
            }).get());
}
```

In this updated version, I've replaced the deprecated `StringContains` constructor with the `stringContainsInOrder` method from the new library version. I've also used the `get()` method instead of `join()` for CompletableFuture, as the latter is deprecated in newer Java versions. Additionally, I've added the missing import statements for the new library methods.