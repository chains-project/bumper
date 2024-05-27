Here's the patched method:

```java
@org.junit.jupiter.api.Test
void fixesDigestMismatch() {
    final com.artipie.asto.memory.InMemoryStorage storage = new com.artipie.asto.memory.InMemoryStorage();
    final com.artipie.docker.asto.AstoBlobs blobs = new com.artipie.docker.asto.AstoBlobs(storage, new com.artipie.docker.asto.DefaultLayout(), new com.artipie.docker.RepoName.Simple("any"));
    final java.lang.String digest = "123";
    com.artipie.docker.asto.CheckedBlobSource checkedBlobSource = new com.artipie.docker.asto.CheckedBlobSource(new com.artipie.asto.Content.From("data".getBytes()), new com.artipie.docker.Digest.Sha256(digest));
    com.artipie.docker.asto.BlobResult blobResult = blobs.put(checkedBlobSource).toCompletableFuture().join();
    org.hamcrest.MatcherAssert.assertThat("Exception thrown", blobResult.exception(), new com.artipie.docker.asto.IsNot<>(new com.artipie.docker.asto.IsNull<>()));
    org.hamcrest.MatcherAssert.assertThat("Exception is InvalidDigestException", com.google.common.base.Throwables.getRootCause(blobResult.exception()), new org.hamcrest.core.IsInstanceOf(com.artipie.docker.error.InvalidDigestException.class));
    org.hamcrest.MatcherAssert.assertThat("Exception message contains calculated digest", com.google.common.base.Throwables.getRootCause(blobResult.exception()).getMessage(), new org.hamcrest.core.StringStartsWith(new org.hamcrest.core.StringValue(new java.lang.StringBuilder("3a6eb0790f39ac87c94f3856b2dd2c5d110e6811602261a9a923d3bb23adc8b7").toString())));
    org.hamcrest.MatcherAssert.assertThat("Exception message contains expected digest", com.google.common.base.Throwables.getRootCause(blobResult.exception()).getMessage(), new org.hamcrest.core.StringContains(digest));
    return java.util.concurrent.CompletableFuture.allOf();
}
```

I made the following changes:

1. Changed the line `blobs.put(new com.artipie.docker.asto.CheckedBlobSource(new com.artipie.asto.Content.From("data".getBytes()), new com.artipie.docker.Digest.Sha256(digest))).toCompletableFuture().handle(( blob, throwable) -> {`
   to
   `com.artipie.docker.asto.CheckedBlobSource checkedBlobSource = new com.artipie.docker.asto.CheckedBlobSource(new com.artipie.asto.Content.From("data".getBytes()), new com.artipie.docker.Digest.Sha256(digest));`
   `com.artipie.docker.asto.BlobResult blobResult = blobs.put(checkedBlobSource).toCompletableFuture().join();`

   The reason for this change is that the `put` method returns a `BlobResult` which can be used to check for exceptions and verify the digest. The `handle` method is not necessary here.

2. Removed the unused `throwable` variable from the lambda expression.

3. Changed the line `org.hamcrest.MatcherAssert.assertThat("Exception message contains expected digest", com.google.common.base.Throwables.getRootCause(throwable).getMessage(), new org.hamcrest.core.StringContains(digest));`
   to
   `org.hamcrest.MatcherAssert.assertThat("Exception message contains expected digest", com.google.common.base.Throwables.getRootCause(blobResult.exception()).getMessage(), new org.hamcrest.core.StringContains(digest));`

   The reason for this change is that the `throwable` variable is not defined anymore, so we need to use `blobResult.exception()` instead.