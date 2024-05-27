Here's a patch that you can apply to fix the error:

```java
@org.junit.jupiter.api.Test
void fixesDigestMismatch() {
    final com.artipie.asto.memory.InMemoryStorage storage = new com.artipie.asto.memory.InMemoryStorage();
    final com.artipie.docker.asto.AstoBlobs blobs = new com.artipie.docker.asto.AstoBlobs(storage, new com.artipie.docker.asto.DefaultLayout(), new com.artipie.docker.RepoName.Simple("any"));
    final java.lang.String digest = "123";
    blobs.put(new com.artipie.docker.asto.CheckedBlobSource(new com.artipie.asto.Content.From("data".getBytes()), new com.artipie.docker.Digest.Sha256(digest))).toCompletableFuture().handle(( blob, throwable) -> {
        org.hamcrest.MatcherAssert.assertThat("Exception thrown", throwable, new com.artipie.docker.asto.IsNot<>(new com.artipie.docker.asto.IsNull<>()));
        org.hamcrest.MatcherAssert.assertThat("Exception is InvalidDigestException", com.google.common.base.Throwables.getRootCause(throwable), new org.hamcrest.core.IsInstanceOf(com.artipie.docker.error.InvalidDigestException.class));
        org.hamcrest.MatcherAssert.assertThat("Exception message contains calculated digest", com.google.common.base.Throwables.getRootCause(throwable).getMessage(), new org.hamcrest.core.StringStartsWith(new java.lang.String("3a6eb0790f39ac87c94f3856b2dd2c5d110e6811602261a9a923d3bb23adc8b7")));
        org.hamcrest.MatcherAssert.assertThat("Exception message contains expected digest", com.google.common.base.Throwables.getRootCause(throwable).getMessage(), new org.hamcrest.core.StringContains(digest));
        return java.util.concurrent.CompletableFuture.allOf();
    }).join();
}
```

The changes I made are as follows:

1. Renamed the method from `failsOnDigestMismatch` to `fixesDigestMismatch` to reflect the fact that the error has been fixed.
2. Replaced the `org.hamcrest.core.StringContains` matcher with `org.hamcrest.core.StringStartsWith` for the calculated digest. This is because the `StringContains` matcher expects a single string argument, whereas it was being passed two arguments in the original code.

Note that the `StringStartsWith` matcher checks if the given string starts with the expected substring. If you want to check if the given string contains the expected substring, you can use the `StringContains` matcher with a single argument.