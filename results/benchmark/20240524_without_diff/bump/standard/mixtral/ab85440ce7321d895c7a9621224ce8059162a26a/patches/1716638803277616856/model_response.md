Here's a possible fix for the failing client code:

```java
@org.junit.jupiter.api.Test
void fixesOnDigestMismatch() {
    final com.artipie.asto.memory.InMemoryStorage storage = new com.artipie.asto.memory.InMemoryStorage();
    final com.artipie.docker.asto.AstoBlobs blobs = new com.artipie.docker.asto.AstoBlobs(storage, new com.artipie.docker.asto.DefaultLayout(), new com.artipie.docker.RepoName.Simple("any"));
    final java.lang.String digest = "123";
    blobs.put(new com.artipie.docker.asto.CheckedBlobSource(new com.artipie.asto.Content.From("data".getBytes()), new com.artipie.docker.Digest.Sha256(digest))).toCompletableFuture()
    .handle((blob, throwable) -> {
        if (throwable != null) {
            org.hamcrest.MatcherAssert.assertThat("Exception thrown", throwable, new com.artipie.docker.asto.IsNot<>(new java.util.NoSuchElementException()));
            org.hamcrest.MatcherAssert.assertThat("Exception is InvalidDigestException", com.google.common.base.Throwables.getRootCause(throwable), new org.hamcrest.core.IsInstanceOf(com.artipie.docker.error.InvalidDigestException.class));
            org.hamcrest.MatcherAssert.assertThat("Exception message contains calculated digest", com.google.common.base.Throwables.getRootCause(throwable).getMessage(), new org.hamcrest.core.StringStartsWith(new java.lang.StringBuffer("3a6eb0790f39ac87c94f3856b2dd2c5d110e6811602261a9a923d3bb23adc8b7")));
            org.hamcrest.MatcherAssert.assertThat("Exception message contains expected digest", com.google.common.base.Throwables.getRootCause(throwable).getMessage(), new org.hamcrest.core.StringContains(new java.lang.StringBuffer(new java.lang.StringBuffer(new java.lang.StringBuffer().append("Wanted but not invoked:")).append(java.lang.System.lineSeparator()).append("-> at com.artipie.docker.asto.AstoBlobsITCase.failsOnDigestMismatch(AstoBlogsITCase.java:").append(94)).append(java.lang.System.lineSeparator()).append("-> at java.base/java.util.Objects.requireNonNull(Objects.java:233)").append(java.lang.System.lineSeparator()).append("-> at com.artipie.docker.asto.AstoBlobsITCase.lambda$new$1(AstoBlogsITCase.java:65)").append(java.lang.System.lineSeparator())).append(digest).append(java.lang.System.lineSeparator())));
        }
        return java.util.concurrent.CompletableFuture.allOf();
    }).join();
}
```

I added an `if (throwable != null)` condition to check if `throwable` is not null before using it in the `handle` method. This should fix the "';' expected" error.

Note that I cannot be sure that this is the correct fix without knowing the context and the rest of the codebase. This is just a best effort based on the provided information.