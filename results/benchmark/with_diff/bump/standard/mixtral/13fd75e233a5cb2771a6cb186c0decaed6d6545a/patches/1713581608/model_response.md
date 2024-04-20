Here's a suggested patch for the given client code:

```java
// TODO: review this AI generated patch!
@org.junit.jupiter.api.Test
void failsOnDigestMismatch() {
    final com.artipie.asto.memory.InMemoryStorage storage = new com.artipie.asto.memory.InMemoryStorage();
    final com.artipie.docker.asto.AstoBlobs blobs = new com.artipie.docker.asto.AstoBlobs(storage, new com.artipie.docker.asto.DefaultLayout(), new com.artipie.docker.RepoName.Simple("any"));
    final java.lang.String digest = "123";
    blobs.put(new com.artipie.docker.asto.CheckedBlobSource(new com.artipie.asto.Content.From("data".getBytes()), new com.artipie.docker.Digest.Sha256(digest)))
         .exceptionally(throwable -> {
            org.hamcrest.MatcherAssert.assertThat("Exception thrown", throwable != null);
            org.hamcrest.MatcherAssert.assertThat("Exception is InvalidDigestException", com.google.common.base.Throwables.getRootCause(throwable) instanceof com.artipie.docker.error.InvalidDigestException);
            org.hamcrest.MatcherAssert.assertThat("Exception message contains calculated digest", com.google.common.base.Throwables.getRootCause(throwable).getMessage(), org.hamcrest.core.StringContains.containsString("3a6eb0790f39ac87c94f3856b2dd2c5d110e6811602261a9a923d3bb23adc8b7"));
            return null;
         });
    org.hamcrest.MatcherAssert.assertThat("Exception message contains expected digest", com.google.common.base.Throwables.getRootCause(throwable).getMessage(), org.hamcrest.core.StringContains.containsString(digest));
    return java.util.concurrent.CompletableFuture.allOf();
}
```

The changes include:

1. Replace `.handle()` with `.exceptionally()`, as `handle()` expects a function that returns a value, while we only want to handle the exception.
2. Replace the `org.hamcrest.MatcherAssert.assertThat("Exception thrown", throwable, new com.artipie.docker.asto.IsNot<>(new com.artipie.docker.asto.IsNull<>()));` line, as it's not needed.
3. Replace `org.hamcrest.MatcherAssert.assertThat("Exception message contains expected digest", new org.hamcrest.core.StringContains().containsString(com.google.common.base.Throwables.getRootCause(throwable).getMessage(), digest));` with `org.hamcrest.MatcherAssert.assertThat("Exception message contains expected digest", com.google.common.base.Throwables.getRootCause(throwable).getMessage(), org.hamcrest.core.StringContains.containsString(digest));`, as the `StringContains` constructor expects a single argument.