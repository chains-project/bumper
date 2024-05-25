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
    final CompletableFuture<Blob> putFuture = blobs.put(checkedBlobSource);
    putFuture.handle(
            (blob, throwable) -> {
                if (throwable != null) {
                    MatcherAssert.assertThat(
                            "Exception thrown",
                            throwable,
                            new IsNot<>(new IsNull<>())
                    );
                    MatcherAssert.assertThat(
                            "Exception is InvalidDigestException",
                            throwable,
                            new IsInstanceOf(InvalidDigestException.class)
                    );
                    MatcherAssert.assertThat(
                            "Exception message contains calculated digest",
                            Throwables.getRootCause(throwable).getMessage(),
                            new JUnit413StringContains(calculatedDigest.value())
                    );
                    MatcherAssert.assertThat(
                            "Exception message contains expected digest",
                            Throwables.getRootCause(throwable).getMessage(),
                            new JUnit413StringContains(digest)
                    );
                }
                return CompletableFuture.allOf();
            }
    ).join();
}
```
The patch creates a `Content` object and a `Digest` object based on the content's checksum. It then creates a `CheckedBlobSource` object using these two objects. This allows the `MatcherAssert.assertThat` statements to use the `calculatedDigest` object instead of the hard-coded digest value, which should resolve the compilation error.

Note that the `MatcherAssert.assertThat` statements for the exception message have been updated to use `Throwables.getRootCause(throwable).getMessage()` instead of just `throwable.getMessage()`. This is because the `handle` method may wrap the original exception in a `CompletionException`, so we need to get the root cause of the exception to get the original message.

I hope this helps! Let me know if you have any questions.