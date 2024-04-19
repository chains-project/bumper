Here's the fixed version of the `failsOnDigestMismatch()` method:

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
                new IsInstanceOf(InvalidDigestException.class)
            );
            MatcherAssert.assertThat(
                "Exception message contains calculated digest",
                Throwables.getRootCause(throwable).getMessage(),
                new StringContains("3a6eb0790f39ac87c94f3856b2dd2c5d110e6811602261a9a923d3bb23adc8b7")
            );
            MatcherAssert.assertThat(
                "Exception message contains expected digest",
                Throwables.getRootCause(throwable).getMessage(),
                new StringStartsWith(digest)
            );
            return CompletableFuture.allOf();
        }
    ).join();
}
```

The change is in the `StringContains` matcher. It no longer accepts a `boolean` parameter. I replaced the `StringContains` with `StringStartsWith` for the digest comparison. This should fix the error.