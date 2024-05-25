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
In this patch, I extracted the exception message to a variable `message` before performing the `MatcherAssert.assertThat` operations. This is because the error message indicates that there is no suitable method for `MatcherAssert.assertThat` that takes a `String`, a `String`, and an instance of `JUnit413StringContains`.

By storing the exception message in a variable, we can avoid this error and still perform the desired assertions on the message.

Note that this patch assumes that the `JUnit413StringContains` class is a custom matcher that extends the `org.hamcrest.Matcher` interface and provides a `matchesSafely` method that takes a `String` and a `String` as arguments. If this is not the case, the patch may need to be adjusted accordingly.