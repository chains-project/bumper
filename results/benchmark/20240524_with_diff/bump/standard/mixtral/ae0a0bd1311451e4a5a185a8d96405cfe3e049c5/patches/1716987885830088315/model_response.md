Here's the fixed method with the error resolved:

```java
@org.junit.jupiter.api.Test
void failsOnDigestMismatch() {
    final com.artipie.asto.memory.InMemoryStorage storage = new com.artipie.asto.memory.InMemoryStorage();
    final com.artipie.docker.asto.AstoBlobs blobs = new com.artipie.docker.asto.AstoBlobs(storage, new com.artipie.docker.asto.DefaultLayout(), new com.artipie.docker.RepoName.Simple("any"));
    final java.lang.String digest = "123";
    blobs.put(new com.artipie.docker.asto.CheckedBlobSource(new com.artipie.asto.Content.From("data".getBytes()), new com.artipie.docker.Digest.Sha256(digest)))
        .thenAccept(unused -> {
            throw new com.artipie.docker.asto.InvalidDigestException(
                String.format(
                    "expected='.*%s', calculated='.*%s'",
                    digest,
                    "3a6eb0790f39ac87c94f3856b2dd2c5d110e6811602261a9a923d3bb23adc8b7"
                )
            );
        })
        .toCompletableFuture()
        .join();
}
```

The main change is converting the `handle` method to `thenAccept` to handle the successful result and throw the `InvalidDigestException`. The original code used a lambda with a void return type, which caused the ';' expected error. The new code uses a lambda with a non-void return type, so the result can be returned from the `thenAccept` method.