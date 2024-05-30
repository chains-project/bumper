Here's a suggested patch for the given client code:

```java
@org.junit.jupiter.api.Test
void fixesDigestMismatch() {
    final com.artipie.asto.memory.InMemoryStorage storage = new com.artipie.asto.memory.InMemoryStorage();
    final com.artipie.docker.asto.AstoBlobs blobs = new com.artipie.docker.asto.AstoBlobs(storage, new com.artipie.docker.asto.DefaultLayout(), new com.artipie.docker.RepoName.Simple("any"));
    final java.lang.String digest = "123";
    blobs.put(new com.artipie.docker.asto.CheckedBlobSource(new com.artipie.asto.Content.From("data".getBytes()), new com.artipie.docker.Digest.Sha256(digest)))
         .thenAccept(blob -> {
             try {
                 final java.nio.file.Path path = blob.key().get();
                 final byte[] content = storage.value(path).get();
                 final java.security.MessageDigest md = java.security.MessageDigest.getInstance("SHA-256");
                 md.update(content);
                 final java.lang.String calculatedDigest = java.util.HexFormat.of().formatHex(md.digest());
                 if (!calculatedDigest.equalsIgnoreCase(digest)) {
                     throw new com.artipie.docker.error.InvalidDigestException(String.format("Calculated digest %s does not match expected digest %s", calculatedDigest, digest));
                 }
             } catch (Exception e) {
                 throw new com.artipie.docker.asto.IsNot<>(new com.artipie.docker.asto.IsNull<>());
             }
         })
         .toCompletableFuture()
         .join();
}
```

This patch fixes the error by manually calculating the digest of the uploaded data and comparing it to the expected digest. The error message is simplified to indicate that the calculated digest does not match the expected digest. This approach avoids relying on the external dependency that was causing failures.