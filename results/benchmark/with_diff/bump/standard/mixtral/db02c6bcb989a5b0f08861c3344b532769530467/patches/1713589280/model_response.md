Here's the fixed method with the error resolved:

```java
@org.junit.jupiter.api.Test
void fixesDigestMismatch() {
    final com.artipie.asto.memory.InMemoryStorage storage = new com.artipie.asto.memory.InMemoryStorage();
    final com.artipie.docker.asto.AstoBlobs blobs = new com.artipie.docker.asto.AstoBlobs(storage, new com.artipie.docker.asto.DefaultLayout(), new com.artipie.docker.RepoName.Simple("any"));
    final java.lang.String digest = "123";
    blobs.put(new com.artipie.docker.asto.CheckedBlobSource(new com.artipie.asto.Content.From("data".getBytes()), new com.artipie.docker.Digest.Sha256(digest)))
         .exceptionally(throwable -> {
            org.hamcrest.MatcherAssert.assertThat("Exception thrown", throwable, new com.artipie.docker.asto.IsNot<>(new com.artipie.docker.asto.IsNull<>()));
            org.hamcrest.MatcherAssert.assertThat("Exception is InvalidDigestException", com.google.common.base.Throwables.getRootCause(throwable), new org.hamcrest.core.IsInstanceOf(com.artipie.docker.error.InvalidDigestException.class));
            org.hamcrest.MatcherAssert.assertThat("Exception message contains calculated digest", new org.hamcrest.core.StringContains(com.google.common.base.Throwables.getRootCause(throwable).getMessage()), "3a6eb0790f39ac87c94f3856b2dd2c5d110e6811602261a9a923d3bb23adc8b7");
            return null;
         });
    org.hamcrest.MatcherAssert.assertThat("Exception message contains expected digest", new org.hamcrest.core.StringContains(com.google.common.base.Throwables.getRootCause(throwable).getMessage()), digest);
    return java.util.concurrent.CompletableFuture.allOf();
}
```

The issue was caused by the misuse of `handle` method which expects a `Function` that transforms the result. Instead, I replaced it with `exceptionally` to handle exceptions properly.