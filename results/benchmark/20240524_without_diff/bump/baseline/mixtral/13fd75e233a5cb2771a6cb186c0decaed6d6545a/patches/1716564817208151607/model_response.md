Here's a suggested patch for the failing client code:

```java
@Test
void failsOnDigestMismatch() {
    final InMemoryStorage storage = new InMemoryStorage();
    final AstoBlobs blobs = new AstoBlobs(
            storage, new DefaultLayout(), new RepoName.Simple("any")
    );
    final String digest = "123";
    CheckedBlobSource checkedBlobSource = new CheckedBlobSource(
            new Content.From("data".getBytes()), new Digest.Sha256(digest));
    Blob blob = blobs.put(checkedBlobSource);
    CompletableFuture<Void> completableFuture = blob.toCompletableFuture();
    completableFuture.handle(
            (result, throwable) -> {
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
                                        "3a6eb0790f39ac87c94f3856b2dd2c5d110e6811602261a9a923d3bb23adc8b7"
                                ),
                                stringContains(digest)
                        )
                );
                return CompletableFuture.allOf();
            }
    );
    completableFuture.join();
}
```

In this patch, I created a `CheckedBlobSource` variable to make the code easier to read. I also explicitly assigned the result of the `blobs.put()` method to a `Blob` variable and the result of `blob.toCompletableFuture()` to a `CompletableFuture` variable. These changes make the code more readable and easier to understand.