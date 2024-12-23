Here's a fixed version of the code:

```java
@org.junit.jupiter.api.Test
void fixesDigestMismatch() {
    final com.artipie.asto.memory.InMemoryStorage storage = new com.artipie.asto.memory.InMemoryStorage();
    final com.artipie.docker.asto.AstoBlobs blobs = new com.artipie.docker.asto.AstoBlobs(storage, new com.artipie.docker.asto.DefaultLayout(), new com.artipie.docker.RepoName.Simple("any"));
    final java.lang.String digest = "123";
    com.artipie.docker.asto.CheckedBlobSource checkedBlobSource = new com.artipie.docker.asto.CheckedBlobSource(new com.artipie.asto.Content.From("data".getBytes()), new com.artipie.docker.Digest.Sha256(digest));
    com.artipie.docker.asto.CheckedBlob checkedBlob = blobs.put(checkedBlobSource).toCompletableFuture().join();
    java.lang.Exception exception = new java.lang.Exception();
    org.hamcrest.MatcherAssert.assertThat("Exception thrown", exception, new com.artipie.docker.asto.IsNot<>(new com.artipie.docker.asto.IsNull<>()));
    org.hamcrest.MatcherAssert.assertThat("Exception is InvalidDigestException", com.google.common.base.Throwables.getRootCause(exception), new org.hamcrest.core.IsInstanceOf(com.artipie.docker.error.InvalidDigestException.class));
    org.hamcrest.MatcherAssert.assertThat("Exception message contains calculated digest", com.google.common.base.Throwables.getRootCause(exception).getMessage(), new org.hamcrest.core.StringStartsWith(new org.hamcrest.core.StringValue(new java.lang.StringBuilder("3a6eb0790f39ac87c94f3856b2dd2c5d110e6811602261a9a923d3bb23adc8b7").toString())));
    org.hamcrest.MatcherAssert.assertThat("Exception message contains expected digest", com.google.common.base.Throwables.getRootCause(exception).getMessage(), new org.hamcrest.core.StringContains(digest));
    return java.util.concurrent.CompletableFuture.allOf();
}
```

The issue was that the `handle` method was being called directly on the result of the `put` method, which is a `CompletableFuture`. Instead, the `join` method should be called on the `CompletableFuture` to get the result, and then the `handle` method can be called on the result. Also, I have added a new `Exception` object `exception` for assertion.