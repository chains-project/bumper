Here's a suggested patch for the code to fix the error:

```java
@org.junit.jupiter.api.Test
void failsOnDigestMismatch() {
    final com.artipie.asto.memory.InMemoryStorage storage = new com.artipie.asto.memory.InMemoryStorage();
    final com.artipie.docker.asto.AstoBlobs blobs = new com.artipie.docker.asto.AstoBlobs(storage, new com.artipie.docker.asto.DefaultLayout(), new com.artipie.docker.RepoName.Simple("any"));
    final java.lang.String digest = "123";
    blobs.put(new com.artipie.docker.asto.CheckedBlobSource(new com.artipie.asto.Content.From("data".getBytes()), new com.artipie.docker.Digest.Sha256(digest))).toCompletableFuture().handle(( blob, throwable) -> {
        org.hamcrest.MatcherAssert.assertThat("Exception thrown", throwable, new com.artipie.docker.asto.IsNot<>(new com.artipie.docker.asto.IsNull<>()));
        org.hamcrest.MatcherAssert.assertThat("Exception is InvalidDigestException", com.google.common.base.Throwables.getRootCause(throwable), new org.hamcrest.MatcherAssert.MatchesPattern(com.artipie.docker.error.InvalidDigestException.class.getName() + ": .*"));
        org.hamcrest.MatcherAssert.assertThat("Exception message contains calculated digest", com.google.common.base.Throwables.getRootCause(throwable).getMessage(), new org.hamcrest.core.StringContains.Containing("3a6eb0790f39ac87c94f3856b2dd2c5d110e6811602261a9a923d3bb23adc8b7"));
        org.hamcrest.MatcherAssert.assertThat("Exception message contains expected digest", com.google.common.base.Throwables.getRootCause(throwable).getMessage(), new org.hamcrest.core.StringContains.Containing(digest));
        return java.util.concurrent.CompletableFuture.allOf();
    }).join();
}
```

The changes made are:

* Replaced `new org.hamcrest.core.StringContains(true, "3a6eb0790f39ac87c94f3856b2dd2c5d110e6811602261a9a923d3bb23adc8b7")` with `new org.hamcrest.core.StringContains.Containing("3a6eb0790f39ac87c94f3856b2dd2c5d110e6811602261a9a923d3bb23adc8b7")`.
* Replaced `new org.hamcrest.core.StringContains(true, digest)` with `new org.hamcrest.core.StringContains.Containing(digest)`.
* Replaced `new org.hamcrest.core.IsInstanceOf(com.artipie.docker.error.InvalidDigestException.class)` with `new org.hamcrest.MatcherAssert.MatchesPattern(com.artipie.docker.error.InvalidDigestException.class.getName() + ": .*")`.

Note that the `StringContains` constructor has been changed in the new library version to require only one argument (the expected substring), instead of two (a boolean flag and the expected substring). The `IsInstanceOf` matcher has been replaced with a `MatchesPattern` matcher that checks if the exception message matches a regular expression pattern.