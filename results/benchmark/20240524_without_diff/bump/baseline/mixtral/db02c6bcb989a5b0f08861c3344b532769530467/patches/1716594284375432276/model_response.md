Here is the proposed patch:
```java
@Test
void failsOnDigestMismatch() {
    final InMemoryStorage storage = new InMemoryStorage();
    final AstoBlobs blobs = new AstoBlobs(
            storage, new DefaultLayout(), new RepoName.Simple("any")
    );
    final String digest = "123";
    final String expectedDigest = "3a6eb0790f39ac87c94f3856b2dd2c5d110e6811602261a9a923d3bb23adc8b7";
    blobs.put(
            new CheckedBlobSource(new Content.From("data".getBytes()), new Digest.Sha256(digest))
    ).toCompletableFuture().handle(
            (blob, throwable) -> {
                Assertions.assertNotNull(
                        throwable,
                        "Exception thrown"
                );
                Assertions.assertTrue(
                        throwable instanceof InvalidDigestException,
                        "Exception is InvalidDigestException"
                );
                Assertions.assertTrue(
                        throwable.getMessage().contains(expectedDigest),
                        "Exception message contains calculated digest"
                );
                Assertions.assertTrue(
                        throwable.getMessage().contains(digest),
                        "Exception message contains expected digest"
                );
                return CompletableFuture.allOf();
            }
    ).join();
}
```
The changes include:

* Importing `Assertions` from `org.junit.jupiter.api` to replace the deprecated `MatcherAssert` and `JUnit413StringContains` classes.
* Creating a new variable `expectedDigest` for the calculated digest value.
* Using `Assertions.assertNotNull` instead of `MatcherAssert.assertThat`.
* Using `Assertions.assertTrue` instead of `MatcherAssert.assertThat` with `IsInstanceOf` and `IsNot`.
* Using `throwable.getMessage().contains` instead of `JUnit413StringContains`.