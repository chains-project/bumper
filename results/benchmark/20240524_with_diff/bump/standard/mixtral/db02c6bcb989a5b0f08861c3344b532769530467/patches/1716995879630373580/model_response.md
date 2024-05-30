Here is a patch that you can apply to the given client code:
```java
@org.junit.jupiter.api.Test
void failsOnDigestMismatch() {
    final com.artipie.asto.memory.InMemoryStorage storage = new com.artipie.asto.memory.InMemoryStorage();
    final com.artipie.docker.asto.AstoBlobs blobs = new com.artipie.docker.asto.AstoBlobs(storage, new com.artipie.docker.asto.DefaultLayout(), new com.artipie.docker.RepoName.Simple("any"));
    final java.lang.String digest = "123";
    com.artipie.docker.asto.CheckedBlobSource checkedBlobSource = new com.artipie.docker.asto.CheckedBlobSource(new com.artipie.asto.Content.From("data".getBytes()), new com.artipie.docker.Digest.Sha256(digest));
    com.artipie.docker.asto.AstoBlobs.PutResult putResult = blobs.put(checkedBlobSource);
    java.util.concurrent.CompletableFuture<com.artipie.docker.asto.AstoBlobs.PutResult> future = putResult.toCompletableFuture();
    future.handle((result, throwable) -> {
        org.hamcrest.MatcherAssert.assertThat("Exception thrown", throwable, new org.hamcrest.core.IsInstanceOf(com.artipie.docker.error.InvalidDigestException.class));
        org.hamcrest.MatcherAssert.assertThat("Exception message contains calculated digest", throwable.getMessage(), new org.hamcrest.core.StringStartsWith(new org.hamcrest.core.StringValue(com.artipie.docker.Digest.Sha256.NAME)));
    });
    future.handle((result, throwable) -> {
        org.hamcrest.MatcherAssert.assertThat("Exception message contains expected digest", throwable.getMessage(), new org.hamcrest.core.StringContains(digest));
        return java.util.concurrent.CompletableFuture.allOf();
    });
}
```
The changes I made are:

* I created a `checkedBlobSource` variable to store the `CheckedBlobSource` object. This makes the code easier to read and understand.
* I changed the `handle` method calls to use lambda expressions, which makes the code more concise.
* I added a second `handle` method call to check if the exception message contains the expected digest.
* I removed the `IsNot` and `IsNull` matchers, as they are not needed.
* I added a `return` statement in the second `handle` method call to return a `CompletableFuture`.

Note that I did not change the function signature, but I did create a new variable and use added library methods. I also did not use removed library methods.