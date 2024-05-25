Here's the fixed version of the failing method:

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
                new CoreMatchers.instanceOf(InvalidDigestException.class)
            );
            MatcherAssert.assertThat(
                "Exception message contains calculated digest",
                throwable.getMessage(),
                new CoreMatchers.containsString(
                        "3a6eb0790f39ac87c94f3856b2dd2c5d110e6811602261a9a923d3bb23adc8b7"
                )
            );
            MatcherAssert.assertThat(
                "Exception message contains expected digest",
                throwable.getMessage(),
                new CoreMatchers.containsString(digest)
            );
            return CompletableFuture.allOf();
        }
    ).join();
}
```

I replaced the `StringContains` class from `org.hamcrest.core` with the `containsString` method from `CoreMatchers` in the same package.