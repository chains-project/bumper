```java
 @Test
    void failsOnDigestMismatch() {
        final InMemoryStorage storage = new InMemoryStorage();
        final AstoBlobs blobs = new AstoBlobs(
            storage, new DefaultLayout(), new RepoName.Simple("any")
        );
        final String digest = "123";

        final CompletableFuture<Blob> put = blobs.put(
            new CheckedBlobSource(new Content.From("data".getBytes()), new Digest.Sha256(digest))
        );

        final CompletableFuture<Void> future = put.thenAccept(
            blob -> {
                MatcherAssert.assertThat(
                    "Exception thrown",
                    put.exceptionally(e -> e),
                    new IsNot<>(new IsNull<>())
                );
                MatcherAssert.assertThat(
                    "Exception is InvalidDigestException",
                    Throwables.getRootCause(put.exceptionally(e -> e)),
                    new IsInstanceOf(InvalidDigestException.class)
                );
                MatcherAssert.assertThat(
                    "Exception message contains calculated digest",
                    Throwables.getRootCause(put.exceptionally(e -> e)).getMessage(),
                    new StringContains(
                        true,
                        "3a6eb0790f39ac87c94f3856b2dd2c5d110e6811602261a9a923d3bb23adc8b7"
                    )
                );
                MatcherAssert.assertThat(
                    "Exception message contains expected digest",
                    Throwables.getRootCause(put.exceptionally(e -> e)).getMessage(),
                    new StringContains(true, digest)
                );
            }
        );

        future.join();
    }
```