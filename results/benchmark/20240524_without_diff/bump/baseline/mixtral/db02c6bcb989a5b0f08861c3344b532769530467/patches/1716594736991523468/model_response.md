Here's a possible patch for the given code:

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
                assertTrue(throwable != null);
                assertTrue(throwable instanceof InvalidDigestException);
                assertTrue(throwable.getMessage().contains("3a6eb0790f39ac87c94f3856b2dd2c5d110e6811602261a9a923d3bb23adc8b7"));
                assertTrue(throwable.getMessage().contains(digest));
                return CompletableFuture.allOf();
            }
    ).join();
}
```

In this patch, I replaced the `MatcherAssert.assertThat` statements with `assertTrue` statements and used the `contains` method instead of the custom `JUnit413StringContains` matcher. This should fix the compilation error.