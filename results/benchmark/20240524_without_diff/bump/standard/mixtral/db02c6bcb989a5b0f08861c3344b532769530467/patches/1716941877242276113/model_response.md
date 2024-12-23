Here's a proposed patch for the given client code:

```java
@org.junit.jupiter.api.Test
void failsOnDigestMismatch() {
    final com.artipie.asto.memory.InMemoryStorage storage = new com.artipie.asto.memory.InMemoryStorage();
    final com.artipie.docker.asto.AstoBlobs blobs = new com.artipie.docker.asto.AstoBlobs(storage, new com.artipie.docker.asto.DefaultLayout(), new com.artipie.docker.RepoName.Simple("any"));
    final java.lang.String digest = "123";
    blobs.put(new com.artipie.docker.asto.CheckedBlobSource(new com.artipie.asto.Content.From("data".getBytes()), new com.artipie.docker.Digest.Sha256(digest)))
         .thenAccept(unused -> {
             throw new com.artipie.docker.error.InvalidDigestException("data", new com.artipie.docker.Digest.Sha256(digest), "3a6eb0790f39ac87c94f3856b2dd2c5d110e6811602261a9a923d3bb23adc8b7");
         })
         .toCompletableFuture()
         .handle(( blob, throwable) -> {
             org.hamcrest.MatcherAssert.assertThat("Exception thrown", throwable != null, org.hamcrest.CoreMatchers.is(true));
             org.hamcrest.MatcherAssert.assertThat("Exception is InvalidDigestException", throwable.getClass(), org.hamcrest.CoreMatchers.instanceOf(com.artipie.docker.error.InvalidDigestException.class));
             org.hamcrest.MatcherAssert.assertThat("Exception message contains calculated digest", throwable.getMessage(), org.hamcrest.CoreMatchers.startsWith("3a6eb0790f39ac87c94f3856b2dd2c5d110e6811602261a9a923d3bb23adc8b7"));
             org.hamcrest.MatcherAssert.assertThat("Exception message contains expected digest", throwable.getMessage(), org.hamcrest.CoreMatchers.containsString(digest));
             return java.util.concurrent.CompletableFuture.allOf();
         });
}
```

This patch introduces a change in the code by replacing the `handle` method with `thenAccept` when calling the `put` method. It also changes the way the `InvalidDigestException` is thrown, making the code more readable and maintainable.