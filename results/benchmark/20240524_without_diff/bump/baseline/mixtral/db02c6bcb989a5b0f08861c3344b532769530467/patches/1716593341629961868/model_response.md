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
                String exceptionMessage = Throwables.getRootCause(throwable).getMessage();
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
                        exceptionMessage,
                        new JUnit413StringContains(
                                "3a6eb0790f39ac87c94f3856b2dd2c5d110e6811602261a9a923d3bb23adc8b7"
                        )
                );
                MatcherAssert.assertThat(
                        "Exception message contains expected digest",
                        exceptionMessage,
                        new JUnit413StringContains(digest)
                );
                return CompletableFuture.allOf();
            }
    ).join();
}
```
The patch modifies the way the `exceptionMessage` is extracted from the `throwable` object, by using the `Throwables.getRootCause(throwable)` method to get the root cause of the exception, and then calling the `getMessage()` method on it. This way, the `assertThat()` method can be called with the correct arguments.

Note that the `MatcherAssert.assertThat()` method has been called twice with the same `throwable` object, but with different matchers. This is because the first `assertThat()` call checks if the exception is an `InvalidDigestException`, and the second `assertThat()` call checks if the exception message contains the expected digest.

The `MatcherAssert.assertThat()` method has also been called twice with the same `exceptionMessage` object, but with different matchers. This is because the first `assertThat()` call checks if the exception message contains the calculated digest, and the second `assertThat()` call checks if the exception message contains the expected digest.

Finally, the `CompletableFuture.allOf()` method is returned from the `handle()` method, to indicate that the asynchronous operation has completed successfully.