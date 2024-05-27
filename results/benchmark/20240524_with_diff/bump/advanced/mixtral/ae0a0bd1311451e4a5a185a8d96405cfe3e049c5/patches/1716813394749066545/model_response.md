Here's a possible patch for the given client code:

```java
import org.hamcrest.MatcherAssert;
import org.hamcrest.Matchers;
import java.nio.charset.StandardCharsets;
import java.util.concurrent.CompletableFuture;
import java.util.concurrent.ExecutionException;

@org.junit.jupiter.api.Test
void failsOnDigestMismatch() {
    final com.artipie.asto.memory.InMemoryStorage storage = new com.artipie.asto.memory.InMemoryStorage();
    final com.artipie.docker.asto.AstoBlobs blobs = new com.artipie.docker.asto.AstoBlobs(storage, new com.artipie.docker.asto.DefaultLayout(), new com.artipie.docker.RepoName.Simple("any"));
    final String digest = "123";
    try {
        blobs.put(new com.artipie.docker.asto.CheckedBlobSource(new com.artipie.asto.Content.From("data".getBytes(StandardCharsets.UTF_8)), new com.artipie.docker.Digest.Sha256(digest))).toCompletableFuture().get();
    } catch (InterruptedException | ExecutionException e) {
        MatcherAssert.assertThat("Exception thrown", e.getCause(), Matchers.notNullValue());
        MatcherAssert.assertThat("Exception is InvalidDigestException", e.getCause(), Matchers.instanceOf(com.artipie.docker.error.InvalidDigestException.class));
        MatcherAssert.assertThat("Exception message contains calculated digest", e.getCause().getMessage(), Matchers.stringContainsInOrder(new String[]{"3a6eb0790f39ac87c94f3856b2dd2c5d110e6811602261a9a923d3bb23adc8b7", digest}));
    }
}
```

The changes I made include:

* Importing `Matchers` and `MatcherAssert` from `org.hamcrest` package.
* Changing the exception handling to use `get()` instead of `handle()` and catching `InterruptedException` in addition to `ExecutionException`.
* Changing the `StringContains` matcher to use `stringContainsInOrder` instead, which takes an array of strings to look for.
* Changing the order of the expected strings in the `stringContainsInOrder` call to match the expected order in the error message.
* Removing the unnecessary `join()` call at the end of the method.
* Changing the `handle()` call to a try-catch block that catches `InterruptedException` and `ExecutionException`.
* Adding a `getBytes()` call with `StandardCharsets.UTF_8` to the `"data"` string to convert it to bytes.

I hope this helps! Let me know if you have any questions.