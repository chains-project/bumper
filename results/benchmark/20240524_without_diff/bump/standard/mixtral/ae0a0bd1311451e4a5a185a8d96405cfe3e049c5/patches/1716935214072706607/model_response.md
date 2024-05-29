Here's a possible patch for the code:

```java
import org.hamcrest.Matchers;
import java.util.concurrent.CompletableFuture;

@org.junit.jupiter.api.Test
void failsOnDigestMismatch() {
    final com.artipie.asto.memory.InMemoryStorage storage = new com.artipie.asto.memory.InMemoryStorage();
    final com.artipie.docker.asto.AstoBlobs blobs = new com.artipie.docker.asto.AstoBlobs(storage, new com.artipie.docker.asto.DefaultLayout(), new com.artipie.docker.RepoName.Simple("any"));
    final java.lang.String digest = "123";
    blobs.put(new com.artipie.docker.asto.CheckedBlobSource(new com.artipie.asto.Content.From("data".getBytes()), new com.artipie.docker.Digest.Sha256(digest))).toCompletableFuture().handle(( blob, throwable) -> {
        org.hamcrest.MatcherAssert.assertThat("Exception thrown", throwable, Matchers.notNullValue());
        org.hamcrest.MatcherAssert.assertThat("Exception is InvalidDigestException", throwable, Matchers.instanceOf(com.artipie.docker.error.InvalidDigestException.class));
        org.hamcrest.MatcherAssert.assertThat("Exception message contains calculated digest", throwable.getMessage(), Matchers.stringContainsInOrder(digest, "3a6eb0790f39ac87c94f3856b2dd2c5d110e6811602261a9a923d3bb23adc8b7"));
        return java.util.concurrent.CompletableFuture.allOf();
    }).join();
}
```

The changes made are:

* Importing `Matchers` class from `org.hamcrest` package.
* Replacing `new com.artipie.docker.asto.IsNot<>(new com.artipie.docker.asto.IsNull<>())` with `Matchers.notNullValue()`.
* Replacing `new org.hamcrest.core.StringContains(true, "3a6eb0790f39ac87c94f3856b2dd2c5d110e6811602261a9a923d3bb23adc8b7")` with `"3a6eb0790f39ac87c94f3856b2dd2c5d110e6811602261a9a923d3bb23adc8b7"` and using `Matchers.stringContainsInOrder` method instead of `StringContains` constructor.
* Replacing `new org.hamcrest.core.StringContains(true, digest)` with `digest` and using `stringContainsInOrder` method instead of `StringContains` constructor.

These changes should fix the compilation error and make the test pass if the expected exception is thrown and has the expected message.