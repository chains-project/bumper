Here is a proposed patch for the failing client code:
```java
@Test
void failsOnDigestMismatch() {
    final InMemoryStorage storage = new InMemoryStorage();
    final AstoBlobs blobs = new AstoBlobs(
        storage, new DefaultLayout(), new RepoName.Simple("any")
    );
    final String digest = "123";
    CheckedBlobSource checkedBlobSource = new CheckedBlobSource(
        new Content.From("data".getBytes()), new Digest.Sha256(digest)
    );
    CompletableFuture<Blob> future = blobs.put(checkedBlobSource);
    future.handle(
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
                        "3a6eb0790f39ac87c94f3856b2dd2c5d110e6811602261a9a923d3bb23adc8b7"
                    ),
                    stringContains(digest)
                )
            )
            );
            return CompletableFuture.allOf();
        }
    );
    future.join();
}
```
The main change made to the code is to declare the `CheckedBlobSource` variable on its own line and assign it the result of the `new CheckedBlobSource` constructor call, before passing it as an argument to the `blobs.put` method. This allows the method to complete its execution before attempting to handle its result, which should resolve the reported error.