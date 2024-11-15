Here's a possible patch for the given client code:

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
                assertNotNull(
                        "Exception thrown",
                        throwable
                );
                assertTrue(
                        "Exception is InvalidDigestException",
                        throwable instanceof InvalidDigestException
                );
                assertTrue(
                        "Exception message contains calculated digest",
                        throwable.getMessage().contains(
                                "3a6eb0790f39ac87c94f3856b2dd2c5d110e6811602261a9a923d3bb23adc8b7"
                        )
                );
                assertTrue(
                        "Exception message contains expected digest",
                        throwable.getMessage().contains(digest)
                );
                return CompletableFuture.allOf();
            }
    ).join();
}
```

The patch replaces the `MatcherAssert.assertThat` calls with JUnit 4.x assert methods (`assertNotNull`, `assertTrue`). It also replaces the `JUnit413StringContains` matcher with the `contains` method of the `String` class.

Note that this patch assumes that the `MatcherAssert` and `JUnit413StringContains` classes are not available in the classpath, while the JUnit 4.x assert methods are available. If this is not the case, a different patch may be needed.