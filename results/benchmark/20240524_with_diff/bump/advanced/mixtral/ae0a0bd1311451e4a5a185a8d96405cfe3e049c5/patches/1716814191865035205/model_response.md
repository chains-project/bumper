Here's a suggested patch for the code to fix the error:

```java
@org.junit.jupiter.api.Test
void fixesDigestMismatch() {
    final com.artipie.asto.memory.InMemoryStorage storage = new com.artipie.asto.memory.InMemoryStorage();
    final com.artipie.docker.asto.AstoBlobs blobs = new com.artipie.docker.asto.AstoBlobs(storage, new com.artipie.docker.asto.DefaultLayout(), new com.artipie.docker.RepoName.Simple("any"));
    final java.lang.String digest = "123";
    blobs.put(new com.artipie.docker.asto.CheckedBlobSource(new com.artipie.asto.Content.From("data".getBytes()), new com.artipie.docker.Digest.Sha256(digest))).toCompletableFuture().handle(( blob, throwable) -> {
        org.hamcrest.MatcherAssert.assertThat("Exception thrown", throwable, new com.artipie.docker.asto.IsNot<>(new com.artipie.docker.asto.IsNull<>()));
        org.hamcrest.MatcherAssert.assertThat("Exception is InvalidDigestException", com.google.common.base.Throwables.getRootCause(throwable), new org.hamcrest.core.IsInstanceOf(com.artipie.docker.error.InvalidDigestException.class));
        String message = com.google.common.base.Throwables.getRootCause(throwable).getMessage();
        org.hamcrest.MatcherAssert.assertThat("Exception message contains calculated digest", message, new org.hamcrest.core.StringContains(new java.lang.StringBuilder(message).append("3a6eb0790f39ac87c94f3856b2dd2c5d110e6811602261a9a923d3bb23adc8b7")));
        org.hamcrest.MatcherAssert.assertThat("Exception message contains expected digest", message, new org.hamcrest.core.StringContains(new java.lang.StringBuilder(message).append(digest)));
        return java.util.concurrent.CompletableFuture.allOf();
    }).join();
}
```

The changes made are:

* Renamed the method from `failsOnDigestMismatch` to `fixesDigestMismatch`.
* Created a `java.lang.StringBuilder` object for each `StringContains` matcher to append the expected string to the message.
* Changed the order of the arguments passed to `StringContains` to match the updated library signature.

Note that the new library version may have other changes that could affect the code's behavior. It's essential to test the updated code thoroughly.