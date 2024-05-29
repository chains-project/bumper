Here is the proposed patch:

```java
@org.junit.jupiter.api.Test
void fixesDigestMismatch() {
    final com.artipie.asto.memory.InMemoryStorage storage = new com.artipie.asto.memory.InMemoryStorage();
    final com.artipie.docker.asto.AstoBlobs blobs = new com.artipie.docker.asto.AstoBlobs(storage, new com.artipie.docker.asto.DefaultLayout(), new com.artipie.docker.RepoName.Simple("any"));
    final java.lang.String digest = "123";
    com.artipie.docker.asto.CheckedBlobSource checkedBlobSource = new com.artipie.docker.asto.CheckedBlobSource(new com.artipie.asto.Content.From("data".getBytes()), new com.artipie.docker.Digest.Sha256(digest));
    com.artipie.docker.asto.BlobSource blobSource = new com.artipie.docker.asto.RetryableBlobSource(checkedBlobSource, new com.artipie.docker.asto.FallbackBlobSource(checkedBlobSource, new com.artipie.docker.asto.NoopBlobSource()));
    com.artipie.docker.asto.PutResponse putResponse = blobs.put(blobSource);
    java.util.concurrent.CompletableFuture<com.artipie.docker.asto.PutResponse> completableFuture = putResponse.toCompletableFuture();
    completableFuture.handle(( putResponse1, throwable) -> {
        org.hamcrest.MatcherAssert.assertThat("Exception thrown", throwable, new com.artipie.docker.asto.IsNot<>(new com.artipie.docker.asto.IsNull<>()));
        org.hamcrest.MatcherAssert.assertThat("Exception is InvalidDigestException", com.google.common.base.Throwables.getRootCause(throwable), new org.hamcrest.core.IsInstanceOf(com.artipie.docker.error.InvalidDigestException.class));
        org.hamcrest.MatcherAssert.assertThat("Exception message contains calculated digest", com.google.common.base.Throwables.getRootCause(throwable).getMessage(), new org.hamcrest.core.StringStartsWith(new org.hamcrest.core.StringValue(new java.lang.StringBuilder("3a6eb0790f39ac87c94f3856b2dd2c5d110e6811602261a9a923d3bb23adc8b7").toString())));
        return null;
    });
    org.hamcrest.MatcherAssert.assertThat("Exception message contains expected digest", com.google.common.base.Throwables.getRootCause(throwable).getMessage(), new org.hamcrest.core.StringContains(digest));
    return java.util.concurrent.CompletableFuture.allOf();
}
```

This patch adds a few new variables to make the code easier to understand, and wraps the `CheckedBlobSource` in a `RetryableBlobSource` and a `FallbackBlobSource` to handle potential errors. The `PutResponse` and `CompletableFuture` are also assigned to variables for easier access.