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
The patch modifies the assertion on the exception message by assigning it to a variable and using it in the subsequent assertions. This avoids the compilation error caused by passing a `String` argument to a method that expects a `Matcher<String>` argument.

I hope this helps! Let me know if you have any questions or if there's anything else I can do for you.