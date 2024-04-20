Here is the proposed patch:

```java
@org.junit.jupiter.api.Test
void fixesDigestMismatch() {
    final com.artipie.asto.memory.InMemoryStorage storage = new com.artipie.asto.memory.InMemoryStorage();
    final com.artipie.docker.asto.AstoBlobs blobs = new com.artipie.docker.asto.AstoBlobs(storage, new com.artipie.docker.asto.DefaultLayout(), new com.artipie.docker.RepoName.Simple("any"));
    final java.lang.String digest = "123";
    com.artipie.docker.asto.CheckedBlobSource checkedBlobSource = new com.artipie.docker.asto.CheckedBlobSource(new com.artipie.asto.Content.From("data".getBytes()), new com.artipie.docker.Digest.Sha256(digest));
    com.artipie.docker.asto.PutResponse putResponse = blobs.put(checkedBlobSource);
    java.util.concurrent.CompletableFuture<com.artipie.docker.asto.PutResponse> putFuture = putResponse.toCompletableFuture();
    putFuture.handle((putResponse, throwable) -> {
        org.hamcrest.MatcherAssert.assertThat("Exception thrown", throwable, new org.hamcrest.core.IsInstanceOf(com.artipie.docker.error.InvalidDigestException.class));
        org.hamcrest.MatcherAssert.assertThat("Exception message contains calculated digest", putResponse.digest().toString(), new org.hamcrest.core.StringContains("3a6eb0790f39ac87c94f3856b2dd2c5d110e6811602261a9a923d3bb23adc8b7"));
        return null;
    });
    org.hamcrest.MatcherAssert.assertThat("Exception message contains expected digest", putResponse.digest().toString(), digest);
    return java.util.concurrent.CompletableFuture.allOf();
}
```

The changes made include:

* Creating a `checkedBlobSource` variable to store the `CheckedBlobSource` object, to make the code easier to read.
* Changing the argument of `handle` method from `( blob, throwable)` to `(putResponse, throwable)` to match the type of the `CompletableFuture`.
* Changing the first `MatcherAssert.assertThat` statement to check if the exception is an instance of `InvalidDigestException`.
* Changing the second `MatcherAssert.assertThat` statement to check if the calculated digest is contained in the message of the exception.
* Adding a return statement to the lambda expression in the `handle` method.
* Changing the last `MatcherAssert.assertThat` statement to check if the expected digest is equal to the digest of the `PutResponse` object.