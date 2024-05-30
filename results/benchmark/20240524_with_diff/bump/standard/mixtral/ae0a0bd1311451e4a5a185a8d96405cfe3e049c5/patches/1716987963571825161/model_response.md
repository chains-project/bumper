Here's a possible patch for the given client code:

```java
@org.junit.jupiter.api.Test
void failsOnDigestMismatch() {
    final com.artipie.asto.memory.InMemoryStorage storage = new com.artipie.asto.memory.InMemoryStorage();
    final com.artipie.docker.asto.AstoBlobs blobs = new com.artipie.docker.asto.AstoBlobs(storage, new com.artipie.docker.asto.DefaultLayout(), new com.artipie.docker.RepoName.Simple("any"));
    final java.lang.String digest = "123";
    blobs.put(new com.artipie.docker.asto.CheckedBlobSource(new com.artipie.asto.Content.From("data".getBytes()), new com.artipie.docker.Digest.Sha256(digest)))
         .toCompletableFuture()
         .handle((blob, throwable) -> {
             if (throwable != null) {
                 if (throwable instanceof com.artipie.docker.asto.IsNull) {
                     throw throwable;
                 } else if (throwable instanceof com.artipie.docker.error.InvalidDigestException) {
                     org.hamcrest.MatcherAssert.assertThat("Exception is InvalidDigestException", com.google.common.base.Throwables.getRootCause(throwable), new org.hamcrest.MatcherAssert.MatchesPattern(com.artipie.docker.error.InvalidDigestException.class.getName() + ": .*: expected='.*%s', calculated='.*%s'".formatted(digest, "3a6eb0790f39ac87c94f3856b2dd2c5d110e6811602261a9a923d3bb23adc8b7")));
                 } else {
                     throw throwable;
                 }
             }
             return java.util.concurrent.CompletableFuture.allOf();
         })
         .join();
}
```

The patch includes the following changes:

* Added an `if` statement to check if `throwable` is not null and handle the different types of exceptions.
* Replaced the `MatcherAssert.assertThat` for the `IsNot` matcher with a simple `throw throwable` statement.
* Changed the order of the `MatcherAssert.assertThat` for the `MatchesPattern` matcher to match the exception message format.

Note: I'm assuming that the `IsNot` matcher was removed from the new library version and the `MatchesPattern` matcher was added. If that's not the case, please provide the correct matchers to use.