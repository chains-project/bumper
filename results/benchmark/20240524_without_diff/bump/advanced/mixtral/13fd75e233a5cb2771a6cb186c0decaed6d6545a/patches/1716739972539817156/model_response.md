Here's a possible patch for the failing client code:

```java
import org.hamcrest.Matchers;
import java.util.concurrent.CompletableFuture;
import java.util.concurrent.ExecutionException;

@org.junit.jupiter.api.Test
void failsOnDigestMismatch() throws ExecutionException, InterruptedException {
    final com.artipie.asto.memory.InMemoryStorage storage = new com.artipie.asto.memory.InMemoryStorage();
    final com.artipie.docker.asto.AstoBlobs blobs = new com.artipie.docker.asto.AstoBlobs(storage, new com.artipie.docker.asto.DefaultLayout(), new com.artipie.docker.RepoName.Simple("any"));
    final java.lang.String digest = "123";
    CompletableFuture<Void> putResult = blobs.put(new com.artipie.docker.asto.CheckedBlobSource(new com.artipie.asto.Content.From("data".getBytes()), new com.artipie.docker.Digest.Sha256(digest)));
    putResult.toCompletableFuture().get();
    try {
        putResult.get();
    } catch (ExecutionException e) {
        org.hamcrest.MatcherAssert.assertThat("Exception thrown", e.getCause() instanceof com.artipie.docker.asto.IsNull);
        org.hamcrest.MatcherAssert.assertThat("Exception is InvalidDigestException", com.google.common.base.Throwables.getRootCause(e.getCause()) instanceof com.artipie.docker.error.InvalidDigestException);
        org.hamcrest.MatcherAssert.assertThat("Exception message contains calculated digest", Matchers.containsString(com.google.common.base.Throwables.getRootCause(e.getCause()).getMessage(), "3a6eb0790f39ac87c94f3856b2dd2c5d110e6811602261a9a923d3bb23adc8b7"));
        org.hamcrest.MatcherAssert.assertThat("Exception message contains expected digest", Matchers.containsString(com.google.common.base.Throwables.getRootCause(e.getCause()).getMessage(), digest));
    }
}
```

The main changes are:

* Importing `Matchers` from `hamcrest` to use its `containsString` method.
* Changing the exception handling to use `try-catch` instead of `handle` to avoid the `StringContains` constructor error.
* Using `get` method of `CompletableFuture` to wait for the completion of `put` method.
* Using `MatcherAssert.assertThat` with `containsString` instead of `StringContains`.
* Wrapping the `put` method call in a `try-catch` block to handle exceptions.
* Adding `throws` clause to the method signature to handle checked exceptions.

Note: The patch assumes that the `IsNot` class is available in the `com.artipie.docker.asto` package and can be used with `MatcherAssert.assertThat`. If this class is not available, you may need to modify the exception handling accordingly.