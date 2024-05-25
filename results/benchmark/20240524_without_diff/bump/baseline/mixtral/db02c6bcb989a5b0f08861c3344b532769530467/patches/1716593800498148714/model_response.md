Here is a patch that you can apply to the code in order to fix the error:
```java
@Test
void failsOnDigestMismatch() {
    final InMemoryStorage storage = new InMemoryStorage();
    final AstoBlobs blobs = new AstoBlobs(
            storage, new DefaultLayout(), new RepoName.Simple("any")
    );
    final String digest = "123";
    final JUnit413StringContains containsDigest = new JUnit413StringContains(digest);
    final JUnit413StringContains containsCalculatedDigest = new JUnit413StringContains(
            "3a6eb0790f39ac87c94f3856b2dd2c5d110e6811602261a9a923d3bb23adc8b7"
    );
    blobs.put(
            new CheckedBlobSource(new Content.From("data".getBytes()), new Digest.Sha256(digest))
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
                        containsCalculatedDigest
                );
                MatcherAssert.assertThat(
                        "Exception message contains expected digest",
                        Throwables.getRootCause(throwable).getMessage(),
                        containsDigest
                );
                return CompletableFuture.allOf();
            }
    ).join();
}
```
This patch creates two new variables `containsDigest` and `containsCalculatedDigest` to replace the anonymous instances of `JUnit413StringContains`. This makes the code easier to read and understand. It also makes it clear that the same instance of `JUnit413StringContains` is being reused in multiple assertions.

I hope this helps! Let me know if you have any questions.