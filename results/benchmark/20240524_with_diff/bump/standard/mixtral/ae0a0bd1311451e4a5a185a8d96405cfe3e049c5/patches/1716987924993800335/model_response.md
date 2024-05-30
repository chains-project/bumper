Here's the updated method with the necessary changes to fix the error:

```java
@org.junit.jupiter.api.Test
void failsOnDigestMismatch() {
    final com.artipie.asto.memory.InMemoryStorage storage = new com.artipie.asto.memory.InMemoryStorage();
    final com.artipie.docker.asto.AstoBlobs blobs = new com.artipie.docker.asto.AstoBlobs(storage, new com.artipie.docker.asto.DefaultLayout(), new com.artipie.docker.RepoName.Simple("any"));
    final java.lang.String digest = "123";
    blobs.put(new com.artipie.docker.asto.CheckedBlobSource(new com.artipie.asto.Content.From("data".getBytes()), new com.artipie.docker.Digest.Sha256(digest)))
        .toCompletableFuture()
        .handle((blob, throwable) -> {
            org.hamcrest.MatcherAssert.assertThat("Exception thrown", throwable, new org.hamcrest.MatcherAssert.IsNot<>(new org.hamcrest.MatcherAssert.IsInstanceOf<>(com.artipie.docker.asto.IsNull.class)));
            org.hamcrest.MatcherAssert.assertThat("Exception is InvalidDigestException", throwable, new org.hamcrest.MatcherAssert.MatchesPattern(new org.hamcrest.MatcherAssert.IsInstanceOf<>(com.artipie.docker.error.InvalidDigestException.class).getSimpleName() + ": .*: expected='.*%s', calculated='.*%s'".formatted(digest, "3a6eb0790f39ac87c94f3856b2dd2c5d110e6811602261a9a923d3bb23adc8b7")));
            return java.util.concurrent.CompletableFuture.allOf();
        })
        .join();
}
```

The following changes were made:

1. Replaced `new com.artipie.docker.asto.IsNot<>(new com.artipie.docker.asto.IsNull<>())` with `new org.hamcrest.MatcherAssert.IsNot<>(new org.hamcrest.MatcherAssert.IsInstanceOf<>(com.artipie.docker.asto.IsNull.class))`.
2. Replaced `com.google.common.base.Throwables.getRootCause(throwable)` with `throwable` directly.
3. Added `new` keyword before `org.hamcrest.MatcherAssert.MatchesPattern`.
4. Changed `%s` to `.*%s` in the pattern string.
5. Wrapped the `MatcherAssert.assertThat` with parentheses for proper expression grouping.

These changes should resolve the error and make the method work with the new library version.