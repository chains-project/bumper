Here is a possible patch for the code:
```java
@Test
void failsOnDigestMismatch() {
    final InMemoryStorage storage = new InMemoryStorage();
    final AstoBlobs blobs = new AstoBlobs(
            storage, new DefaultLayout(), new RepoName.Simple("any")
    );
    final String digest = "123";
    final Content content = new Content.From("data".getBytes());
    final Digest calculatedDigest = new Digest.Sha256(content.checksum());
    final CheckedBlobSource checkedBlobSource = new CheckedBlobSource(content, calculatedDigest);
    blobs.put(checkedBlobSource)
            .handle(
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
                                new JUnit413StringContains(calculatedDigest.toString())
                        );
                        MatcherAssert.assertThat(
                                "Exception message contains expected digest",
                                Throwables.getRootCause(throwable).getMessage(),
                                new JUnit413StringContains(digest)
                        );
                        return CompletableFuture.allOf();
                    }
            ).join();
}
```
The changes I made are:

* I created a `Content` object and calculated its digest using the `checksum()` method.
* I created a `CheckedBlobSource` object using the `Content` object and the calculated digest.
* I removed the `Digest.Sha256` constructor from the `CheckedBlobSource` constructor call.
* I updated the `JUnit413StringContains` assertion to use the `calculatedDigest.toString()` method instead of the hard-coded digest value.

These changes should fix the compilation error by providing a suitable method for the `assertThat()` call.

Note that I don't have enough context to verify if the updated code is functionally correct, so it's important to thoroughly test the updated code before deploying it.