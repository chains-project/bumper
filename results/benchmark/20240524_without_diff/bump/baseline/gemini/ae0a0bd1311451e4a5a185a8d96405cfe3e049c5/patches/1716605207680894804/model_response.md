```java
  @Test
  public void failsOnDigestMismatch() throws Exception {
    final InMemoryStorage storage = new InMemoryStorage();
    final AstoBlobs blobs = new AstoBlobs(storage, new DefaultLayout(), new RepoName.Simple("any"));
    final String digest = "123";
    final CompletableFuture<Blob> blobFuture = blobs.put(new CheckedBlobSource(new Content.From("data".getBytes()), new Digest.Sha256(digest)));
    final CompletableFuture<Void> completionFuture = blobFuture.thenAccept(
      blob -> {
        try {
          final String actualDigest = blobs.get(blob.layer()).digest().value();
          MatcherAssert.assertThat(actualDigest, new StringContains(true, digest));
        } catch (IOException e) {
          throw new RuntimeException(e);
        }
      }
    );
    try {
      completionFuture.get();
      fail("Expected an exception to be thrown.");
    } catch (ExecutionException e) {
      MatcherAssert.assertThat(e.getCause(), new IsInstanceOf(InvalidDigestException.class));
      MatcherAssert.assertThat(
        e.getCause().getMessage(),
        new StringContains(true, "3a6eb0790f39ac87c94f3856b2dd2c5d110e6811602261a9a923d3bb23adc8b7")
      );
      MatcherAssert.assertThat(
        e.getCause().getMessage(),
        new StringContains(true, digest)
      );
    }
  }
```