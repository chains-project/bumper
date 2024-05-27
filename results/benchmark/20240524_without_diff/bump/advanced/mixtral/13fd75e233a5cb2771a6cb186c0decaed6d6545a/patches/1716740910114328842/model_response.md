Here's a patch that fixes the error by using `org.hamcrest.core.StringContains.containsString(String)` instead of `org.hamcrest.core.StringContains(boolean, String)`:

```java
@org.junit.jupiter.api.Test
void failsOnDigestMismatch() {
    final com.artipie.asto.memory.InMemoryStorage storage = new com.artipie.asto.memory.InMemoryStorage();
    final com.artipie.docker.asto.AstoBlobs blobs = new com.artipie.docker.asto.AstoBlobs(storage, new com.artipie.docker.asto.DefaultLayout(), new com.artipie.docker.RepoName.Simple("any"));
    final java.lang.String digest = "123";
    blobs.put(new com.artipie.docker.asto.CheckedBlobSource(new com.artipie.asto.Content.From("data".getBytes()), new com.artipie.docker.asto.Digest.Sha256(digest))).toCompletableFuture().handle(( blob, throwable) -> {
        org.hamcrest.MatcherAssert.assertThat("Exception thrown", throwable, new com.artipie.docker.asto.IsNot<>(new com.artipie.docker.asto.IsNull<>()));
        org.hamcrest.MatcherAssert.assertThat("Exception is InvalidDigestException", com.google.common.base.Throwables.getRootCause(throwable), new org.hamcrest.core.IsInstanceOf(com.artipie.docker.error.InvalidDigestException.class));
        org.hamcrest.MatcherAssert.assertThat("Exception message contains calculated digest", org.hamcrest.core.StringContains.containsString(com.google.common.base.Throwables.getRootCause(throwable).getMessage()), new org.hamcrest.core.StringContains(true, "3a6eb0790f39ac87c94f3856b2dd2c5d110e6811602261a9a923d3bb23adc8b7"));
        org.hamcrest.MatcherAssert.assertThat("Exception message contains expected digest", org.hamcrest.core.StringContains.containsString(com.google.common.base.Throwables.getRootCause(throwable).getMessage()), new org.hamcrest.core.StringContains(true, digest));
        return java.util.concurrent.CompletableFuture.allOf();
    }).join();
}
```

The error was caused by passing two arguments to `org.hamcrest.core.StringContains` constructor, while it only takes one argument. I replaced it with `org.hamcrest.core.StringContains.containsString(String)` which takes a single argument.