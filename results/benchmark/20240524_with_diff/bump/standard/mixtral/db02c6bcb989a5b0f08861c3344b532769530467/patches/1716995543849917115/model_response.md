Here is the proposed patch for the failing client code:
```java
@org.junit.jupiter.api.Test
void failsOnDigestMismatch() {
    final com.artipie.asto.memory.InMemoryStorage storage = new com.artipie.asto.memory.InMemoryStorage();
    final com.artipie.docker.asto.AstoBlobs blobs = new com.artipie.docker.asto.AstoBlobs(storage, new com.artipie.docker.asto.DefaultLayout(), new com.artipie.docker.RepoName.Simple("any"));
    final java.lang.String digest = "123";
    blobs.put(new com.artipie.docker.asto.CheckedBlobSource(new com.artipie.asto.Content.From("data".getBytes()), new com.artipie.docker.Digest.Sha256(digest))).toCompletableFuture().handle(( blob, throwable) -> {
        org.hamcrest.MatcherAssert.assertThat("Exception thrown", throwable, new com.artipie.docker.asto.IsNot<>(new com.artipie.docker.asto.IsNull<>()));
        org.hamcrest.MatcherAssert.assertThat("Exception is InvalidDigestException", com.google.common.base.Throwables.getRootCause(throwable), new org.hamcrest.core.IsInstanceOf(com.artipie.docker.error.InvalidDigestException.class));
        org.hamcrest.MatcherAssert.assertThat("Exception message contains calculated digest", com.google.common.base.Throwables.getRootCause(throwable).getMessage(), new org.hamcrest.core.StringStartsWith(com.artipie.docker.Digest.Sha256.NAME + ":"));
        org.hamcrest.MatcherAssert.assertThat("Exception message contains expected digest", com.google.common.base.Throwables.getRootCause(throwable).getMessage(), new org.hamcrest.core.StringContains(digest));
        return java.util.concurrent.CompletableFuture.allOf();
    }).join();
}
```
The changes made to the code are:

1. Replace the `org.hamcrest.core.StringContains` matcher with `org.hamcrest.core.StringStartsWith` for the calculated digest check. This is because the `StringContains` constructor that takes a `boolean` argument has been removed in the new library version.
2. Keep the `org.hamcrest.core.StringContains` matcher for the expected digest check. This is because the `StringStartsWith` matcher does not provide a way to check if the expected string is contained within the actual string.

The `org.hamcrest.core.IsInstanceOf` matcher is not affected by the library changes and can be reused as is.

Note that this patch assumes that the calculated digest starts with the digest algorithm name, as is the case for the `com.artipie.docker.Digest.Sha256` class. If this is not the case for other digest algorithms, the `StringStartsWith` matcher may need to be adjusted accordingly.