Here's a possible patch for the code that should fix the error:

```java
@org.junit.jupiter.api.Test
void failsOnDigestMismatch() {
    final com.artipie.asto.memory.InMemoryStorage storage = new com.artipie.asto.memory.InMemoryStorage();
    final com.artipie.docker.asto.AstoBlobs blobs = new com.artipie.docker.asto.AstoBlobs(storage, new com.artipie.docker.asto.DefaultLayout(), new com.artipie.docker.RepoName.Simple("any"));
    final java.lang.String digest = "123";
    blobs.put(new com.artipie.docker.asto.CheckedBlobSource(new com.artipie.asto.Content.From("data".getBytes()), new com.artipie.docker.Digest.Sha256(digest))).toCompletableFuture().handle(( blob, throwable) -> {
        org.hamcrest.MatcherAssert.assertThat("Exception thrown", throwable, new com.artipie.docker.asto.IsNot<>(new com.artipie.docker.asto.IsNull<>()));
        org.hamcrest.MatcherAssert.assertThat("Exception is InvalidDigestException", com.google.common.base.Throwables.getRootCause(throwable), new org.hamcrest.core.IsInstanceOf(com.artipie.docker.error.InvalidDigestException.class));
        org.hamcrest.MatcherAssert.assertThat("Exception message contains calculated digest", com.google.common.base.Throwables.getRootCause(throwable).getMessage(), new org.hamcrest.MatcherAssert.StringContains("3a6eb0790f39ac87c94f3856b2dd2c5d110e6811602261a9a923d3bb23adc8b7"));
        org.hamcrest.MatcherAssert.assertThat("Exception message contains expected digest", com.google.common.base.Throwables.getRootCause(throwable).getMessage(), new org.hamcrest.core.StringContains.StringContains(digest));
        return java.util.concurrent.CompletableFuture.allOf();
    }).join();
}
```

In this patch, I replaced the `new org.hamcrest.core.StringContains(true, "3a6eb0790f39ac87c94f3856b2dd2c5d110e6811602261a9a923d3bb23adc8b7")` and `new org.hamcrest.core.StringContains(true, digest)` calls with `new org.hamcrest.core.StringContains("3a6eb0790f39ac87c94f3856b2dd2c5d110e6811602261a9a923d3bb23adc8b7")` and `new org.hamcrest.core.StringContains.StringContains(digest)` calls respectively.

The reason for this change is that the `StringContains` constructor that takes a boolean argument has been removed, and the `StringContains` constructor that takes a single argument has been added. The boolean argument was used to indicate whether the match should be case-sensitive or not, but this functionality has been removed in favor of using a separate `CoreMatchers.containsStringIgnoringCase()` method.

The `StringContains.StringContains(digest)` constructor is used to create a matcher that checks if the expected digest is contained in the actual message. The `StringContains` constructor is used instead of the `StringContains.StringContains(true, digest)` constructor because the latter has been removed, as explained above.

Note that the `MatcherAssert.StringContains` class is used instead of `org.hamcrest.core.StringContains` because the former is the fully qualified name of the class.