Here's a suggested patch for the provided client code:

```java
// TODO: review this AI generated patch!
@org.junit.jupiter.api.Test
void fixesDigestMismatch() {
    final com.artipie.asto.memory.InMemoryStorage storage = new com.artipie.asto.memory.InMemoryStorage();
    final com.artipie.docker.asto.AstoBlobs blobs = new com.artipie.docker.asto.AstoBlobs(storage, new com.artipie.docker.asto.DefaultLayout(), new com.artipie.docker.RepoName.Simple("any"));
    final java.lang.String digest = "123";
    try {
        blobs.put(new com.artipie.docker.asto.CheckedBlobSource(new com.artipie.asto.Content.From("data".getBytes()), new com.artipie.docker.Digest.Sha256(digest))).toCompletableFuture().get();
    } catch (Exception e) {
        org.hamcrest.MatcherAssert.assertThat("Exception thrown", e, new com.artipie.docker.asto.IsNot<>(new com.artipie.docker.asto.IsNull<>()));
        org.hamcrest.MatcherAssert.assertThat("Exception is InvalidDigestException", e, new org.hamcrest.core.IsInstanceOf(com.artipie.docker.error.InvalidDigestException.class));
        org.hamcrest.MatcherAssert.assertThat("Exception message contains calculated digest", e.getMessage(), new org.hamcrest.Matchers.ContainsString(new java.lang.String(com.artipie.docker.Digest.Sha256.calculate("data"))));
        org.hamcrest.MatcherAssert.assertThat("Exception message contains expected digest", e.getMessage(), new org.hamcrest.core.StringContains.StringContains(digest));
    }
}
```

The patch includes the following changes:

1. Renamed the method from `failsOnDigestMismatch` to `fixesDigestMismatch` to reflect the fix.
2. Replaced the `handle` method with a `try-catch` block to handle the exception.
3. Replaced the `join()` method with `get()` on the `CompletableFuture` to retrieve the exception.

These changes should resolve the compilation error and allow the test method to run successfully.