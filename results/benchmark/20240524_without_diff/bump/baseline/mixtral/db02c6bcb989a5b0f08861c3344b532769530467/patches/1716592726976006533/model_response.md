Here's the proposed patch for the failing client code:

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
                        new CoreMatchers.notNullValue()
                );
                MatcherAssert.assertThat(
                        "Exception is InvalidDigestException",
                        throwable,
                        new InstanceOf(InvalidDigestException.class)
                );
                MatcherAssert.assertThat(
                        "Exception message contains calculated digest",
                        throwable.getMessage(),
                        new StringContains.ContainsString("3a6eb0790f39ac87c94f3856b2dd2c5d110e6811602261a9a923d3bb23adc8b7")
                );
                MatcherAssert.assertThat(
                        "Exception message contains expected digest",
                        throwable.getMessage(),
                        new StringContains.ContainsString(digest)
                );
                return CompletableFuture.allOf();
            }
    ).join();
}
```

Changes made:

* Replaced `new IsNot<>(new IsNull<>())` with `new CoreMatchers.notNullValue()`
* Replaced `new IsInstanceOf(InvalidDigestException.class)` with `new InstanceOf(InvalidDigestException.class)`
* Replaced `new StringContains(true, "3a6eb0790f39ac87c94f3856b2dd2c5d110e6811602261a9a923d3bb23adc8b7")` with `new StringContains.ContainsString("3a6eb0790f39ac87c94f3856b2dd2c5d110e6811602261a9a923d3bb23adc8b7")`
* Replaced `new StringContains(true, digest)` with `new StringContains.ContainsString(digest)`