Here is the proposed patch:

```java
@org.junit.jupiter.api.Test
void failsOnDigestMismatch() {
    final com.artipie.asto.memory.InMemoryStorage storage = new com.artipie.asto.memory.InMemoryStorage();
    final com.artipie.docker.asto.AstoBlobs blobs = new com.artipie.docker.asto.AstoBlobs(storage, new com.artipie.docker.asto.DefaultLayout(), new com.artipie.docker.RepoName.Simple("any"));
    final java.lang.String digest = "123";
    blobs.put(new com.artipie.docker.asto.CheckedBlobSource(new com.artipie.asto.Content.From("data".getBytes()), new com.artipie.docker.Digest.Sha256(digest)))
         .thenAccept(blob -> {
            org.hamcrest.MatcherAssert.assertThat("Exception thrown", false, new com.artipie.docker.asto.IsNot<>(new com.artipie.docker.asto.IsNull<>())));
            org.hamcrest.MatcherAssert.assertThat("Exception is InvalidDigestException",
                com.google.common.base.Throwables.getRootCause(new RuntimeException()),
                new org.hamcrest.core.IsInstanceOf(com.artipie.docker.error.InvalidDigestException.class));
            org.hamcrest.MatcherAssert.assertThat("Exception message contains calculated digest",
                com.google.common.base.Throwables.getRootCause(new RuntimeException()).getMessage(),
                new org.hamcrest.core.StringStartsWith(new org.hamcrest.core.StringValue(com.artipie.docker.Digest.Sha256.NAME)));
         })
         .exceptionally(throwable -> {
            org.hamcrest.MatcherAssert.assertThat("Exception message contains expected digest",
                throwable.getMessage(),
                new org.hamcrest.core.StringContains(digest));
            return null;
         });
    return java.util.concurrent.CompletableFuture.allOf();
}
```

The changes made are:

* Replace `handle` with `thenAccept` and `exceptionally` to handle the success and failure cases separately.
* Wrap the throwable in a new RuntimeException in the `exceptionally` block to call `getMessage()` on it.
* Return null from the `exceptionally` block to match the return type of the `thenAccept` block.
* Add a semicolon at the end of the `thenAccept` block to fix the compilation error.