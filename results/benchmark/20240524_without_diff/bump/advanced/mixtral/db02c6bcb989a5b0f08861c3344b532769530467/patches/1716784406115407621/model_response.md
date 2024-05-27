Here's the fixed `fixesDigestMismatch()` method:

```java
@org.junit.jupiter.api.Test
void fixesDigestMismatch() {
    final com.artipie.asto.memory.InMemoryStorage storage = new com.artipie.asto.memory.InMemoryStorage();
    final com.artipie.docker.asto.AstoBlobs blobs = new com.artipie.docker.asto.AstoBlobs(storage, new com.artipie.docker.asto.DefaultLayout(), new com.artipie.docker.RepoName.Simple("any"));
    final java.lang.String digest = "123";
    com.artipie.docker.asto.CheckedBlobSource checkedBlobSource = new com.artipie.docker.asto.CheckedBlobSource(new com.artipie.asto.Content.From("data".getBytes()), new com.artipie.docker.Digest.Sha256(digest));
    com.artipie.docker.asto.PutResult putResult = blobs.put(checkedBlobSource);
    java.util.concurrent.CompletableFuture<com.artipie.docker.asto.PutResult> completableFuture = putResult.toCompletableFuture();
    completableFuture.handle(( blob, throwable) -> {
        org.hamcrest.MatcherAssert.assertThat("Exception thrown", throwable, new org.hamcrest.core.IsInstanceOf(com.artipie.docker.asto.IsNull.class));
        org.hamcrest.MatcherAssert.assertThat("Exception is InvalidDigestException", com.google.common.base.Throwables.getRootCause(throwable), new org.hamcrest.core.IsInstanceOf(com.artipie.docker.error.InvalidDigestException.class));
        org.hamcrest.MatcherAssert.assertThat("Exception message contains calculated digest", com.google.common.base.Throwables.getRootCause(throwable).getMessage(), new org.hamcrest.core.StringStartsWith(new org.hamcrest.core.StringValue(new java.lang.StringBuilder("3a6eb0790f39ac87c94f3856b2dd2c5d110e6811602261a9a923d3bb23adc8b7").toString())));
        return null;
    });
    org.hamcrest.MatcherAssert.assertThat("Exception message contains expected digest", com.google.common.base.Throwables.getRootCause(throwable).getMessage(), new org.hamcrest.core.StringContains(digest));
    return java.util.concurrent.CompletableFuture.allOf();
}
```

The changes include:

1. Declaring and initializing `checkedBlobSource` and `putResult` variables to make the code easier to read.
2. Changing the first `MatcherAssert.assertThat` statement to check if the exception is an instance of `IsNull` instead of checking for a non-null value.
3. Adding a `return null;` statement in the lambda expression for the `handle` method to satisfy the compiler.

Please review the changes and test thoroughly before merging.