Here is a possible patch for the code you provided:
```java
@Test
void failsOnDigestMismatch() {
    final InMemoryStorage storage = new InMemoryStorage();
    final AstoBlobs blobs = new AstoBlobs(
        storage, new DefaultLayout(), new RepoName.Simple("any")
    );
    final String digest = "123";
    final Content content = new Content.From("data".getBytes());
    final Digest calculatedDigest = new Digest.Sha256(
        Hash.sha256().asHex(content.data())
    );
    blobs.put(new CheckedBlobSource(content, new Digest.Sha256(digest)))
        .toCompletableFuture()
        .handle(
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
                        new CoreMatchers.StringContains(calculatedDigest.asString()),
                        new CoreMatchers.StringContains(digest)
                    )
                );
                return CompletableFuture.allOf();
            }
        ).join();
}
```
The main change I made is to calculate the expected digest of the content being uploaded, and use that in the assertions instead of a hard-coded string. I also added a `Content` variable to make the code a bit more readable.

I hope this helps! Let me know if you have any questions.