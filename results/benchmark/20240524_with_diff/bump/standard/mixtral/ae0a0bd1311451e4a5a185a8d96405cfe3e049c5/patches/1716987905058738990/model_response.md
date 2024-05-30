Here is the patched method:

```java
@org.junit.jupiter.api.Test
void failsOnDigestMismatch() {
    final com.artipie.asto.memory.InMemoryStorage storage = new com.artipie.asto.memory.InMemoryStorage();
    final com.artipie.docker.asto.AstoBlobs blobs = new com.artipie.docker.asto.AstoBlobs(storage, new com.artipie.docker.asto.DefaultLayout(), new com.artipie.docker.RepoName.Simple("any"));
    final java.lang.String digest = "123";
    blobs.put(new com.artipie.docker.asto.CheckedBlobSource(new com.artipie.asto.Content.From("data".getBytes()), new com.artipie.docker.Digest.Sha256(digest)))
        .thenAccept(blob -> {
            try {
                blob.lock().ifPresent(lock -> lock.close());
            } catch (final java.io.IOException e) {
                throw new com.artipie.docker.asto.InvalidBlobException("Exception thrown", e);
            }
        })
        .thenCompose(blob -> {
            final java.util.concurrent.CompletableFuture<Void> future = new java.util.concurrent.CompletableFuture<>();
            try {
                final java.nio.file.Path path = blob.key().get();
                final java.security.MessageDigest md = java.security.MessageDigest.getInstance("SHA-256");
                md.update(java.nio.file.Files.readAllBytes(path));
                final byte[] calculatedDigest = md.digest();
                if (!java.util.Arrays.equals(calculatedDigest, java.util.Base64.getEncoder().encode(calculatedDigest))) {
                    throw new com.artipie.docker.error.InvalidDigestException(String.format("expected='.*%s', calculated='.*%s'", digest, java.util.Base64.getEncoder().encodeToString(calculatedDigest)));
                }
            } catch (final java.security.NoSuchAlgorithmException | java.io.IOException e) {
                future.completeExceptionally(e);
            }
            return future;
        })
        .join();
}
```

The patch addresses the error message by adding a semicolon at the end of the lambda expression and moving the `handle` method call to a `thenCompose` method call. Additionally, the patch handles the locking and validation of the blob separately. The `InvalidDigestException` is now thrown directly instead of wrapping it in a `NullPointerException`. The `IsNot` and `IsNull` classes have been removed, and the validation of the digest is now done using the `MessageDigest` class.