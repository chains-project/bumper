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
                if (throwable != null) {
                    InvalidDigestException idException = (InvalidDigestException) Throwables.getRootCause(throwable);
                    Assert.assertEquals("Exception message contains calculated digest",
                            "3a6eb0790f39ac87c94f3856b2dd2c5d110e6811602261a9a923d3bb23adc8b7",
                            idException.calculatedDigest().asString());
                    Assert.assertEquals("Exception message contains expected digest",
                            digest, idException.expectedDigest().asString());
                } else {
                    Assert.fail("Exception thrown");
                }
                return CompletableFuture.allOf();
            }
    ).join();
}
```

I changed the `MatcherAssert` calls to `Assert` calls and used `assertEquals` instead of `JUnit413StringContains`. I also added a `calculatedDigest` and `expectedDigest` call to get the actual digest values instead of relying on the error message.