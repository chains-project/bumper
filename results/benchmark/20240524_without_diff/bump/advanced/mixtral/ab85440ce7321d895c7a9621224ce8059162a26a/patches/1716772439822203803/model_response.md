Here is the proposed patch:

```java
@org.junit.jupiter.api.Test
void failsOnDigestMismatch() {
    final com.artipie.asto.memory.InMemoryStorage storage = new com.artipie.asto.memory.InMemoryStorage();
    final com.artipie.docker.asto.AstoBlobs blobs = new com.artipie.docker.asto.AstoBlobs(storage, new com.artipie.docker.asto.DefaultLayout(), new com.artipie.docker.RepoName.Simple("any"));
    final java.lang.String digest = "123";
    blobs.put(new com.artipie.docker.asto.CheckedBlobSource(new com.artipie.asto.Content.From("data".getBytes()), new com.artipie.docker.Digest.Sha256(digest))).toCompletableFuture().handle(( blob, throwable) -> {
        org.hamcrest.MatcherAssert.assertThat("Exception thrown", throwable, new com.artipie.docker.asto.IsNot<>(new com.artipie.docker.asto.IsNull<>()));
        org.hamcrest.MatcherAssert.assertThat("Exception is InvalidDigestException", com.google.common.base.Throwables.getRootCause(throwable), new org.hamcrest.core.IsInstanceOf(com.artipie.docker.error.InvalidDigestException.class));
        String message = com.google.common.base.Throwables.getRootCause(throwable).getMessage();
        org.hamcrest.MatcherAssert.assertThat("Exception message contains calculated digest", message, new org.hamcrest.core.StringContains(new org.hamcrest.core.StringStartsWith("3a6eb0790f39ac87c94f3856b2dd2c5d110e6811602261a9a923d3bb23adc8b7")));
        org.hamcrest.MatcherAssert.assertThat("Exception message contains expected digest", message, new org.hamcrest.core.StringContains(digest));
        return java.util.concurrent.CompletableFuture.allOf();
    }).join();
}
```

The issue is caused by the fact that the `StringContains` constructor expects a single argument, but was being passed two arguments. I have changed the code to use the `StringStartsWith` matcher instead of `StringContains` for the calculated digest, and removed the second argument to `StringContains` for the expected digest. Additionally, I have stored the exception message in a variable to avoid calling `com.google.common.base.Throwables.getRootCause(throwable).getMessage()` twice.