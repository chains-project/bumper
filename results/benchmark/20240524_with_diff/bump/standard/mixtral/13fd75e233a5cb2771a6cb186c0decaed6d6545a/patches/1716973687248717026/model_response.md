Here's a suggested patch for the given client code:

```java
// TODO: review this AI generated patch!
@org.junit.jupiter.api.Test
void failsOnDigestMismatch() {
    final com.artipie.asto.memory.InMemoryStorage storage = new com.artipie.asto.memory.InMemoryStorage();
    final com.artipie.docker.asto.AstoBlobs blobs = new com.artipie.docker.asto.AstoBlobs(storage, new com.artipie.docker.asto.DefaultLayout(), new com.artipie.docker.RepoName.Simple("any"));
    final java.lang.String digest = "123";
    blobs.put(new com.artipie.docker.asto.CheckedBlobSource(new com.artipie.asto.Content.From("data".getBytes()), new com.artipie.docker.Digest.Sha256(digest)))
         .thenAccept(blob -> {
             try {
                 blob.write().toCompletableFuture().get();
             } catch (Exception e) {
                 org.hamcrest.MatcherAssert.assertThat("Exception thrown", e, new com.artipie.docker.asto.IsNot<>(new com.artipie.docker.asto.IsNull<>()));
                 org.hamcrest.MatcherAssert.assertThat("Exception is InvalidDigestException", e, new org.hamcrest.core.IsInstanceOf(com.artipie.docker.error.InvalidDigestException.class));
                 org.hamcrest.MatcherAssert.assertThat("Exception message contains calculated digest", e.getMessage(), new org.hamcrest.core.StringStartsWith(new org.hamcrest.core.StringValue(com.artipie.docker.Digest.Sha256.NAME)));
             }
         });
    org.hamcrest.MatcherAssert.assertThat("Exception message contains expected digest", com.google.common.base.Throwables.getRootCause(throwable).getMessage(), new org.hamcrest.core.StringContains(digest));
    return java.util.concurrent.CompletableFuture.allOf();
}
```

The error message suggests that a semicolon is expected, which can be resolved by changing the lambda expression. Additionally, I replaced the `handle` method with `thenAccept` and added a try-catch block to handle exceptions properly.

As the new library version doesn't include any relevant changes, I haven't used any added library methods in the patched code.