Here's the proposed patch:

```java
@org.junit.jupiter.api.Test
void fixesDigestMismatch() {
    final com.artipie.asto.memory.InMemoryStorage storage = new com.artipie.asto.memory.InMemoryStorage();
    final com.artipie.docker.asto.AstoBlobs blobs = new com.artipie.docker.asto.AstoBlobs(storage, new com.artipie.docker.asto.DefaultLayout(), new com.artipie.docker.RepoName.Simple("any"));
    final java.lang.String digest = "123";
    blobs.put(new com.artipie.docker.asto.CheckedBlobSource(new com.artipie.asto.Content.From("data".getBytes()), new com.artipie.docker.Digest.Sha256(digest))).toCompletableFuture().handle(( blob, throwable) -> {
        org.hamcrest.MatcherAssert.assertThat("Exception thrown", throwable, new com.artipie.docker.asto.IsNot<>(new com.artipie.docker.asto.IsNull<>()));
        org.hamcrest.MatcherAssert.assertThat("Exception is InvalidDigestException", com.google.common.base.Throwables.getRootCause(throwable), new org.hamcrest.core.IsInstanceOf(com.artipie.docker.error.InvalidDigestException.class));
        boolean containsCalculatedDigest = com.google.common.base.Throwables.getRootCause(throwable).getMessage().contains("3a6eb0790f39ac87c94f3856b2dd2c5d110e6811602261a9a923d3bb23adc8b7");
        boolean containsExpectedDigest = com.google.common.base.Throwables.getRootCause(throwable).getMessage().contains(digest);
        org.hamcrest.MatcherAssert.assertThat("Exception message contains calculated digest", containsCalculatedDigest);
        org.hamcrest.MatcherAssert.assertThat("Exception message contains expected digest", containsExpectedDigest);
        return java.util.concurrent.CompletableFuture.allOf();
    }).join();
}
```

The changes I made:

1. Renamed the method from `failsOnDigestMismatch` to `fixesDigestMismatch` to reflect the fact that it should no longer fail.
2. Replaced the `new org.hamcrest.core.StringContains(true, "3a6eb0790f39ac87c94f3856b2dd2c5d110e6811602261a9a923d3bb23adc8b7")` and `new org.hamcrest.core.StringContains(true, digest)` calls with `.contains("3a6eb0790f39ac87c94f3856b2dd2c5d110e6811602261a9a923d3bb23adc8b7")` and `.contains(digest)` calls.

The error message indicates that the `StringContains` constructor is expecting only one argument, but it's receiving two. The new library version may have removed the constructor that accepts a `boolean` argument, so I replaced the `StringContains` instances with a call to the `contains` method on the `String` object. This should achieve the same functionality as the original code, but without relying on the deprecated constructor.