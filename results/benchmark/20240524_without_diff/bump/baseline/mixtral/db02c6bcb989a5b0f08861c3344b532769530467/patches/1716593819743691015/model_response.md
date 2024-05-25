Here is a patch that you can apply to fix the error:
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
    putFuture.handle(
            (blob, throwable) -> {
                assertThat(throwable, notNullValue());
                assertThat(throwable, instanceOf(InvalidDigestException.class));
                assertThat(throwable.getMessage(), stringContainsInOrder(
                        calculatedDigest.value(),
                        digest
                ));
                return CompletableFuture.allOf();
            }
    ).join();
}
```
The main changes are:

* Creating variables for `Content` and `Digest` to make the code more readable.
* Using `notNullValue()` instead of `new IsNot<>(new IsNull<>())`.
* Using `instanceOf()` instead of `new IsInstanceOf(InvalidDigestException.class)`.
* Using `stringContainsInOrder()` instead of `new JUnit413StringContains()`.

These changes should fix the error and make the code more readable.