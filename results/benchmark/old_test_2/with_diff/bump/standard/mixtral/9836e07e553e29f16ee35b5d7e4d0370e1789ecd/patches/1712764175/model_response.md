Here's a suggested patch for the given client code to fix the error:

```java
@org.junit.jupiter.api.Test
void failsOnDigestMismatch() {
    final com.artipie.asto.memory.InMemoryStorage storage = new com.artipie.asto.memory.InMemoryStorage();
    final com.artipie.docker.asto.AstoBlobs blobs = new com.artipie.docker.asto.AstoBlobs(storage, new com.artipie.docker.asto.DefaultLayout(), new com.artipie.docker.RepoName.Simple("any"));
    final java.lang.String digest = "123";
    blobs.put(new com.artipie.docker.asto.CheckedBlobSource(new com.artipie.asto.Content.From("data".getBytes()), new com.artipie.docker.Digest.Sha256(digest))).toCompletableFuture().handle(( blob, throwable) -> {
        org.hamcrest.MatcherAssert.assertThat("Exception thrown", throwable, new com.artipie.docker.asto.IsNot<>(new com.artipie.docker.asto.IsNull<>()));
        org.hamcrest.MatcherAssert.assertThat("Exception is InvalidDigestException", com.google.common.base.Throwables.getRootCause(throwable), new org.hamcrest.core.IsInstanceOf(com.artipie.docker.error.InvalidDigestException.class));
        org.hamcrest.MatcherAssert.assertThat("Exception message contains calculated digest", com.google.common.base.Throwables.getRootCause(throwable).getMessage(), new org.hamcrest.MatcherAssert.MatchesPattern(new java.util.regex.Pattern(".*3a6eb0790f39ac87c94f3856b2dd2c5d110e6811602261a9a923d3bb23adc8b7.*")));
        org.hamcrest.MatcherAssert.assertThat("Exception message contains expected digest", com.google.common.base.Throwables.getRootCause(throwable).getMessage(), new org.hamcrest.core.StringContains.ContainsString(digest));
        return java.util.concurrent.CompletableFuture.allOf();
    }).join();
}
```

The changes made are:

* Replaced `new org.hamcrest.core.StringContains(true, "3a6eb0790f39ac87c94f3856b2dd2c5d110e6811602261a9a923d3bb23adc8b7")` with `new org.hamcrest.MatcherAssert.MatchesPattern(new java.util.regex.Pattern(".*3a6eb0790f39ac87c94f3856b2dd2c5d110e6811602261a9a923d3bb23adc8b7.*"))`.
* Replaced `new org.hamcrest.core.StringContains(true, digest)` with `new org.hamcrest.core.StringContains.ContainsString(digest)`.

This patch fixes the error by using the `MatchesPattern` matcher instead of `StringContains` matcher for the calculated digest, and using the `ContainsString` matcher instead of `StringContains` matcher for the expected digest. This aligns with the changes made in the new library version.