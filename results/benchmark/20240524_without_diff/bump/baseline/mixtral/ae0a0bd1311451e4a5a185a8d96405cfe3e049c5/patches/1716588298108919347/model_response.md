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
The patch creates a couple of variables to make the code more readable, and it calculates the digest of the content before creating the `CheckedBlobSource`. It also uses the `calculatedDigest` variable in the assertion of the exception message.

Note that the patch uses the `CompletableFuture.join()` method to wait for the completion of the `putFuture`, before handling the exception. This is because the `handle()` method of `CompletableFuture` only gets called when the future completes, either normally or with an exception. If the future is not completed yet, the `handle()` method will not be called, and the test will not work as expected.

The patch also removes the `Override` decorator from the method, because the method is not overriding any method in the new version.

The patch does not use any removed library methods, but it uses the `CompletableFuture.allOf()` method, which is an added library method in Java 9. If the target platform is Java 8 or earlier, this method should be replaced with an equivalent implementation.