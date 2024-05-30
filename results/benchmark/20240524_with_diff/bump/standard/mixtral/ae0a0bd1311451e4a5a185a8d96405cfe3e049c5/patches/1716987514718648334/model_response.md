Here's a suggested patch for the code that should fix the error:

```java
import org.hamcrest.Matchers;
import static org.hamcrest.Matchers.allOf;
import static org.hamcrest.Matchers.instanceOf;
import static org.hamcrest.Matchers.not;
import static org.hamcrest.Matchers.stringContainsInOrder;

@org.junit.jupiter.api.Test
void failsOnDigestMismatch() {
    final com.artipie.asto.memory.InMemoryStorage storage = new com.artipie.asto.memory.InMemoryStorage();
    final com.artipie.docker.asto.AstoBlobs blobs = new com.artipie.docker.asto.AstoBlobs(storage, new com.artipie.docker.asto.DefaultLayout(), new com.artipie.docker.RepoName.Simple("any"));
    final java.lang.String digest = "123";
    blobs.put(new com.artipie.docker.asto.CheckedBlobSource(new com.artipie.asto.Content.From("data".getBytes()), new com.artipie.docker.Digest.Sha256(digest))).toCompletableFuture().handle(( blob, throwable) -> {
        org.junit.jupiter.api.Assertions.assertNotNull(throwable, "Exception thrown");
        org.junit.jupiter.api.Assertions.assertEquals(com.artipie.docker.error.InvalidDigestException.class, throwable.getClass(), "Exception is InvalidDigestException");
        org.junit.jupiter.api.Assertions.assertTrue(throwable.getMessage().contains("3a6eb0790f39ac87c94f3856b2dd2c5d110e6811602261a9a923d3bb23adc8b7"), "Exception message contains calculated digest");
        org.junit.jupiter.api.Assertions.assertTrue(throwable.getMessage().contains(digest), "Exception message contains expected digest");
        return java.util.concurrent.CompletableFuture.allOf();
    }).join();
}
```

In this patch, I've replaced the `MatcherAssert.assertThat` calls with `Assertions.assertEquals`, `Assertions.assertNotNull`, and `Assertions.assertTrue` calls using JUnit 5's Assertions API. I've also replaced the `StringContains` matcher with `contains` method from `Assertions`.

Note that I've imported the `Matchers` class and some static methods from `Matchers` to simplify the code.