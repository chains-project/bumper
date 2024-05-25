Here is a possible patch for the failing client code:
```java
@Test
void failsOnDigestMismatch() {
    final InMemoryStorage storage = new InMemoryStorage();
    final AstoBlobs blobs = new AstoBlobs(
        storage, new DefaultLayout(), new RepoName.Simple("any")
    );
    final String digest = "123";
    final Content content = new Content.From("data".getBytes());
    final Digest calculatedDigest = new Digest.Sha256(content);
    final CheckedBlobSource checkedBlobSource = new CheckedBlobSource(content, calculatedDigest);
    final BlobId blobId = new BlobId(content.contentType(), calculatedDigest);
    blobs.put(checkedBlobSource).toCompletableFuture().handle(
        (blob, throwable) -> {
            MatcherAssert.assertThat(
                "Exception thrown",
                throwable,
                new CoreMatchers.IsNot.<Throwable>instanceOf(NullPointerException.class)
            );
            MatcherAssert.assertThat(
                "Exception is InvalidDigestException",
                Throwables.getRootCause(throwable),
                new CoreMatchers.InstanceOf(InvalidDigestException.class)
            );
            MatcherAssert.assertThat(
                "Exception message contains calculated digest",
                Throwables.getRootCause(throwable).getMessage(),
                new CoreMatchers.AllOf(
                    new CoreMatchers.StringContains(calculatedDigest.toString()),
                    new CoreMatchers.StringContains(digest)
                )
            );
            return CompletableFuture.allOf();
        }
    ).join();
}
```
The patch creates some variables to make the code more readable and maintainable. It also uses the `toString()` method of the `Digest` class to extract its value as a string. This method is an added library method, identified with `++`. The `Digest.Sha256` constructor is used to create the `calculatedDigest` variable, instead of the `Content` object. This is because the `Digest.Sha256` constructor takes the content as an argument and calculates the digest from it. The `BlobId` constructor is used to create the `blobId` variable, which is the expected id of the blob that will be stored. The `put` method of the `blobs` object is called with the `checkedBlobSource` variable, which is a `CheckedBlobSource` object that wraps the `content` and the `calculatedDigest` variables. The `handle` method of the `CompletableFuture` returned by the `put` method is used to process the result of the asynchronous operation. The `throwable` argument of the lambda expression passed to the `handle` method is used to check that an `InvalidDigestException` is thrown if the digest of the stored blob does not match the expected digest.