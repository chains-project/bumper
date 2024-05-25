Here's a patch that you can apply to fix the error:

```java
@Test
void failsOnDigestMismatch() {
    final InMemoryStorage storage = new InMemoryStorage();
    final AstoBlobs blobs = new AstoBlobs(
            storage, new DefaultLayout(), new RepoName.Simple("any")
    );
    final String digest = "123";
    final Content content = new Content.From("data".getBytes());
    final Digest calculatedDigest = new Digest.Sha256(content.digest());
    blobs.put(
            new CheckedBlobSource(content, new Digest.Sha256(digest))
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
                        new JUnit413StringContains(
                                calculatedDigest.toString()
                        )
                );
                MatcherAssert.assertThat(
                        "Exception message contains expected digest",
                        Throwables.getRootCause(throwable).getMessage(),
                        new JUnit413StringContains(digest)
                );
                MatcherAssert.assertThat(
                        "Calculated digest matches expected digest",
                        calculatedDigest,
                        new IsEqual<Digest>(new Digest.Sha256(digest))
                );
                return CompletableFuture.allOf();
            }
    ).join();
}
```

The changes I made are:

* Created a new variable `content` to hold the content of the blob.
* Created a new variable `calculatedDigest` to hold the digest of the content.
* Updated the `JUnit413StringContains` matcher to check if the calculated digest is in the exception message.
* Added a new `IsEqual` matcher to check if the calculated digest matches the expected digest.

These changes should fix the error and make the test pass.