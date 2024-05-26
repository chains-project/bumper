```java
@org.junit.jupiter.api.Test
void readAbsentBlob() throws java.lang.Exception {
    final com.artipie.docker.asto.AstoBlobs blobs = new com.artipie.docker.asto.AstoBlobs(new com.artipie.asto.memory.InMemoryStorage(), new com.artipie.docker.asto.DefaultLayout(), new com.artipie.docker.RepoName.Simple("whatever"));
    final com.artipie.docker.Digest digest = new com.artipie.docker.Digest.Sha256("0123456789012345678901234567890123456789012345678901234567890123");
    try {
        blobs.blob(digest).toCompletableFuture().get();
        org.junit.jupiter.api.Assertions.fail("Expected NoSuchElementException");
    } catch (final java.util.concurrent.ExecutionException e) {
        org.junit.jupiter.api.Assertions.assertEquals(java.util.NoSuchElementException.class, e.getCause().getClass());
    }
}
```