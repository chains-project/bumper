Here is a possible patch for the failing client code:
```java
@Test
void failsOnDigestMismatch() {
    InMemoryStorage storage = new InMemoryStorage();
    AstoBlobs blobs = new AstoBlobs(
        storage, new DefaultLayout(), new RepoName.Simple("any")
    );
    String digest = "123";
    blobs.put(
        new CheckedBlobSource(new Content.From("data".getBytes()), new Digest.Sha256(digest))
    )
    .thenAcceptAsync(blob -> {
        InvalidDigestException ex = Assertions.assertThrows(
            InvalidDigestException.class,
            () -> blobs.get(blob.content().digest())
        );
        assertTrue(ex.getMessage().contains("3a6eb0790f39ac87c94f3856b2dd2c5d110e6811602261a9a923d3bb23adc8b7"));
        assertTrue(ex.getMessage().contains(digest));
    })
    .join();
}
```
The patch removes the `handle` method and uses `thenAcceptAsync` instead, which allows to handle the exception more directly. It also uses JUnit 5's `Assertions.assertThrows` method to assert that an exception of the expected type is thrown. Finally, it simplifies the assertions by using `assertTrue` and `contains` instead of `MatcherAssert.assertThat` and `allOf`.