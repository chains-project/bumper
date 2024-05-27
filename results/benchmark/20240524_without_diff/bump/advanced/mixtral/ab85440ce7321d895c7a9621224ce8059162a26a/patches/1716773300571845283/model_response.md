Here's a possible patch for the provided client code. I've added a variable `throwable` in the lambda expression to fix the compilation error:
```java
@org.junit.jupiter.api.Test
void failsOnDigestMismatch() {
    final com.artipie.asto.memory.InMemoryStorage storage = new com.artipie.asto.memory.InMemoryStorage();
    final com.artipie.docker.asto.AstoBlobs blobs = new com.artipie.docker.asto.AstoBlobs(storage, new com.artipie.docker.asto.DefaultLayout(), new com.artipie.docker.RepoName.Simple("any"));
    final java.lang.String digest = "123";
    blobs.put(new com.artipie.docker.asto.CheckedBlobSource(new com.artipie.asto.Content.From("data".getBytes()), new com.artipie.docker.Digest.Sha256(digest))).toCompletableFuture().handle(( blob, throwableFromFuture) -> {
        org.hamcrest.MatcherAssert.assertThat("Exception thrown", throwableFromFuture, new com.artipie.docker.asto.IsNot<>(new com.artipie.docker.asto.IsNull<>()));
        org.hamcrest.MatcherAssert.assertThat("Exception is InvalidDigestException", com.google.common.base.Throwables.getRootCause(throwableFromFuture), new org.hamcrest.core.IsInstanceOf(com.artipie.docker.error.InvalidDigestException.class));
        org.hamcrest.MatcherAssert.assertThat("Exception message contains calculated digest", com.google.common.base.Throwables.getRootCause(throwableFromFuture).getMessage(), new org.hamcrest.core.StringStartsWith(new org.hamcrest.core.StringValue(com.artipie.docker.Digest.Sha256.NAME)));
        org.hamcrest.MatcherAssert.assertThat("Exception message contains expected digest", com.google.common.base.Throwables.getRootCause(throwableFromFuture).getMessage(), new org.hamcrest.core.StringContains(digest));
    });
    return java.util.concurrent.CompletableFuture.allOf();
}
```
This patch declares a new variable `throwableFromFuture` in the lambda expression and replaces all occurrences of `throwable` with `throwableFromFuture`. The code should now compile without issues.