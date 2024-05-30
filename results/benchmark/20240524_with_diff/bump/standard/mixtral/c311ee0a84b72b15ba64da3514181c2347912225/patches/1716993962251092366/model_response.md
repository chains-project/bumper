Here's a proposed patch for the given client code:

```java
import org.hamcrest.Matchers;
import org.junit.jupiter.api.Test;
import java.nio.charset.StandardCharsets;
import java.util.concurrent.CompletableFuture;

@Test
void failsOnDigestMismatch() {
    final com.artipie.asto.memory.InMemoryStorage storage = new com.artipie.asto.memory.InMemoryStorage();
    final com.artipie.docker.asto.AstoBlobs blobs = new com.artipie.docker.asto.AstoBlobs(storage, new com.artipie.docker.asto.DefaultLayout(), new com.artipie.docker.RepoName.Simple("any"));
    final String digest = "123";
    blobs.put(new com.artipie.docker.asto.CheckedBlobSource(new com.artipie.asto.Content.From("data".getBytes(StandardCharsets.UTF_8)), new com.artipie.docker.Digest.Sha256(digest))).toCompletableFuture().handle(( blob, throwable) -> {
        MatcherAssert.assertThat("Exception thrown", throwable, Matchers.notNullValue());
        MatcherAssert.assertThat("Exception is InvalidDigestException", throwable, Matchers.instanceOf(com.artipie.docker.error.InvalidDigestException.class));
        MatcherAssert.assertThat("Exception message contains calculated digest", throwable.getMessage(), Matchers.stringContainsInOrder(
            "3a6eb0790f39ac87c94f3856b2dd2c5d110e6811602261a9a923d3bb23adc8b7",
            digest
        ));
        return CompletableFuture.allOf();
    }).join();
}
```

The changes made are:

1. Import `Matchers` class from `org.hamcrest` package.
2. Replace `com.google.common.base.Throwables.getRootCause(throwable)` with `throwable` directly.
3. Replace `new com.artipie.docker.asto.StringContains<>(true, "3a6eb0790f39ac87c94f3856b2dd2c5d110e6811602261a9a923d3bb23adc8b7")` with `"3a6eb0790f39ac87c94f3856b2dd2c5d110e6811602261a9a923d3bb23adc8b7"`.
4. Use `MatcherAssert.assertThat` with `Matchers.stringContainsInOrder` instead of `StringContains`.
5. Replace `new com.artipie.docker.asto.IsNull<>()` with `Matchers.notNullValue()`.
6. Replace `com.google.common.base.Throwables.getRootCause(throwable)` with `throwable`.
7. Replace `new com.artipie.docker.error.InvalidDigestException.class` with `com.artipie.docker.error.InvalidDigestException.class`.
8. Replace `new org.hamcrest.core.StringContains(true, "3a6eb0790f39ac87c94f3856b2dd2c5d110e6811602261a9a923d3bb23adc8b7")` with `"3a6eb0790f39ac87c94f3856b2dd2c5d110e6811602261a9a923d3bb23adc8b7"`.
9. Replace `new org.hamcrest.core.StringContains(true, digest)` with `digest`.
10. Replace `new org.hamcrest.core.IsInstanceOf(com.artipie.docker.error.InvalidDigestException.class)` with `Matchers.instanceOf(com.artipie.docker.error.InvalidDigestException.class)`.
11. Replace `new org.hamcrest.core.IsNot<>(new com.artipie.docker.asto.IsNull<>()` with `Matchers.notNullValue()`.
12. Replace `java.lang.String` with `String` for variable declarations.
13. Replace `new com.artipie.asto.Content.From("data".getBytes())` with `new com.artipie.asto.Content.From("data".getBytes(StandardCharsets.UTF_8))`.

These changes should resolve the error caused by the updated library version.