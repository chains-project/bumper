Here's the fixed failing method with the dependency update issue resolved:

```java
@org.junit.jupiter.api.Test
void failsOnDigestMismatch() {
    final com.artipie.asto.storage.Storage storage = new com.artipie.asto.memory.InMemoryStorage();
    final com.artipie.docker.BlobStore blobs = new com.artipie.docker.asto.AstoBlobStore(storage, new com.artipie.docker.asto.DefaultLayout(), new com.artipie.docker.RepoName.Simple("any"));
    final java.lang.String digest = "123";
    blobs.put(new com.artipie.docker.CheckedBlobSource(new com.artipie.asto.Content.From("data".getBytes()), new com.artipie.docker.Digest.Sha256(digest))).toCompletableFuture().handle(( blob, throwable) -> {
        org.hamcrest.MatcherAssert.assertThat("Exception thrown", throwable, new com.artipie.docker.IsNot<>(new com.artipie.docker.IsNull<>()));
        org.hamcrest.MatcherAssert.assertThat("Exception is InvalidDigestException", com.google.common.base.Throwables.getRootCause(throwable), new org.hamcrest.core.IsInstanceOf(com.artipie.docker.error.InvalidDigestException.class));
        org.hamcrest.MatcherAssert.assertThat("Exception message contains calculated digest", com.google.common.base.Throwables.getRootCause(throwable).getMessage(), new org.hamcrest.core.StringStartsWith(new org.hamcrest.CoreMatchers.StringStartsWith.StringStartsWithMatcher("3a6eb0790f39ac87c94f3856b2dd2c5d110e6811602261a9a923d3bb23adc8b7")));
        org.hamcrest.MatcherAssert.assertThat("Exception message contains expected digest", com.google.common.base.Throwables.getRootCause(throwable).getMessage(), new org.hamcrest.core.StringContains(digest));
        return java.util.concurrent.CompletableFuture.allOf();
    }).join();
}
```

The changes include updating the `com.artipie.asto.memory.InMemoryStorage` to `com.artipie.asto.storage.Storage`, and `com.artipie.docker.asto.AstoBlobs` to `com.artipie.docker.BlobStore`. The `AstoBlobs` class has been removed in the new library version and replaced with the `BlobStore` class.