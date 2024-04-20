Here's the fixed failsOnDigestMismatch method using the new library version:

```java
import org.hamcrest.MatcherAssert;
import org.hamcrest.Matchers;
import java.util.concurrent.CompletableFuture;

@org.junit.jupiter.api.Test
void failsOnDigestMismatch() {
    final com.artipie.asto.memory.InMemoryStorage storage = new com.artipie.asto.memory.InMemoryStorage();
    final com.artipie.docker.asto.AstoBlobs blobs = new com.artipie.docker.asto.AstoBlobs(storage, new com.artipie.docker.asto.DefaultLayout(), new com.artipie.docker.RepoName.Simple("any"));
    final java.lang.String digest = "123";
    blobs.put(new com.artipie.docker.asto.CheckedBlobSource(new com.artipie.asto.Content.From("data".getBytes()), new com.artipie.docker.Digest.Sha256(digest))).toCompletableFuture().handle(( blob, throwable) -> {
        MatcherAssert.assertThat("Exception thrown", throwable, Matchers.notNullValue());
        MatcherAssert.assertThat("Exception is InvalidDigestException", com.google.common.base.Throwables.getRootCause(throwable), Matchers.instanceOf(com.artipie.docker.error.InvalidDigestException.class));
        MatcherAssert.assertThat("Exception message contains calculated digest", com.google.common.base.Throwables.getRootCause(throwable).getMessage(), Matchers.stringContainsInOrder(new String[]{"3a6eb0790f39ac87c94f3856b2dd2c5d110e6811602261a9a923d3bb23adc8b7", digest}));
        return CompletableFuture.allOf();
    }).join();
}
```

The changes I made:

1. Replaced `new com.artipie.docker.asto.IsNot<>(new com.artipie.docker.asto.IsNull<>()` with `Matchers.notNullValue()`.
2. Replaced `new org.hamcrest.core.IsInstanceOf(com.artipie.docker.error.InvalidDigestException.class)` with `Matchers.instanceOf(com.artipie.docker.error.InvalidDigestException.class)`.
3. Replaced `new org.hamcrest.core.StringContains(true, "3a6eb0790f39ac87c94f3856b2dd2c5d110e6811602261a9a923d3bb23adc8b7")` with `Matchers.stringContainsInOrder(new String[]{"3a6eb0790f39ac87c94f3856b2dd2c5d110e6811602261a9a923d3bb23adc8b7"})`.
4. Replaced `new org.hamcrest.core.StringContains(true, digest)` with `Matchers.stringContainsInOrder(new String[]{digest})`.

These changes use the new library version's methods for string matching and null value checking.