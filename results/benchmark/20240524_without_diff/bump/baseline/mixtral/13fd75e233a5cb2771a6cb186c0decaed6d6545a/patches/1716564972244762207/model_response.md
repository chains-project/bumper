Here's a patch that fixes the error by adding a semicolon at the end of the line causing the issue:

```java
@Test
void failsOnDigestMismatch() {
    final InMemoryStorage storage = new InMemoryStorage();
    final AstoBlobs blobs = new AstoBlobs(
            storage, new DefaultLayout(), new RepoName.Simple("any")
    );
    final String digest = "123";
    blobs.put(
            new CheckedBlobSource(new Content.From("data".getBytes()), new Digest.Sha256(digest))
    ).toCompletableFuture().handle(
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
    ).join();
}
```
The error message suggests that a semicolon is expected at the end of a line. After reviewing the code, I found that the line causing the issue is the one that contains `MatcherAssert.assertThat(...);`. I added a semicolon at the end of that line, and now the code should compile without errors.