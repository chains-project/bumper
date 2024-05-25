```java
@Test
void failsOnDigestMismatch() throws Exception {
    final InMemoryStorage storage = new InMemoryStorage();
    final AstoBlobs blobs = new AstoBlobs(
        storage, new DefaultLayout(), new RepoName.Simple("any")
    );
    final String digest = "123";
    blobs.put(
        new CheckedBlobSource(new Content.From("data".getBytes()), new Digest.Sha256(digest))
    ).toCompletableFuture().handle(
        (blob, throwable) -> {
            assertThat(throwable, notNullValue());
            assertThat(Throwables.getRootCause(throwable), instanceOf(InvalidDigestException.class));
            assertThat(
                Throwables.getRootCause(throwable).getMessage(),
                containsString("3a6eb0790f39ac87c94f3856b2dd2c5d110e6811602261a9a923d3bb23adc8b7")
            );
            assertThat(
                Throwables.getRootCause(throwable).getMessage(),
                containsString(digest)
            );
            return CompletableFuture.allOf();
        }
    ).join();
}
```