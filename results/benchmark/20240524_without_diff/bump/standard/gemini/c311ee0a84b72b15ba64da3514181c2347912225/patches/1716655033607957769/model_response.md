```java
@org.junit.jupiter.api.Test
void writeAndReadBlob() throws java.lang.Exception {
    final com.artipie.docker.asto.AstoBlobs blobs = new com.artipie.docker.asto.AstoBlobs(new com.artipie.asto.memory.InMemoryStorage(), new com.artipie.docker.asto.DefaultLayout(), new com.artipie.docker.RepoName.Simple("test"));
    final byte[] bytes = new byte[]{ 0x5, 0x6, 0x7, 0x8 };
    final com.artipie.docker.Digest digest = blobs.put(new com.artipie.docker.asto.TrustedBlobSource(bytes)).toCompletableFuture().get().digest();
    final byte[] read = blobs.blob(digest).toCompletableFuture().get().get().content().toCompletableFuture().get().array();
    org.hamcrest.MatcherAssert.assertThat(read, org.hamcrest.Matchers.equalTo(bytes));
}
```