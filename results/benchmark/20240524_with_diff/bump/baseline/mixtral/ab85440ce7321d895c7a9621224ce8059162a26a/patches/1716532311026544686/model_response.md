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
                new IsNot<>(new IsNull<>())
            );
            MatcherAssert.assertThat(
                "Exception is InvalidDigestException",
                Throwables.getRootCause(throwable),
                new IsInstanceOf(InvalidDigestException.class)
            );
            MatcherAssert.assertThat(
                "Exception message contains calculated digest",
                containsString(
                        "3a6eb0790f39ac87c94f3856b2dd2c5d110e6811602261a9a923d3bb23adc8b7"
                )
            );
            MatcherAssert.assertThat(
                "Exception message contains expected digest",
                containsString(digest)
            );
            return CompletableFuture.allOf();
        }
    ).join();
}
```

In this fixed version, I replaced the `StringContains` matcher with the `containsString` method from the JUnit library. The `StringContains` constructor has changed in the new library version, and now it accepts only a single `String` argument. To fix the issue, I replaced the `StringContains` constructor with the `containsString` method, which accepts a `String` argument and checks if it's contained in the given string.