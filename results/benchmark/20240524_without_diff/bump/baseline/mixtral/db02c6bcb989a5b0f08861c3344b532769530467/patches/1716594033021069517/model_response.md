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
The patch extracts the message of the root cause of the throwable into a separate variable, and then uses this variable in the `assertThat` calls. This avoids the error message about the unsuitable `assertThat` method.

The patch also removes the unnecessary type argument `<String>` from the `JUnit413StringContains` matcher. This is not necessary and may cause a compilation error in some versions of JUnit.

The patch does not change the function signature or remove the `@Override` decorator, as they are not causing the failure.

The patch does not use any removed library methods or introduce any new library methods.

The patch changes the code by introducing a new variable and modifying the `assertThat` calls to use this variable instead of the `throwable` directly.