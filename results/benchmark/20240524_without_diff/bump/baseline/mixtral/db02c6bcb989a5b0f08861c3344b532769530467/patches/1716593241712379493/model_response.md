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
    final Digest expectedDigest = new Digest.Sha256(digest);
    final CheckedBlobSource checkedBlobSource = new CheckedBlobSource(content, expectedDigest);
    blobs.put(checkedBlobSource)
         .toCompletableFuture()
         .handle(
             (blob, throwable) -> {
                 MatcherAssert.assertThat(throwable, new IsNot<>(new IsNull<>()));
                 MatcherAssert.assertThat(
                     Throwables.getRootCause(throwable),
                     new IsInstanceOf(InvalidDigestException.class)
                 );
                 MatcherAssert.assertThat(
                     Throwables.getRootCause(throwable).getMessage(),
                     new JUnit413StringContains(
                         calculatedDigest.toString()
                     )
                 );
                 MatcherAssert.assertThat(
                     Throwables.getRootCause(throwable).getMessage(),
                     new JUnit413StringContains(digest)
                 );
                 return CompletableFuture.allOf();
             }
         )
         .join();
}
```
The changes I made are:

* I created a `content` variable to avoid calling `getBytes()` multiple times.
* I created `calculatedDigest` and `expectedDigest` variables to avoid creating them multiple times and make the code more readable.
* I added a `checkedBlobSource` variable to make the code more readable.
* I replaced the hardcoded digest value in the `JUnit413StringContains` matcher with a variable.
* I added a `toString()` call on `calculatedDigest` in the `JUnit413StringContains` matcher.

These changes should fix the error and make the code more readable and maintainable.