Here's the proposed patch for the given client code:

```java
@org.junit.jupiter.api.Test
void failsOnDigestMismatch() {
    final com.artipie.asto.memory.InMemoryStorage storage = new com.artipie.asto.memory.InMemoryStorage();
    final com.artipie.docker.asto.AstoBlobs blobs = new com.artipie.docker.asto.AstoBlobs(storage, new com.artipie.docker.asto.DefaultLayout(), new com.artipie.docker.RepoName.Simple("any"));
    final java.lang.String digest = "123";
    blobs.put(new com.artipie.docker.asto.CheckedBlobSource(new com.artipie.asto.Content.From("data".getBytes()), new com.artipie.docker.Digest.Sha256(digest))).toCompletableFuture().handle(( blob, throwable) -> {
        org.hamcrest.MatcherAssert.assertThat("Exception thrown", throwable, new com.artipie.docker.asto.IsNot<>(new com.artipie.docker.asto.IsNull<>()));
        org.hamcrest.MatcherAssert.assertThat("Exception is InvalidDigestException", com.google.common.base.Throwables.getRootCause(throwable), new org.hamcrest.core.IsInstanceOf(com.artipie.docker.error.InvalidDigestException.class));
        org.hamcrest.MatcherAssert.assertThat("Exception message contains calculated digest", new org.hamcrest.core.StringContains("3a6eb0790f39ac87c94f3856b2dd2c5d110e6811602261a9a923d3bb23adc8b7"), com.google.common.base.Throwables.getRootCause(throwable).getMessage());
        org.hamcrest.MatcherAssert.assertThat("Exception message contains expected digest", new org.hamcrest.core.StringContains(digest), com.google.common.base.Throwables.getRootCause(throwable).getMessage());
        return java.util.concurrent.CompletableFuture.allOf();
    }).join();
}
```

The changes include replacing the `new org.hamcrest.core.StringContains(true, ...)` constructor calls with `new org.hamcrest.core.StringContains(...)` constructors that only take a single argument. This is because the two-argument constructor has been removed in the updated library version, causing the compilation error in the original code.