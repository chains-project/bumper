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
        final CompletableFuture<Void> handle = put.handle(
            (blob, throwable) -> {
                MatcherAssert.assertThat(
                    "Exception thrown",
                    throwable,
                    new IsNot<>(new IsNull<>())
                );
                MatcherAssert.assertThat(
                    "Exception is InvalidDigestException",
                    Throwables.getRootCause(throwable),
                    new IsInstanceOf(InvalidDigestException.class)
                );
                final String expected = String.format(
                    "Expected digest '%s' does not match calculated digest '%s'",
                    digest,
                    blob.hash()
                );
                MatcherAssert.assertThat(
                    "Exception message contains expected digest",
                    Throwables.getRootCause(throwable).getMessage(),
                    new StringContains(true, expected)
                );
                return CompletableFuture.allOf();
            }
        );
        handle.join();
    }

```