Here's a suggested patch for the given client code, taking into account the changes in the new library version:

```java
@org.junit.jupiter.api.Test
void failsOnDigestMismatch() {
  final com.artipie.asto.memory.InMemoryStorage storage = new com.artipie.asto.memory.InMemoryStorage();
  final com.artipie.docker.asto.AstoBlobs blobs = new com.artipie.docker.asto.AstoBlobs(storage, new com.artipie.docker.asto.DefaultLayout(), new com.artipie.docker.RepoName.Simple("any"));
  final java.lang.String digest = "123";
  blobs.put(new com.artipie.docker.asto.CheckedBlobSource(new com.artipie.asto.Content.From("data".getBytes()), new com.artipie.docker.Digest.Sha256(digest)))
    .toCompletableFuture()
    .handle(
      (blob, throwable) -> {
        org.hamcrest.MatcherAssert.assertThat("Exception thrown", throwable, new org.hamcrest.core.IsInstanceOf(com.artipie.docker.asto.IsNot.class));
        org.hamcrest.MatcherAssert.assertThat("Exception is InvalidDigestException", com.google.common.base.Throwables.getRootCause(throwable), new org.hamcrest.core.IsInstanceOf(com.artipie.docker.error.InvalidDigestException.class));
        org.hamcrest.MatcherAssert.assertThat("Exception message contains calculated digest", new org.hamcrest.core.StringContains().containsString(
          com.google.common.base.Throwables.getRootCause(throwable).getMessage(),
          "3a6eb0790f39ac87c94f3856b2dd2c5d110e6811602261a9a923d3bb23adc8b7"
        ));
        return null;
      }
    );
  org.hamcrest.MatcherAssert.assertThat("Exception message contains expected digest", new org.hamcrest.core.StringContains().containsString(
    com.google.common.base.Throwables.getRootCause(throwable).getMessage(),
    digest
  ));
  return java.util.concurrent.CompletableFuture.allOf();
}
```

The changes made include:

- Fixing the ';' expected error by removing the semicolon after `new org.hamcrest.core.StringContains().containsString(...)`
- Replacing `new com.artipie.docker.asto.IsNot<>(new com.artipie.docker.asto.IsNull<>())` with `new org.hamcrest.core.IsInstanceOf(com.artipie.docker.asto.IsNot.class)` as the first matcher in the handle method.
- Replacing the `return` statement in the handle method with `return null;` since it is not required in this case.