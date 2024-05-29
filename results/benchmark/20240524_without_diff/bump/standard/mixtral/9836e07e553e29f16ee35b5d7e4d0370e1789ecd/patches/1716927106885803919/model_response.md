Here's a possible patch for the given client code:

```java
import org.hamcrest.Matchers;
import java.util.concurrent.CompletableFuture;
import java.util.concurrent.ExecutionException;
import static java.util.concurrent.CompletableFuture.allOf;
import static java.util.concurrent.CompletableFuture.join;
import static org.hamcrest.MatcherAssert.assertThat;

@org.junit.jupiter.api.Test
void failsOnDigestMismatch() throws ExecutionException, InterruptedException {
    final com.artipie.asto.memory.InMemoryStorage storage = new com.artipie.asto.memory.InMemoryStorage();
    final com.artipie.docker.asto.AstoBlobs blobs = new com.artipie.docker.asto.AstoBlobs(storage, new com.artipie.docker.asto.DefaultLayout(), new com.artipie.docker.RepoName.Simple("any"));
    final java.lang.String digest = "123";
    blobs.put(new com.artipie.docker.asto.CheckedBlobSource(new com.artipie.asto.Content.From("data".getBytes()), new com.artipie.docker.Digest.Sha256(digest))).toCompletableFuture().handle(( blob, throwable) -> {
        assertThat("Exception thrown", throwable, Matchers.notNullValue());
        assertThat("Exception is InvalidDigestException", throwable.getCause(), Matchers.instanceOf(com.artipie.docker.error.InvalidDigestException.class));
        String message = throwable.getCause().getMessage();
        assertThat("Exception message contains calculated digest", message, Matchers.stringContains("3a6eb0790f39ac87c94f3856b2dd2c5d110e6811602261a9a923d3bb23adc8b7"));
        assertThat("Exception message contains expected digest", message, Matchers.stringContains(digest));
        return allOf();
    }).join();
}
```

I made the following changes to the original code:

* I imported the `Matchers` class from `org.hamcrest` package.
* I changed the `IsNot` and `IsNull` matchers to `notNullValue` matcher.
* I changed the `StringContains` matcher to `stringContains` matcher and removed the extra arguments.
* I added `throws` clause to the method signature to handle checked exceptions.
* I added `ExecutionException` and `InterruptedException` to the method signature.
* I added `join()` method call to the end of the method to wait for the completion of the `CompletableFuture`.
* I added `allOf()` method call inside the `handle` method to return a completed `CompletableFuture`.
* I extracted the message from the cause of the exception and used it in the `stringContains` matcher.