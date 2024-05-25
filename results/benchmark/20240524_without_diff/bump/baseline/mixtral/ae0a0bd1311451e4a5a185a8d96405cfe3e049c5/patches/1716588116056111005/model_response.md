Here is a fixed version of the method that should resolve the error:

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
                new CoreMatchers.IsNot.<Throwable>instanceOf(NullPointerException.class)
            );
            MatcherAssert.assertThat(
                "Exception is InvalidDigestException",
                Throwables.getRootCause(throwable),
                new CoreMatchers.InstanceOf(InvalidDigestException.class)
            );
            MatcherAssert.assertThat(
                "Exception message contains calculated digest",
                Throwables.getRootCause(throwable).getMessage(),
                new CoreMatchers.AllOf(
                    new CoreMatchers.StringContains("3a6eb0790f39ac87c94f3856b2dd2c5d110e6811602261a9a923d3bb23adc8b7"),
                    new CoreMatchers.StringContains(digest)
                )
            );
            return CompletableFuture.allOf();
        }
    ).join();
}
```

I replaced the offending `StringContains` matcher with a new one that uses the `AllOf` matcher to check that the exception message contains both the calculated and expected digests. I also changed the `IsNot` and `InstanceOf` matchers to use the `CoreMatchers` class, which is part of the Hamcrest library and provides the same functionality as the removed `MatcherAssert` methods.