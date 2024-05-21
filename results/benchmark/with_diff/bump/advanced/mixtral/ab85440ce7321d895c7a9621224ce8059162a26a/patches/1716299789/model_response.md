Here's a suggested patch for the failing client code:

```java
// TODO: review this AI generated patch!
@org.junit.jupiter.api.Test
void failsOnDigestMismatch() {
    final com.artipie.asto.memory.InMemoryStorage storage = new com.artipie.asto.memory.InMemoryStorage();
    final com.artipie.docker.asto.AstoBlobs blobs = new com.artipie.docker.asto.AstoBlobs(storage, new com.artipie.docker.asto.DefaultLayout(), new com.artipie.docker.RepoName.Simple("any"));
    final java.lang.String digest = "123";
    com.artipie.docker.asto.CheckedBlobSource checkedBlobSource = new com.artipie.docker.asto.CheckedBlobSource(new com.artipie.asto.Content.From("data".getBytes()), new com.artipie.docker.Digest.Sha256(digest));
    com.artipie.docker.asto.CheckedBlob checkedBlob = blobs.put(checkedBlobSource).toCompletableFuture().join();
    org.hamcrest.MatcherAssert.assertThat("Exception thrown", checkedBlob.cause(), new com.artipie.docker.asto.IsNot<>(new com.artipie.docker.asto.IsNull<>()));
    org.hamcrest.MatcherAssert.assertThat("Exception is InvalidDigestException", com.google.common.base.Throwables.getRootCause(checkedBlob.cause()), new org.hamcrest.core.IsInstanceOf(com.artipie.docker.error.InvalidDigestException.class));
    org.hamcrest.MatcherAssert.assertThat("Exception message contains calculated digest", com.google.common.base.Throwables.getRootCause(checkedBlob.cause()).getMessage(), new org.hamcrest.core.StringStartsWith(new org.hamcrest.core.StringValue(new java.lang.StringBuilder("3a6eb0790f39ac87c94f3856b2dd2c5d110e6811602261a9a923d3bb23adc8b7").toString())));
    org.hamcrest.MatcherAssert.assertThat("Exception message contains expected digest", com.google.common.base.Throwables.getRootCause(checkedBlob.cause()).getMessage(), new org.hamcrest.core.StringContains(digest));
    return java.util.concurrent.CompletableFuture.allOf();
}
```

The suggested changes include:

* Creating a `checkedBlobSource` variable to store the `CheckedBlobSource` instance.
* Changing the call to `blobs.put()` to use the `join()` method instead of `toCompletableFuture()` and `handle()`.
* Updating the `MatcherAssert` statements to use `checkedBlob.cause()` instead of `throwable`.

These changes should resolve the error message:

> [ERROR] /docker-adapter/src/test/java/com/artipie/docker/asto/AstoBlobsITCase.java:[72,349] ';' expected

by fixing the syntax error caused by the missing semicolon and the incorrect usage of `handle()`.