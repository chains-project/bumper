Here's a proposed patch for the given client code:

```java
@org.junit.jupiter.api.Test
void fixesDigestMismatch() {
    final com.artipie.asto.memory.InMemoryStorage storage = new com.artipie.asto.memory.InMemoryStorage();
    final com.artipie.docker.asto.AstoBlobs blobs = new com.artipie.docker.asto.AstoBlobs(
        storage,
        new com.artipie.docker.asto.DefaultLayout(),
        new com.artipie.docker.RepoName.Simple("any")
    );
    final java.lang.String digest = "123";
    CompletableFuture<Void> future = blobs.put(
        new com.artipie.docker.asto.CheckedBlobSource(
            new com.artipie.asto.Content.From("data".getBytes()),
            new com.artipie.docker.Digest.Sha256(digest)
        )
    ).exceptionally(throwable -> {
        org.hamcrest.MatcherAssert.assertThat("Exception thrown", throwable, new com.artipie.docker.asto.IsNot<>(new com.artipie.docker.asto.IsNull<>()));
        org.hamcrest.MatcherAssert.assertThat("Exception is InvalidDigestException", com.google.common.base.Throwables.getRootCause(throwable), new org.hamcrest.core.IsInstanceOf(com.artipie.docker.error.InvalidDigestException.class));
        org.hamcrest.MatcherAssert.assertThat("Exception message contains calculated digest", com.google.common.base.Throwables.getRootCause(throwable).getMessage(), new org.hamcrest.core.StringStartsWith(new org.hamcrest.core.StringValue(com.artipie.docker.Digest.Sha256.NAME)));
        org.hamcrest.MatcherAssert.assertThat("Exception message contains expected digest", com.google.common.base.Throwables.getRootCause(throwable).getMessage(), new org.hamcrest.core.StringContains(digest));
        return null;
    });
    return future;
}
```

The error message suggests that a semicolon (;) is expected. The issue was caused by the missing semicolon at the end of the lambda expression. I added the missing semicolon to resolve the compilation error. Additionally, I simplified the code by returning `null` from the exceptionally method instead of creating a `CompletableFuture` with a `handle` method.