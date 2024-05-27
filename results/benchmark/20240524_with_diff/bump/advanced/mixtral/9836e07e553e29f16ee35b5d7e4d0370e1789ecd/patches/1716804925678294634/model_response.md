Here's the patched code:

```java
@org.junit.jupiter.api.Test
void failsOnDigestMismatch() {
    final com.artipie.asto.memory.InMemoryStorage storage = new com.artipie.asto.memory.InMemoryStorage();
    final com.artipie.docker.asto.AstoBlobs blobs = new com.artipie.docker.asto.AstoBlobs(storage, new com.artipie.docker.asto.DefaultLayout(), new com.artipie.docker.RepoName.Simple("any"));
    final java.lang.String digest = "123";
    blobs.put(new com.artipie.docker.asto.CheckedBlobSource(new com.artipie.asto.Content.From("data".getBytes()), new com.artipie.docker.Digest.Sha256(digest)))
         .thenAccept(blob -> {
            org.hamcrest.MatcherAssert.assertThat("Exception thrown", false, new org.hamcrest.core.IsInstanceOf(com.artipie.docker.asto.IsNull.class));
            org.hamcrest.MatcherAssert.assertThat("Exception is InvalidDigestException", com.google.common.base.Throwables.getRootCause(new RuntimeException()), new org.hamcrest.MatcherAssert.MatchesPattern(com.artipie.docker.error.InvalidDigestException.class.getName() + ": .*"));
            org.hamcrest.MatcherAssert.assertThat("Exception message contains calculated digest", com.google.common.base.Throwables.getRootCause(new RuntimeException()).getMessage(), new org.hamcrest.core.StringContains.Containing(new java.lang.StringBuilder("3a6eb0790f39ac87c94f3856b2dd2c5d110e6811602261a9a923d3bb23adc8b7").toString()));
         })
         .exceptionally(throwable -> {
            org.hamcrest.MatcherAssert.assertThat("Exception message contains expected digest", com.google.common.base.Throwables.getRootCause(throwable).getMessage(), new org.hamcrest.core.StringContains.Containing(digest));
            return null;
         });
    return java.util.concurrent.CompletableFuture.allOf();
}
```

The following changes have been made:

* Replaced `handle` with `thenAccept` and `exceptionally` to handle success and failure cases separately.
* Wrapped the conditions in `thenAccept` with a lambda that returns nothing.
* Wrapped the condition in `exceptionally` with a lambda that returns null.
* Wrapped the conditions in `assertThat` with `com.google.common.base.Throwables.getRootCause(new RuntimeException())` to get the root cause of the exception.
* Wrapped the conditions in `assertThat` with `com.google.common.base.Throwables.getRootCause(throwable)` in `exceptionally` to get the root cause of the exception.
* Added `return null;` in `exceptionally` to satisfy the method signature.
* Added semicolons to separate statements.
* Added parentheses to make the method call clearer.
* Added space after commas for readability.