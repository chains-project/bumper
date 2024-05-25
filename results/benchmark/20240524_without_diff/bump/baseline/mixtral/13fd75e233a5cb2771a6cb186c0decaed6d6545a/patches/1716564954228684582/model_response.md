Here is a possible patch for the failing client code:
```java
@Test
void failsOnDigestMismatch() {
    final InMemoryStorage storage = new InMemoryStorage();
    final AstoBlobs blobs = new AstoBlobs(
        storage, new DefaultLayout(), new RepoName.Simple("any")
    );
    final String digest = "123";
    CheckedBlobSource source = new CheckedBlobSource(new Content.From("data".getBytes()), new Digest.Sha256(digest));
    BlobId blobId = BlobId.name(Digest.sha256(source.content()));
    blobs.put(source).toCompletableFuture().handle(
        (blob, throwable) -> {
            MatcherAssert.assertThat(
                "Exception thrown",
                throwable,
                notNullValue()
            );
            MatcherAssert.assertThat(
                "Exception is InvalidDigestException",
                Throwables.getRootCause(throwable),
                instanceOf(InvalidDigestException.class)
            );
            MatcherAssert.assertThat(
                "Exception message contains calculated digest",
                Throwables.getRootCause(throwable).getMessage(),
                allOf(
                    stringContains(
                        blobId.digest().toString()
                    ),
                    stringContains(digest)
                )
            )
            );
            return CompletableFuture.allOf();
        }
    ).join();
}
```
Explanation:

* I created a `blobId` variable to represent the expected digest of the blob, computed from its content.
* I used this `blobId` variable in the assertion of the exception message, instead of the hard-coded digest value.
* I used the `Digest.sha256` method to compute the digest of the blob content, instead of the `Digest.Sha256` constructor.
* I used the `BlobId.name` method to create a `blobId` from the digest, instead of concatenating the digest and the prefix manually.

Note: this patch assumes that the `CheckedBlobSource`, `Content`, `Digest`, `MatcherAssert`, `Throwables`, and `CompletableFuture` classes are available and unchanged. It also assumes that the `AstoBlobs` class and the `InMemoryStorage`, `DefaultLayout`, `RepoName`, `BlobId`, and `StringUtils` classes (if used) have not changed their behavior or their constructors.