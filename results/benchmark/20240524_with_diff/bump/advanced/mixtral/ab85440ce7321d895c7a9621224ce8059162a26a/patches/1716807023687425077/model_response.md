Here's a proposed patch for the given client code:

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
    putFuture.exceptionally(throwable -> {
        MatcherAssert.assertThat("Exception thrown", throwable != null);
        MatcherAssert.assertThat("Exception is InvalidDigestException", throwable.getCause() instanceof com.artipie.docker.error.InvalidDigestException);
        MatcherAssert.assertThat("Exception message contains calculated digest", throwable.getCause().getMessage(), Matchers.containsString("3a6eb0790f39ac87c94f3856b2dd2c5d110e6811602261a9a923d3bb23adc8b7"));
        MatcherAssert.assertThat("Exception message contains expected digest", throwable.getCause().getMessage(), Matchers.containsString(digest));
        return null;
    });
    putFuture.get();
}
```

The changes include:

* Importing `MatcherAssert` and `Matchers` from `org.hamcrest` package
* Adding `throws` clause for `ExecutionException` and `InterruptedException` in the test method signature
* Replacing `com.google.common.base.Throwables.getRootCause` with `throwable.getCause()`
* Replacing `new com.artipie.docker.asto.IsNot<>(new com.artipie.docker.asto.IsNull<>()` with `throwable != null`
* Replacing `com.artipie.docker.asto.StringContains` with `Matchers.containsString`
* Adding `StandardCharsets.UTF_8` when calling `getBytes` on the `"data"` string
* Replacing `CompletableFuture.allOf()` with `putFuture.get()` to wait for the completion of the `put` operation
* Using `exceptionally` method on `CompletableFuture` to handle exceptions and return `null` if an exception occurs.