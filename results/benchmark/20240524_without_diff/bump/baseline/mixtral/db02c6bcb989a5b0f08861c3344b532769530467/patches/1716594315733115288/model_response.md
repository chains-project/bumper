Here is a possible patch for the failing client code:
```java
@Test
void failsOnDigestMismatch() {
    final InMemoryStorage storage = new InMemoryStorage();
    final AstoBlobs blobs = new AstoBlobs(
            storage, new DefaultLayout(), new RepoName.Simple("any")
    );
    final String digest = "123";
    final Content content = new Content.From("data".getBytes());
    final Digest calculatedDigest = new Digest.Sha256(content.checksum());
    final CheckedBlobSource checkedBlobSource = new CheckedBlobSource(content, calculatedDigest);
    final InvalidDigestException expectedException = new InvalidDigestException(
            "blob's digest does not match expected digest",
            checkedBlobSource,
            calculatedDigest,
            new Digest.Sha256(digest)
    );
    blobs.put(checkedBlobSource)
            .toCompletableFuture()
            .handle(
                    (blob, throwable) -> {
                        if (throwable == null) {
                            throw new AssertionError("Expected InvalidDigestException, but got no exception");
                        }
                        Assertions.assertThat(throwable).isInstanceOf(InvalidDigestException.class);
                        Assertions.assertThat(throwable.getMessage()).containsSequence(
                                "blob's digest does not match expected digest",
                                calculatedDigest.value(),
                                digest
                        );
                        return CompletableFuture.allOf();
                    }
            )
            .join();
}
```
This patch uses JUnit 5's `Assertions` class instead of JUnit 4's `MatcherAssert` and `Throwables` classes. It also creates some variables to make the code more readable. The `InvalidDigestException` is constructed explicitly with the expected message and digests. The `handle` method is simplified by using a single `if` statement to check for the expected exception. The `MatcherAssert.assertThat` and `Throwables.getRootCause` methods are replaced with `Assertions.assertThat` and `throwable.getMessage()`, respectively. The `JUnit413StringContains` matcher is replaced with `Assertions.assertThat(throwable.getMessage()).containsSequence`.