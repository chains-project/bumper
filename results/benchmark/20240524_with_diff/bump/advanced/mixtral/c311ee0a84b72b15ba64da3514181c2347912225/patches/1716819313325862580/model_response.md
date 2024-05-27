Here's a proposed patch for the given failing client code:

```java
import org.hamcrest.MatcherAssert;
import org.hamcrest.Matchers;
import java.nio.charset.StandardCharsets;
import java.util.concurrent.CompletableFuture;

@org.junit.jupiter.api.Test
void failsOnDigestMismatch() {
    final com.artipie.asto.memory.InMemoryStorage storage = new com.artipie.asto.memory.InMemoryStorage();
    final com.artipie.docker.asto.AstoBlobs blobs = new com.artipie.docker.asto.AstoBlobs(storage, new com.artipie.docker.asto.DefaultLayout(), new com.artipie.docker.RepoName.Simple("any"));
    final String digest = "123";
    blobs.put(new com.artipie.docker.asto.CheckedBlobSource(new com.artipie.asto.Content.From("data".getBytes(StandardCharsets.UTF_8)), new com.artipie.docker.Digest.Sha256(digest))).toCompletableFuture().handle(( blob, throwable) -> {
        MatcherAssert.assertThat("Exception thrown", throwable, Matchers.notNullValue());
        MatcherAssert.assertThat("Exception is InvalidDigestException", throwable, Matchers.instanceOf(com.artipie.docker.error.InvalidDigestException.class));
        MatcherAssert.assertThat("Exception message contains calculated digest", throwable.getMessage(), Matchers.stringContainsInOrder(new String[]{"3a6eb0790f39ac87c94f3856b2dd2c5d110e6811602261a9a923d3bb23adc8b7", digest}));
        return CompletableFuture.allOf();
    }).join();
}
```

The changes include:

* Importing `Matchers` from `org.hamcrest` package.
* Using `Matchers.notNullValue()` instead of `new com.artipie.docker.asto.IsNot<>(new com.artipie.docker.asto.IsNull<String>)()`.
* Using `Matchers.instanceOf(com.artipie.docker.error.InvalidDigestException.class)` instead of `new com.google.common.base.IsInstanceOf(com.artipie.docker.error.InvalidDigestException.class)`.
* Using `MatcherAssert.assertThat("Exception message contains calculated digest", throwable.getMessage(), Matchers.stringContainsInOrder(new String[]{"3a6eb0790f39ac87c94f3856b2dd2c5d110e6811602261a9a923d3bb23adc8b7", digest}))` instead of `new org.hamcrest.core.StringContains(true, "3a6eb0790f39ac87c94f3856b2dd2c5d110e6811602261a9a923d3bb23adc8b7"), new org.hamcrest.core.StringContains(true, digest)`.
* Using `StandardCharsets.UTF_8` instead of the removed `"data".getBytes()`.
* Replacing `CompletableFuture.allOf()` with `CompletableFuture.allOf()` (no changes).