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
                new StringContains(
                    Throwables.getRootCause(throwable).getMessage(),
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

The change I made is to remove the `true` argument from the `StringContains` constructor. This argument was added in a newer version of the library, and is not present in the version you are using. By removing it, the code should be able to compile and run again.

Note that this change may affect the behavior of the test. The `StringContains` matcher now only checks if the expected digest is contained in the message, rather than checking if it is at a specific position in the message. If the position of the digest in the message is important for the test, you may need to modify the code further.