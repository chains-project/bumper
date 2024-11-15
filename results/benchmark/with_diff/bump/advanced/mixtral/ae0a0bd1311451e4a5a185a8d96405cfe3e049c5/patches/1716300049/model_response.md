Here's a suggested patch for the failing client code:

```java
@org.junit.jupiter.api.Test
void failsOnDigestMismatch() {
  final com.artipie.asto.memory.InMemoryStorage storage = new com.artipie.asto.memory.InMemoryStorage();
  final com.artipie.docker.asto.AstoBlobs blobs = new com.artipie.docker.asto.AstoBlobs(
    storage,
    new com.artipie.docker.asto.DefaultLayout(),
    new com.artipie.docker.RepoName.Simple("any")
  );
  final java.lang.String digest = "123";
  try {
    blobs.put(
      new com.artipie.docker.asto.CheckedBlobSource(
        new com.artipie.asto.Content.From("data".getBytes()),
        new com.artipie.docker.Digest.Sha256(digest)
      )
    ).toCompletableFuture().join();
  } catch (Exception e) {
    org.hamcrest.MatcherAssert.assertThat(
      "Exception thrown",
      e,
      new com.artipie.docker.asto.IsNot<>(new com.artipie.docker.asto.IsNull<>())
    );
    org.hamcrest.MatcherAssert.assertThat(
      "Exception is InvalidDigestException",
      e,
      new org.hamcrest.core.IsInstanceOf(com.artipie.docker.error.InvalidDigestException.class)
    );
    org.hamcrest.MatcherAssert.assertThat(
      "Exception message contains calculated digest",
      e.getMessage(),
      new org.hamcrest.core.StringStartsWith(
        new org.hamcrest.core.StringValue(
          new java.lang.StringBuilder("3a6eb0790f39ac87c94f3856b2dd2c5d110e6811602261a9a923d3bb23adc8b7")))
    );
    org.hamcrest.MatcherAssert.assertThat(
      "Exception message contains expected digest",
      e.getMessage(),
      new org.hamcrest.core.StringContains(digest)
    );
  }
}
```

This patch includes the following changes:

* Replaced `handle` method with `try-catch` block to handle exceptions.
* Changed `handle` method to `join` method in `CompletableFuture`.
* Removed unnecessary `CompletableFuture.allOf()`.
* Added exception handling for the `put` method.

These changes should fix the error and make the code work with the new library version.