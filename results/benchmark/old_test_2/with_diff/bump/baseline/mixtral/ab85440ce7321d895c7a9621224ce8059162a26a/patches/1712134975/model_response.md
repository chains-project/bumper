Here's a suggested patch for the failing client code:

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
                MatcherAssert.assertThat(
                        "Exception thrown",
                        throwable,
                        new IsNot<>(new IsNull<>())
                );
                MatcherAssert.assertThat(
                        "Exception is InvalidDigestException",
                        Throwables.getRootCause(throwable),
                        new InstanceOf(InvalidDigestException.class)
                );
                String message = Throwables.getRootCause(throwable).getMessage();
                MatcherAssert.assertThat(
                        "Exception message contains calculated digest",
                        message,
                        new StringContains("3a6eb0790f39ac87c94f3856b2dd2c5d110e6811602261a9a923d3bb23adc8b7")
                );
                MatcherAssert.assertThat(
                        "Exception message contains expected digest",
                        message,
                        new StringContains(digest)
                );
                MatcherAssert.assertThat(
                        "Exception message contains expected digest",
                        message,
                        new StringContains(digest)
                );
                return CompletableFuture.allOf();
            }
    ).join();
}
```

In this patch, I replaced the `StringContains` constructor with a new one that only takes a single argument. This should fix the compilation error. I also created a new variable `message` to store the exception message, making the code easier to read.