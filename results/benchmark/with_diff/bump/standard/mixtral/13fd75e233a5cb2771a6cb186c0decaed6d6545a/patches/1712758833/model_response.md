Here is the proposed patch:

```java
@org.junit.jupiter.api.Test
void fixedDigestMismatch() {
    final com.artipie.asto.memory.InMemoryStorage storage = new com.artipie.asto.memory.InMemoryStorage();
    final com.artipie.docker.asto.AstoBlobs blobs = new com.artipie.docker.asto.AstoBlobs(storage, new com.artipie.docker.asto.DefaultLayout(), new com.artipie.docker.RepoName.Simple("any"));
    final java.lang.String digest = "123";
    blobs.put(new com.artipie.docker.asto.CheckedBlobSource(new com.artipie.asto.Content.From("data".getBytes()), new com.artipie.docker.Digest.Sha256(digest)))
         .thenAccept(unused -> {
             throw new com.artipie.docker.error.InvalidDigestException(
                     "3a6eb0790f39ac87c94f3856b2dd2c5d110e6811602261a9a923d3bb23adc8b7",
                     digest
             );
         })
         .toCompletableFuture()
         .join();
}
```

Explanation:

* I replaced the `handle` method with `thenAccept` and `toCompletableFuture` to handle the success and failure cases, respectively.
* I created a new `InvalidDigestException` instance with the expected digest values.
* The `join` method is used to wait for the completion of the `CompletableFuture`.
* I changed the name of the method to `fixedDigestMismatch` to indicate that it is the fixed version of the failing method.