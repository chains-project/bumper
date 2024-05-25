Here's the fixed version of the `failsOnDigestMismatch()` method:

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

The following changes were made:

1. Replaced `new IsNot<>(new IsNull<>())` with `new CoreMatchers.notNullValue()`.
2. Replaced `new IsInstanceOf(InvalidDigestException.class)` with `new InstanceOf(InvalidDigestException.class)`.
3. Replaced `new StringContains(true, ...)` with `new StringContains.ContainsString(...)`.

These changes are based on the assumption that the issue is caused by the removal of the `StringContains` constructor that accepts a boolean parameter in the version of Hamcrest you are using. The replacement methods are added in Hamcrest 2.2 and later. If you are using an earlier version of Hamcrest, you may need to upgrade or use a different approach to achieve the desired assertions.