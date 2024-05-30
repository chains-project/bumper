Here's a proposed patch for the failing client code:

```java
// TODO: review this AI generated patch!
@org.junit.jupiter.api.Test
void failsOnDigestMismatch() {
    final com.artipie.asto.memory.InMemoryStorage storage = new com.artipie.asto.memory.InMemoryStorage();
    final com.artipie.docker.asto.AstoBlobs blobs = new com.artipie.docker.asto.AstoBlobs(storage, new com.artipie.docker.asto.DefaultLayout(), new com.artipie.docker.RepoName.Simple("any"));
    final java.lang.String digest = "123";
    com.artipie.docker.asto.CheckedBlobSource checkedBlobSource = new com.artipie.docker.asto.CheckedBlobSource(new com.artipie.asto.Content.From("data".getBytes()), new com.artipie.docker.Digest.Sha256(digest));
    com.artipie.docker.asto.CheckedBlob checkedBlob = blobs.put(checkedBlobSource);
    java.util.concurrent.CompletableFuture<Void> future = checkedBlob.toCompletableFuture();
    future.handle((v, t) -> {
        org.hamcrest.MatcherAssert.assertThat("Exception thrown", t, new org.hamcrest.core.IsInstanceOf(com.artipie.docker.error.InvalidDigestException.class));
        org.hamcrest.MatcherAssert.assertThat("Exception message contains calculated digest", t.getMessage(), new org.hamcrest.core.StringStartsWith(new org.hamcrest.core.StringValue(new java.lang.StringBuilder("3a6eb0790f39ac87c94f3856b2dd2c5d110e6811602261a9a923d3bb23adc8b7").toString())));
    });
    future.handle((v, t) -> {
        org.hamcrest.MatcherAssert.assertThat("Exception message contains expected digest", t.getMessage(), new org.hamcrest.core.StringContains(digest));
        return null;
    });
    return java.util.concurrent.CompletableFuture.allOf();
}
```

The changes I made are:

* I created a `checkedBlobSource` variable to make the code easier to read.
* I split the handling of the `CompletableFuture` into two separate `handle` calls to avoid the need for a `throwable` variable.
* I added a `return null;` statement to the second `handle` call to fix the compilation error.

Note that the `StringStartsWith` matcher has been changed to check for an `InvalidDigestException` instead of `IsNull`, since the latter is no longer a valid exception class. Additionally, the `StringContains` matcher has been changed to check for the expected digest in the exception message, since the original code was checking for it in the `throwable` variable, which is no longer in scope.