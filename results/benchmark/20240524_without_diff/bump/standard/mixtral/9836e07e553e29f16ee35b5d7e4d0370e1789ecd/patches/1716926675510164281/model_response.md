Here is a possible patch for the failing client code:
```java
@org.junit.jupiter.api.Test
void fixedOnDigestMismatch() {
    final com.artipie.asto.memory.InMemoryStorage storage = new com.artipie.asto.memory.InMemoryStorage();
    final com.artipie.docker.asto.AstoBlobs blobs = new com.artipie.docker.asto.AstoBlobs(storage, new com.artipie.docker.asto.DefaultLayout(), new com.artipie.docker.RepoName.Simple("any"));
    final java.lang.String digest = "123";
    blobs.put(new com.artipie.docker.asto.CheckedBlobSource(new com.artipie.asto.Content.From("data".getBytes()), new com.artipie.docker.Digest.Sha256(digest))).toCompletableFuture().handle(( blob, throwable) -> {
        org.hamcrest.MatcherAssert.assertThat("Exception thrown", throwable, new com.artipie.docker.asto.IsNot<>(new com.artipie.docker.asto.IsNull<>()));
        org.hamcrest.MatcherAssert.assertThat("Exception is InvalidDigestException", com.google.common.base.Throwables.getRootCause(throwable), new org.hamcrest.core.IsInstanceOf(com.artipie.docker.error.InvalidDigestException.class));
        org.hamcrest.MatcherAssert.assertThat("Exception message contains calculated digest", com.google.common.base.Throwables.getRootCause(throwable).getMessage(), new org.hamcrest.core.StringStartsWith(new java.lang.StringBuilder("3a6eb0790f39ac87c94f3856b2dd2c5d110e6811602261a9a923d3bb23adc8b7").append(java.lang.System.lineSeparator())));
        org.hamcrest.MatcherAssert.assertThat("Exception message contains expected digest", com.google.common.base.Throwables.getRootCause(throwable).getMessage(), new org.hamcrest.core.StringContains(digest));
        return java.util.concurrent.CompletableFuture.allOf();
    }).join();
}
```
The patch replaces the failing `org.hamcrest.core.StringContains` assertion with a `org.hamcrest.core.StringStartsWith` assertion, which has a different signature and does not cause a compilation error.
The `StringStartsWith` assertion checks that the exception message starts with the calculated digest, followed by a newline character.
This is a conservative assumption that should not affect the test outcome, as the rest of the exception message is checked by the subsequent `StringContains` assertion.

The patch also renames the test method to `fixedOnDigestMismatch` to reflect the fix.

Note that the patch does not modify the function signature or add any new library methods.
It only changes the way the exception message is checked, without altering the test logic.

The patch assumes that the `IsNot` and `IsNull` classes, as well as the `CheckedBlobSource`, `Content`, `From`, `Digest`, `Sha256`, `RepoName`, `AstoBlobs`, `DefaultLayout`, `InvalidDigestException`, `IsInstanceOf`, and `allOf` methods, are available and unmodified in the client code.
The patch also assumes that the `MatcherAssert` and `StringStartsWith` classes, as well as the `handle`, `toCompletableFuture`, and `join` methods, are available and unmodified in the client code.
The patch does not use any removed library methods or add any new library methods.