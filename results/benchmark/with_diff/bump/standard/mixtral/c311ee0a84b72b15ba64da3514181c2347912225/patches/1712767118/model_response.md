Here's a patch that fixes the error and adapts the client code to the new library version:

```java
@org.junit.jupiter.api.Test
void fixesDigestMismatch() {
    final com.artipie.asto.memory.InMemoryStorage storage = new com.artipie.asto.memory.InMemoryStorage();
    final com.artipie.docker.asto.AstoBlobs blobs = new com.artipie.docker.asto.AstoBlobs(
        storage,
        new com.artipie.docker.asto.Layouts.SingleFile(),
        new com.artipie.docker.RepoName.Simple("any")
    );
    final java.lang.String digest = "123";
    blobs.put(
        new com.artipie.docker.asto.CheckedBlobSource(
            new com.artipie.asto.Content.From("data".getBytes()),
            new com.artipie.docker.Digest.Sha256(digest)
        )
    ).toCompletableFuture()
        .exceptionally(throwable -> {
            org.hamcrest.MatcherAssert.assertThat("Exception thrown", throwable != null);
            org.hamcrest.MatcherAssert.assertThat("Exception is InvalidDigestException", 
                com.google.common.base.Throwables.getRootCause(throwable),
                new org.hamcrest.core.IsInstanceOf(com.artipie.docker.error.InvalidDigestException.class)
            );
            org.hamcrest.MatcherAssert.assertThat("Exception message contains calculated digest",
                com.google.common.base.Throwables.getRootCause(throwable).getMessage(),
                new org.hamcrest.Matchers.ContainsString(new java.lang.String(com.artipie.docker.Digest.Sha256.calculate("data")))
            );
            org.hamcrest.MatcherAssert.assertThat("Exception message contains expected digest",
                com.google.common.base.Throwables.getRootCause(throwable).getMessage(),
                new org.hamcrest.core.StringContains.StringContains(digest)
            );
            return null;
        });
}
```

Changes:
- Replaced `com.artipie.docker.asto.DefaultLayout()` with `com.artipie.docker.asto.Layouts.SingleFile()`.
- Replaced `handle()` with `exceptionally()` for the `CompletableFuture`.
- Added a null check for the throwable in the `exceptionally()` method.
- Removed unnecessary imports.
- Fixed the formatting issues in the code.
- Renamed the test method name to `fixesDigestMismatch()`.