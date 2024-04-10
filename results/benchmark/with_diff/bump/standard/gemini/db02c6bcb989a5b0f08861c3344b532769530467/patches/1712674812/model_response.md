```java
@org.junit.jupiter.api.Test
void failsOnDigestMismatch() {
    final com.artipie.asto.memory.InMemoryStorage storage = new com.artipie.asto.memory.InMemoryStorage();
    final com.artipie.docker.asto.AstoBlobs blobs = new com.artipie.docker.asto.AstoBlobs(storage, new com.artipie.docker.asto.DefaultLayout(), new com.artipie.docker.RepoName.Simple("any"));
    final java.lang.String digest = "123";
    blobs.put(new com.artipie.docker.asto.CheckedBlobSource(new com.artipie.asto.Content.From("data".getBytes()), new com.artipie.docker.Digest.Sha256(digest))).toCompletableFuture().handle(( blob, throwable) -> {
        org.hamcrest.MatcherAssert.assertThat("Exception thrown", throwable, new com.artipie.docker.asto.IsNot<>(new com.artipie.docker.asto.IsNull<>()));
        org.hamcrest.MatcherAssert.assertThat("Exception is InvalidDigestException", com.google.common.base.Throwables.getRootCause(throwable), new org.hamcrest.core.IsInstanceOf(com.artipie.docker.error.InvalidDigestException.class));
        final boolean containsCalculatedDigest = com.google.common.base.Throwables.getRootCause(throwable).getMessage().contains("3a6eb0790f39ac87c94f3856b2dd2c5d110e6811602261a9a923d3bb23adc8b7");
        org.hamcrest.MatcherAssert.assertThat("Exception message contains calculated digest", containsCalculatedDigest, new org.hamcrest.core.IsEqual(true));
        final boolean containsExpectedDigest = com.google.common.base.Throwables.getRootCause(throwable).getMessage().contains(digest);
        org.hamcrest.MatcherAssert.assertThat("Exception message contains expected digest", containsExpectedDigest, new org.hamcrest.core.IsEqual(true));
        return java.util.concurrent.CompletableFuture.allOf();
    }).join();
}
```