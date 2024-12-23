Here is the fixed version of the code:

```java
@org.junit.jupiter.api.Test
void fixesDigestMismatch() {
    final com.artipie.asto.memory.InMemoryStorage storage = new com.artipie.asto.memory.InMemoryStorage();
    final com.artipie.docker.asto.AstoBlobs blobs = new com.artipie.docker.asto.AstoBlobs(storage, new com.artipie.docker.asto.DefaultLayout(), new com.artipie.docker.RepoName.Simple("any"));
    final java.lang.String digest = "123";
    com.artipie.docker.asto.CheckedBlobSource source = new com.artipie.docker.asto.CheckedBlobSource(new com.artipie.asto.Content.From("data".getBytes()), new com.artipie.docker.Digest.Sha256(digest));
    com.artipie.docker.asto.Blob blob = blobs.put(source).toCompletableFuture().join();
    java.util.concurrent.CompletableFuture.allOf();
    org.hamcrest.MatcherAssert.assertThat("Exception thrown", blob, new com.artipie.docker.asto.IsNot<>(new com.artipie.docker.asto.IsNull<>()));
    org.hamcrest.MatcherAssert.assertThat("Exception is InvalidDigestException", com.google.common.base.Throwables.getRootCause(blob.exception()), new org.hamcrest.core.IsInstanceOf(com.artipie.docker.error.InvalidDigestException.class));
    org.hamcrest.MatcherAssert.assertThat("Exception message contains calculated digest", new org.hamcrest.core.StringContains(com.google.common.base.Throwables.getRootCause(blob.exception()).getMessage()), "3a6eb0790f39ac87c94f3856b2dd2c5d110e6811602261a9a923d3bb23adc8b7");
    org.hamcrest.MatcherAssert.assertThat("Exception message contains expected digest", new org.hamcrest.core.StringContains(com.google.common.base.Throwables.getRootCause(blob.exception()).getMessage()), digest);
}
```

The original code had some issues with the placement of semicolons and the way exceptions were being handled. I've fixed these issues and also stored the result of the `put` method in a variable so that it can be used later on in the code.