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
    final Digest calculatedDigest = new Digest.Sha256(content.checksum());
    final CheckedBlobSource checkedBlobSource = new CheckedBlobSource(content, calculatedDigest);
    final CompletableFuture<Blob> putFuture = blobs.put(checkedBlobSource);
    final InvalidDigestException exception = assertThrows(InvalidDigestException.class, putFuture::join);
    assertEquals(
            "Exception message contains calculated digest",
            "3a6eb0790f39ac87c94f3856b2dd2c5d110e6811602261a9a923d3bb23adc8b7",
            exception.calculatedDigest().toString()
    );
    assertEquals(
            "Exception message contains expected digest",
            digest,
            exception.expectedDigest()
    );
}
```
In this patch, I have used JUnit 5's `assertThrows` method to simplify the exception handling, and `assertEquals` to replace the custom `JUnit413StringContains` matcher. I have also created some local variables to make the code more readable.

Note that this patch assumes that the `InMemoryStorage`, `AstoBlobs`, `Content`, `Digest`, `CheckedBlobSource`, and `InvalidDigestException` classes are unchanged. If any of these classes have been modified in the new version, the patch may need to be adjusted accordingly.