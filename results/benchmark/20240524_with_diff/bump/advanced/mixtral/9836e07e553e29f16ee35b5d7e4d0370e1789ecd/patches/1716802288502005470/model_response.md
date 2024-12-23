Here's a possible patch for the failing method. I added a new variable `message` to store the exception message and used the `StringContains` matcher with only one argument:

```java
@org.junit.jupiter.api.Test
void failsOnDigestMismatch() {
    final com.artipie.asto.memory.InMemoryStorage storage = new com.artipie.asto.memory.InMemoryStorage();
    final com.artipie.docker.asto.AstoBlobs blobs = new com.artipie.docker.asto.AstoBlobs(storage, new com.artipie.docker.asto.DefaultLayout(), new com.artipie.docker.RepoName.Simple("any"));
    final java.lang.String digest = "123";
    blobs.put(new com.artipie.docker.asto.CheckedBlobSource(new com.artipie.asto.Content.From("data".getBytes()), new com.artipie.docker.asto.Digest.Sha256(digest))).toCompletableFuture().handle(( blob, throwable) -> {
        org.hamcrest.MatcherAssert.assertThat("Exception thrown", throwable, new com.artipie.docker.asto.IsNot<>(new com.artipie.docker.asto.IsNull<>()));
        if (throwable != null) {
            java.lang.String message = throwable.getMessage();
            org.hamcrest.MatcherAssert.assertThat("Exception is InvalidDigestException", throwable, new org.hamcrest.core.IsInstanceOf(com.artipie.docker.error.InvalidDigestException.class));
            org.hamcrest.MatcherAssert.assertThat("Exception message contains calculated digest", message, new org.hamcrest.core.StringContains.StringContains(new java.lang.String[]{"3a6eb0790f39ac87c94f3856b2dd2c5d110e6811602261a9a923d3bb23adc8b7"}));
            org.hamcrest.MatcherAssert.assertThat("Exception message contains expected digest", message, new org.hamcrest.core.StringContains.StringContains(new java.lang.String[]{digest}));
        }
        return java.util.concurrent.CompletableFuture.allOf();
    }).join();
}
```

This patch should resolve the compilation error by using the `StringContains` constructor with a single argument.