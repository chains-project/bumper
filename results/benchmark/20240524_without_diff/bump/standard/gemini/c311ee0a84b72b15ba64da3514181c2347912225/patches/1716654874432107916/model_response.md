```java
@org.junit.jupiter.api.Test
void readAbsentBlob() throws java.lang.Exception {
    final com.artipie.docker.asto.AstoBlobs blobs = new com.artipie.docker.asto.AstoBlobs(new com.artipie.asto.memory.InMemoryStorage(), new com.artipie.docker.asto.DefaultLayout(), new com.artipie.docker.RepoName.Simple("whatever"));
    final com.artipie.docker.Digest digest = new com.artipie.docker.Digest.Sha256("0123456789012345678901234567890123456789012345678901234567890123");
    org.hamcrest.MatcherAssert.assertThat(blobs.blob(digest).toCompletableFuture().get().isPresent(), new org.hamcrest.core.IsEqual<>(false));
}
```