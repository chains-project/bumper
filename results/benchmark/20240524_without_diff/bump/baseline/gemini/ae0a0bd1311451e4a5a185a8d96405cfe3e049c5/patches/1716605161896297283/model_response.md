```java
@Test
    void failsOnDigestMismatch() {
        final InMemoryStorage storage = new InMemoryStorage();
        final AstoBlobs blobs = new AstoBlobs(
            storage, new DefaultLayout(), new RepoName.Simple("any")
        );
        final String digest = "123";
        final Digest sha256 = new Digest.Sha256(digest);
        final BlobSource source = new CheckedBlobSource(new Content.From("data".getBytes()), sha256);
        final CompletableFuture<Blob> future = blobs.put(source);
        final Blob blob = future.join();

        assertThat(blob.hash(), is(sha256));
    }
```