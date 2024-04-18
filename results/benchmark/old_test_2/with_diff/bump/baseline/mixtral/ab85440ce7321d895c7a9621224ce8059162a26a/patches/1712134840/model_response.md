```java
@Test
void failsOnDigestMismatch() {
    final InMemoryStorage storage = new InMemoryStorage();
    final AstoBlobs blobs = new AstoBlobs(
        storage, new DefaultLayout(), new RepoName.Simple("any")
    );
    final String digest = "123";
    final String calculatedDigest = "3a6eb0790f39ac87c94f3856b2dd2c5d110e6811602261a9a923d3bb23adc8b7";
    blobs.put(
        new CheckedBlobSource(new Content.From("data".getBytes()), new Digest.Sha256(digest))
    ).toCompletableFuture().handle(
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
            MatcherAssert.assertThat(
                "Exception message contains calculated digest",
                Throwables.getRootCause(throwable).getMessage(),
                new StringContains(calculatedDigest)
            );
            MatcherAssert.assertThat(
                "Exception message contains expected digest",
                Throwables.getRootCause(throwable).getMessage(),
                new StringContains(digest)
            );
            MatcherAssert.assertThat(
                "Calculated digest matches",
                calculatedDigest,
                new IsEqual(Digest.sha256("data"))
            );
            return CompletableFuture.allOf();
        }
    ).join();
}
```

Changes made:

* Added a new variable `calculatedDigest` for the calculated digest value.
* Replaced the `StringContains` constructor with the one that takes a single `String` argument.
* Added a new assertion to check if the calculated digest matches the expected one.

Note: The `Digest.sha256` method is assumed to be a new added method in the library. If it's not the case, you might need to replace it with the appropriate method for calculating the SHA-256 digest.