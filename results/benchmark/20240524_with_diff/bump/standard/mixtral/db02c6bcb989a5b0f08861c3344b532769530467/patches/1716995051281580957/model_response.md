Here is a possible patch for the failing client code:
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
    MatcherAssert.assertThat("Exception thrown", putFuture.joinException(), Matchers.notNullValue());
    MatcherAssert.assertThat("Exception is InvalidDigestException", putFuture.joinException(), Matchers.instanceOf(com.artipie.docker.error.InvalidDigestException.class));
    MatcherAssert.assertThat("Exception message contains calculated digest", putFuture.joinException().getMessage(), Matchers.stringContains("3a6eb0790f39ac87c94f3856b2dd2c5d110e6811602261a9a923d3bb23adc8b7"));
    MatcherAssert.assertThat("Exception message contains expected digest", putFuture.joinException().getMessage(), Matchers.stringContains(digest));
}
```
The changes I made are:

* I changed the method signature to declare that it can throw `ExecutionException` and `InterruptedException`. This is because the `join()` method on a `CompletableFuture` can throw these exceptions if the future completes exceptionally.
* I changed the way the `CheckedBlobSource` is created to use `StandardCharsets.UTF_8` instead of assuming that the default charset is UTF-8.
* I changed the way the `CompletableFuture` returned by `put()` is handled. Instead of using `handle()` and `join()`, I used `toCompletableFuture()` to convert the `CompletionStage` returned by `put()` to a `CompletableFuture`, and then I called `get()` to wait for the future to complete. This has the effect of rethrowing any exception that the future completes with.
* I changed the way the Hamcrest matchers are used. Instead of using `new StringContains(true, ...)`, I used `stringContains(...)`. This is because the `StringContains` constructor that takes a boolean argument has been removed in the new library version.
* I removed the redundant `return java.util.concurrent.CompletableFuture.allOf();` statement. This is because the method does not need to return a future, since it throws exceptions instead of returning a result.