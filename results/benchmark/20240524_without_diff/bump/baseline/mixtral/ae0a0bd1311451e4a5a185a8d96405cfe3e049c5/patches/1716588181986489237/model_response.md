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
    final Digest calculatedDigest = new Digest.Sha256(digest);
    final CheckedBlobSource checkedBlobSource = new CheckedBlobSource(content, calculatedDigest);
    final CompletableFuture<Blob> putFuture = blobs.put(checkedBlobSource);
    putFuture.handle(
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
                    new CoreMatchers.StringContains(calculatedDigest.value()),
                    new CoreMatchers.StringContains(digest)
                )
            );
            return CompletableFuture.allOf();
        }
    );
    putFuture.join();
}
```
The patch introduces a few changes:

* It creates a separate variable for the `Content` object, so that it can be reused in the `CheckedBlobSource` constructor.
* It creates a separate variable for the `Digest` object, so that it can be used in the `MatcherAssert` for the exception message.
* It creates a separate variable for the `CheckedBlobSource` object, so that it can be used in the `blobs.put()` method call.
* It moves the `putFuture.join()` call after the `handle()` method call, so that the future can be waited for after the exception handling.
* It uses the `calculatedDigest.value()` method instead of the hardcoded digest value in the `MatcherAssert` for the exception message.

These changes should fix the error message and make the code more readable and maintainable.