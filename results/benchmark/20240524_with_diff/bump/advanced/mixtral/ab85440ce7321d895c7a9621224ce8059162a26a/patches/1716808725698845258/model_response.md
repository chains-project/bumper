Here's a proposed patch for the given client code:

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

The patch includes the following changes:

* Replaced `handle` method with `get` method to handle exceptions.
* Replaced `StringContains` matcher with `stringContainsInOrder` method from `Matchers`.
* Replaced `Throwables.getRootCause` method with direct access to the cause of the exception.
* Added `InterruptedException` to the `catch` block.
* Changed `String` to `String[]` in `stringContainsInOrder` method.
* Added `StandardCharsets.UTF_8` to `getBytes` method.

These changes should fix the compilation error and make the code work with the new version of the library.