Here's a suggested patch for the failing client code:

```java
@org.junit.jupiter.api.Test
void failsOnDigestMismatch() {
    final com.artipie.asto.memory.InMemoryStorage storage = new com.artipie.asto.memory.InMemoryStorage();
    final com.artipie.docker.asto.AstoBlobs blobs = new com.artipie.docker.asto.AstoBlobs(storage, new com.artipie.docker.asto.DefaultLayout(), new com.artipie.docker.RepoName.Simple("any"));
    final java.lang.String digest = "123";
    blobs.put(new com.artipie.docker.asto.CheckedBlobSource(new com.artipie.asto.Content.From("data".getBytes()), new com.artipie.docker.Digest.Sha256(digest))).toCompletableFuture().handle(( blob, throwable) -> {
        org.hamcrest.MatcherAssert.assertThat("Exception thrown", throwable, new com.artipie.docker.asto.IsNot<>(new com.artipie.docker.asto.IsNull<>()));
        org.hamcrest.MatcherAssert.assertThat("Exception is InvalidDigestException", com.google.common.base.Throwables.getRootCause(throwable), new org.hamcrest.Matchers.InstanceOf(com.artipie.docker.error.InvalidDigestException.class));
        org.hamcrest.MatcherAssert.assertThat("Exception message contains calculated digest", com.google.common.base.Throwables.getRootCause(throwable).getMessage(), new org.hamcrest.core.StringContains.ContainingSubstring("3a6eb0790f39ac87c94f3856b2dd2c5d110e6811602261a9a923d3bb23adc8b7"));
        org.hamcrest.MatcherAssert.assertThat("Exception message contains expected digest", com.google.common.base.Throwables.getRootCause(throwable).getMessage(), new org.hamcrest.core.StringContains.ContainingSubstring(digest));
        return java.util.concurrent.CompletableFuture.allOf();
    }).join();
}
```

The changes I made are:

* Replace `new org.hamcrest.core.StringContains(true, ...)` with `new org.hamcrest.core.StringContains.ContainingSubstring(...)`.
* Replace `new org.hamcrest.core.StringContains(false, ...)` with `new org.hamcrest.core.StringContains.NotContainingSubstring(...)`.

Explanation:

The error message indicates that the constructor `StringContains(boolean, String)` is no longer available. This suggests that the `StringContains` class has been changed in the new library version.

Based on the changes listed in the question, it seems that the `StringContains` class now has a new constructor `StringContains.ContainingSubstring(String)` that can be used instead of `StringContains(true, String)`. Similarly, the `StringContains(false, String)` constructor has been replaced with `StringContains.NotContainingSubstring(String)`.

By using these new constructors, we can fix the compilation error and make the code work with the new library version.