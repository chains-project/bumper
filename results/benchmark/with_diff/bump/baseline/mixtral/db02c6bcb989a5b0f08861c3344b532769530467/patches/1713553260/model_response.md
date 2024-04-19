Here is a possible patch for the failing code:
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
                new StringStartsWith(
                    "3a6eb0790f39ac87c94f3856b2dd2c5d110e6811602261a9a923d3bb23adc8b7"
                )
            );
            MatcherAssert.assertThat(
                "Exception message contains expected digest",
                Throwables.getRootCause(throwable).getMessage(),
                new StringContains(digest)
            );
            return CompletableFuture.allOf();
        }
    ).join();
}
```
The changes I made are:

* Replace the `StringContains` matcher with the `StringStartsWith` matcher for the calculated digest. This is because the `StringContains` constructor that takes a boolean flag as the second argument has been removed in the new library version.
* Remove the boolean flag from the `StringContains` matcher for the expected digest. This is because the constructor that takes a boolean flag as the second argument has been removed in the new library version.

I hope this helps! Let me know if you have any questions.