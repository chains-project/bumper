```java
@Test
public void failsOnDigestMismatch() {
    // Create an in-memory storage and a blob store.
    InMemoryStorage storage = new InMemoryStorage();
    AstoBlobs blobs = new AstoBlobs(storage, new DefaultLayout(), new RepoName.Simple("any"));

    // Calculate the expected digest for the data.
    String expectedDigest = "3a6eb0790f39ac87c94f3856b2dd2c5d110e6811602261a9a923d3bb23adc8b7";

    // Create a blob source with the data and the expected digest.
    CheckedBlobSource blobSource = new CheckedBlobSource(new Content.From("data".getBytes()), new Digest.Sha256(expectedDigest));

    // Put the blob into the blob store.
    CompletableFuture<Void> future = blobs.put(blobSource);

    // Handle the result of the put operation.
    future.handle((blob, throwable) -> {
        // Assert that an exception was thrown.
        assertThat(throwable, notNullValue());

        // Assert that the exception is an InvalidDigestException.
        assertThat(Throwables.getRootCause(throwable), instanceOf(InvalidDigestException.class));

        // Assert that the exception message contains the calculated digest.
        assertThat(Throwables.getRootCause(throwable).getMessage(), containsString(expectedDigest));

        // Return a completed future.
        return CompletableFuture.allOf();
    }).join();
}
```