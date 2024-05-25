Here is a possible patch for the failing client code:
```java
@Test
void failsOnDigestMismatch() {
    final InMemoryStorage storage = new InMemoryStorage();
    final AstoBlobs blobs = new AstoBlobs(
            storage, new DefaultLayout(), new RepoName.Simple("any")
    );
    final String digest = "123";
    blobs.put(
            new CheckedBlobSource(new Content.From("data".getBytes()), new Digest.Sha256(digest))
    ).toCompletableFuture().handle(
            (blob, throwable) -> {
                if (throwable != null) {
                    InvalidDigestException idException = (InvalidDigestException) Throwables.getRootCause(throwable);
                    MatcherAssert.assertThat(
                            "Exception message contains calculated digest",
                            idException.getMessage(),
                            new JUnit413StringContains("3a6eb0790f39ac87c94f3856b2dd2c5d110e6811602261a9a923d3bb23adc8b7")
                    );
                    MatcherAssert.assertThat(
                            "Exception message contains expected digest",
                            idException.getMessage(),
                            new JUnit413StringContains(digest)
                    );
                } else {
                    fail("Exception was not thrown");
                }
                return CompletableFuture.allOf();
            }
    ).join();
}
```
The patch removes the first `MatcherAssert.assertThat` call and replaces the second one with an `if` statement to check if `throwable` is not null. If `throwable` is not null, the patch extracts the `InvalidDigestException` from the throwable, then uses the `MatcherAssert.assertThat` method to check the exception message.

The patch also removes the `MatcherAssert.assertThat` call that checks if the exception is an `InvalidDigestException` instance, since it is not necessary after the `InvalidDigestException` is extracted from the throwable.

Finally, the patch adds an `else` block to the `if` statement to handle the case where no exception is thrown, and calls the `fail` method to indicate a test failure.