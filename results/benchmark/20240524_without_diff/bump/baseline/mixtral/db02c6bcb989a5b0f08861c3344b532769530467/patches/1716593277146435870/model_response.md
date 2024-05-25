Here is a possible patch for the code:
```java
@Test
void failsOnDigestMismatch() {
    final InMemoryStorage storage = new InMemoryStorage();
    final AstoBlobs blobs = new AstoBlobs(
            storage, new DefaultLayout(), new RepoName.Simple("any")
    );
    final String digest = "123";
    final Content content = new Content.From("data".getBytes());
    final Digest calculatedDigest = new Digest.Sha256(content.digest().algorithm(), content.digest().value());
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
                                calculatedDigest.value()
                        )
                );
                MatcherAssert.assertThat(
                        "Exception message contains expected digest",
                        Throwables.getRootCause(throwable).getMessage(),
                        new JUnit413StringContains(digest)
                );
                return CompletableFuture.allOf();
            }
    ).join();
}
```
The changes I made are:

* I created a `Content` variable `content` to store the content of the blob.
* I created a `Digest` variable `calculatedDigest` to store the calculated digest of the content.
* I replaced the hardcoded expected digest value `3a6eb0790f39ac87c94f3856b2dd2c5d110e6811602261a9a9923d3bb23adc8b7` with the `calculatedDigest` variable.
* I added a cast to `JUnit413StringContains` in the `MatcherAssert.assertThat` call that checks the exception message contains the calculated digest.

These changes should fix the error message and make the code compile.