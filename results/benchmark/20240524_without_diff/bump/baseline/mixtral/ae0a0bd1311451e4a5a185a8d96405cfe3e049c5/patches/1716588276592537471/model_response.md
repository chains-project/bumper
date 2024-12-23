```java
@Test
void failsOnDigestMismatch() {
    final InMemoryStorage storage = new InMemoryStorage();
    final AstoBlobs blobs = new AstoBlobs(
        storage, new DefaultLayout(), new RepoName.Simple("any")
    );
    final String digest = "123";
    final Content content = new Content.From("data".getBytes());
    final Digest calculatedDigest = new Digest.Sha256(content);
    final CheckedBlobSource checkedBlobSource = new CheckedBlobSource(content, calculatedDigest);
    blobs.put(checkedBlobSource)
        .thenAccept(blob -> {
            try {
                MatcherAssert.assertThat(
                    "Exception thrown",
                    Throwables.getRootCause(blob.exception()),
                    new CoreMatchers.InstanceOf(InvalidDigestException.class)
                );
                MatcherAssert.assertThat(
                    "Exception message contains calculated digest",
                    Throwables.getRootCause(blob.exception()).getMessage(),
                    new CoreMatchers.AllOf(
                        new CoreMatchers.StringContains(calculatedDigest.value()),
                        new CoreMatchers.StringContains(digest)
                    )
                );
            } catch (InterruptedException e) {
                throw new RuntimeException(e);
            }
        })
        .join();
}
```