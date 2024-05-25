Here is a fixed version of the code that should resolve the error:

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
                new CoreMatchers.stringContains(
                        "3a6eb0790f39ac87c94f3856b2dd2c5d110e6811602261a9a923d3bb23adc8b7"
                )
            );
            MatcherAssert.assertThat(
                "Exception message contains expected digest",
                throwable.getMessage(),
                new CoreMatchers.stringContains(digest)
            );
            return CompletableFuture.allOf();
        }
    ).join();
}
```

The issue was caused by the use of the deprecated `StringContains` class from the `org.hamcrest.core` package. I replaced it with the `stringContains` method from the `CoreMatchers` class in the same package. Additionally, I replaced the `new IsNot<>(new IsNull<>())` and `new IsInstanceOf(InvalidDigestException.class)` with `notNullValue()` and `instanceOf(InvalidDigestException.class)` respectively.