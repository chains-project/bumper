Here's a possible patch for the given client code. I added a variable `exception` to store the exception thrown in the `handle` method, and changed the order of the `assertThat` calls to avoid the "';' expected" error:

```java
@org.junit.jupiter.api.Test
void failsOnDigestMismatch() {
    final com.artipie.asto.memory.InMemoryStorage storage = new com.artipie.asto.memory.InMemoryStorage();
    final com.artipie.docker.asto.AstoBlobs blobs = new com.artipie.docker.asto.AstoBlobs(storage, new com.artipie.docker.asto.DefaultLayout(), new com.artipie.docker.RepoName.Simple("any"));
    final java.lang.String digest = "123";
    com.artipie.docker.asto.CheckedBlobSource checkedBlobSource = new com.artipie.docker.asto.CheckedBlobSource(new com.artipie.asto.Content.From("data".getBytes()), new com.artipie.docker.Digest.Sha256(digest));
    blobs.put(checkedBlobSource).toCompletableFuture().handle(( blob, throwable) -> {
        org.hamcrest.MatcherAssert.assertThat("Exception thrown", throwable, new com.artipie.docker.asto.IsNot<>(new com.artipie.docker.asto.IsNull<>()));
        exception = throwable;
    });
    org.hamcrest.MatcherAssert.assertThat("Exception message contains calculated digest", new org.hamcrest.core.StringContains().containsString(com.google.common.base.Throwables.getRootCause(exception).getMessage(), "3a6eb0790f39ac87c94f3856b2dd2c5d110e6811602261a9a923d3bb23adc8b7"));
    org.hamcrest.MatcherAssert.assertThat("Exception message contains expected digest", new org.hamcrest.core.StringContains().containsString(com.google.common.base.Throwables.getRootCause(exception).getMessage(), digest));
    org.hamcrest.MatcherAssert.assertThat("Exception is InvalidDigestException", com.google.common.base.Throwables.getRootCause(exception), new org.hamcrest.core.IsInstanceOf(com.artipie.docker.error.InvalidDigestException.class));
    return java.util.concurrent.CompletableFuture.allOf();
}
```

Note: I assumed that the `IsNot` and `IsNull` classes are part of the `com.artipie.docker.asto` package, based on the import statements in the original code. If this is not the case, you might need to adjust the imports accordingly.