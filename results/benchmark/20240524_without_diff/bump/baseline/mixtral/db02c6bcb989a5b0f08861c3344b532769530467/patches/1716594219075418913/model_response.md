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
The patch removes the method call `MatcherAssert.assertThat(String, Matcher<?>)` and replaces it with a variable `message` that stores the message of the exception. Then, the method call `MatcherAssert.assertThat(String, Matcher<?>)` is used with the variable `message` as the first argument.

This patch assumes that the library `MatcherAssert` has a method `assertThat(String, Matcher<?>)` that takes a `String` as the first argument and a `Matcher<T>` as the second argument. If this assumption is incorrect, the patch may not work and a different solution may be needed.