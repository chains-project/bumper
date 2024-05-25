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
                String message = Throwables.getRootCause(throwable).getMessage();
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
                        message,
                        new JUnit413StringContains(
                                "3a6eb0790f39ac87c94f3856b2dd2c5d110e6811602261a9a923d3bb23adc8b7"
                        )
                );
                MatcherAssert.assertThat(
                        "Exception message contains expected digest",
                        message,
                        new JUnit413StringContains(digest)
                );
                return CompletableFuture.allOf();
            }
    ).join();
}
```
The patch changes the order of the `MatcherAssert.assertThat` calls and saves the exception message to a variable before using it in the `MatcherAssert.assertThat` calls. This is because the error message suggests that the `MatcherAssert.assertThat` method cannot find a suitable method for the third argument, which is an instance of `JUnit413StringContains`. By saving the message to a variable and using it in the `MatcherAssert.assertThat` calls, the code avoids the error.

Note that this patch assumes that the `JUnit413StringContains` class is a custom class that implements the `Matcher` interface and checks if a string contains another string. If this is not the case, the patch may not work and a different approach may be needed.