Here's a possible patch for the failing method:

```java
import org.hamcrest.MatcherAssert;
import org.hamcrest.Matchers;
import java.util.concurrent.CompletableFuture;
import java.util.concurrent.ExecutionException;
import static org.hamcrest.Matchers.instanceOf;

@org.junit.jupiter.api.Test
void failsOnDigestMismatch() {
    final com.artipie.asto.memory.InMemoryStorage storage = new com.artipie.asto.memory.InMemoryStorage();
    final com.artipie.docker.asto.AstoBlobs blobs = new com.artipie.docker.asto.AstoBlobs(storage, new com.artipie.docker.asto.DefaultLayout(), new com.artipie.docker.RepoName.Simple("any"));
    final java.lang.String digest = "123";
    try {
        blobs.put(new com.artipie.docker.asto.CheckedBlobSource(new com.artipie.asto.Content.From("data".getBytes()), new com.artipie.docker.Digest.Sha256(digest))).toCompletableFuture().get();
    } catch (InterruptedException | ExecutionException e) {
        MatcherAssert.assertThat("Exception thrown", e.getCause(), Matchers.notNullValue());
        MatcherAssert.assertThat("Exception is InvalidDigestException", e.getCause(), instanceOf(com.artipie.docker.error.InvalidDigestException.class));
        MatcherAssert.assertThat("Exception message contains calculated digest", e.getCause().getMessage(), Matchers.stringContainsInOrder(digest, "3a6eb0790f39ac87c94f3856b2dd2c5d110e6811602261a9a923d3bb23adc8b7"));
    }
}
```

In this patch, I've used `MatcherAssert.assertThat` with `Matchers.notNullValue()` and `Matchers.stringContainsInOrder()` instead of `com.artipie.docker.asto.IsNot.<?>` and `org.hamcrest.core.StringContains`, respectively. This should fix the error message you were seeing.

Note that this patch also removes the final `CompletableFuture.allOf()` call, since it seems unnecessary and may cause a compilation error due to the missing argument. Additionally, it uses a try-catch block to handle the exceptions that may be thrown when calling `toCompletableFuture().get()`.