Here's a possible patch for the code that fixes the error:

```java
@org.junit.jupiter.api.Test
void failsOnDigestMismatch() {
    final com.artipie.asto.memory.InMemoryStorage storage = new com.artipie.asto.memory.InMemoryStorage();
    final com.artipie.docker.asto.AstoBlobs blobs = new com.artipie.docker.asto.AstoBlobs(storage, new com.artipie.docker.asto.DefaultLayout(), new com.artipie.docker.RepoName.Simple("any"));
    final java.lang.String digest = "123";
    blobs.put(new com.artipie.docker.asto.CheckedBlobSource(new com.artipie.asto.Content.From("data".getBytes()), new com.artipie.docker.Digest.Sha256(digest))).toCompletableFuture().handle(( blob, throwable) -> {
        org.hamcrest.MatcherAssert.assertThat("Exception thrown", throwable, new com.artipie.docker.asto.IsNot<>(new com.artipie.docker.asto.IsNull<>()));
        org.hamcrest.MatcherAssert.assertThat("Exception is InvalidDigestException", com.google.common.base.Throwables.getRootCause(throwable), new org.hamcrest.core.IsInstanceOf(com.artipie.docker.error.InvalidDigestException.class));
        org.hamcrest.MatcherAssert.assertThat("Exception message contains calculated digest", com.google.common.base.Throwables.getRootCause(throwable).getMessage(), new org.hamcrest.Matchers.StringContains.ContainsSubstring("3a6eb0790f39ac87c94f3856b2dd2c5d110e6811602261a9a923d3bb23adc8b7"));
        org.hamcrest.MatcherAssert.assertThat("Exception message contains expected digest", com.google.common.base.Throwables.getRootCause(throwable).getMessage(), new org.hamcrest.core.StringContains.StringContains(digest));
        return java.util.concurrent.CompletableFuture.allOf();
    }).join();
}
```

The changes I made are:

* Replace `new org.hamcrest.core.StringContains(true, ...)` with `new org.hamcrest.Matchers.StringContains.ContainsSubstring(...)`
* Replace `new org.hamcrest.core.StringContains<>(true, ...)` with `new org.hamcrest.core.StringContains.StringContains(...)`

The reason for these changes is that the `StringContains` constructor signature has changed in the new library version. The `StringContains` constructor now takes only one argument (the expected substring), instead of two arguments (a flag indicating whether the match should be case-insensitive, and the expected substring).

The `StringContains.ContainsSubstring` and `StringContains.StringContains` classes are new additions in the library that provide the same functionality as the old `StringContains` constructor, but with different constructor signatures. The `StringContains.ContainsSubstring` constructor takes a `String` argument (the expected substring), and the `StringContains.StringContains` constructor takes a `T` argument (the expected substring).

By using these new classes, we can make the code compatible with the new library version.