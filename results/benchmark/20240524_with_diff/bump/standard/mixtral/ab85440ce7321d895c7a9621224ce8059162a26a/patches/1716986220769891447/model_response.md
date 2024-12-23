Here's a suggested patch for the failing client code:

```java
@org.junit.jupiter.api.Test
void failsOnDigestMismatch() {
    final com.artipie.asto.memory.InMemoryStorage storage = new com.artipie.asto.memory.InMemoryStorage();
    final com.artipie.docker.asto.AstoBlobs blobs = new com.artipie.docker.asto.AstoBlobs(storage, new com.artipie.docker.asto.DefaultLayout(), new com.artipie.docker.RepoName.Simple("any"));
    final java.lang.String digest = "123";
    blobs.put(new com.artipie.docker.asto.CheckedBlobSource(new com.artipie.asto.Content.From("data".getBytes()), new com.artipie.docker.Digest.Sha256(digest))).toCompletableFuture().handle(( blob, throwable) -> {
        org.hamcrest.MatcherAssert.assertThat("Exception thrown", throwable, new com.artipie.docker.asto.IsNot<>(new com.artipie.docker.asto.IsNull<>()));
        org.hamcrest.MatcherAssert.assertThat("Exception is InvalidDigestException", com.google.common.base.Throwables.getRootCause(throwable), new org.hamcrest.MatcherAssert.MatchesPattern(new org.hamcrest.pattern.MatchesPattern.CompoundMatcher(".*InvalidDigestException: calculated digest does not match provided.*3a6eb0790f39ac87c94f3856b2dd2c5d110e6811602261a9a923d3bb23adc8b7.*", ".*InvalidDigestException: calculated digest does not match provided.*" + digest + ".*")));
        return java.util.concurrent.CompletableFuture.allOf();
    }).join();
}
```

In this patch, I replaced the `StringContains` matcher with a `MatchesPattern` matcher, which allows for more complex matching patterns. The pattern used checks that the exception message contains both the calculated digest and the expected digest, while still allowing for some variability in the message text.