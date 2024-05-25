Here's a fixed version of the method that should resolve the error:

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

I replaced the `StringContains` constructor with the `stringContains` method from Hamcrest, which takes a single argument. I also replaced the `new IsNot<>(new IsNull<>())` and `new IsInstanceOf(InvalidDigestException.class)` constructors with the `notNullValue()` and `instanceOf(InvalidDigestException.class)` methods from Hamcrest. Finally, I replaced the `new StringContains(true, ...)` constructor with the `allOf` method from Hamcrest, which takes a vararg of matchers and checks that all of them match.