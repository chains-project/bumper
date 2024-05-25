Here's a fixed version of the failing method:

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
                notNullValue()
            );
            MatcherAssert.assertThat(
                "Exception is InvalidDigestException",
                Throwables.getRootCause(throwable),
                instanceOf(InvalidDigestException.class)
            );
            MatcherAssert.assertThat(
                "Exception message contains calculated digest",
                Throwables.getRootCause(throwable).getMessage(),
                allOf(
                    stringContains(
                        "3a6eb0790f39ac87c94f3856b2dd2c5d110e6811602261a9a923d3bb23adc8b7"
                    ),
                    stringContains(digest)
                )
            );
            return CompletableFuture.allOf();
        }
    ).join();
}
```

I've replaced the `new IsNot<>(new IsNull<>())` and `new StringContains(true, ...)` with `notNullValue()` and `stringContains(...)`, respectively.

The `MatcherAssert.assertThat` method can take a matcher as the second argument, and `notNullValue()` and `stringContains(...)` are matchers provided by Hamcrest.

The `StringContains` constructor with two arguments has been removed, so we can't use it anymore. Instead, we can use the `stringContains` matcher provided by Hamcrest.

The `allOf` matcher is used to combine the two `stringContains` matchers into one.

Note that `MatcherAssert` and `Throwables` come from the Hamcrest and Google Guava libraries, respectively, so make sure these libraries are included in your project.