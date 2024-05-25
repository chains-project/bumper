Here's the fixed version of the `failsOnDigestMismatch` method:

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

In this version, I replaced the `new IsNot<>(new IsNull<>())` and `new IsInstanceOf(class)` with `new CoreMatchers.notNullValue()` and `new InstanceOf(class)` respectively, since the `IsNot` and `IsInstanceOf` classes are no longer available. Also, I replaced the `StringContains` constructor with the `ContainsString` method, since the constructor is not available.