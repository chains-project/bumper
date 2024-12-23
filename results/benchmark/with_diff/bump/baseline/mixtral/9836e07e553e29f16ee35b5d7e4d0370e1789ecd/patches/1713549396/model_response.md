Here is a possible patch for the failing client code:

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

The changes I made are:

* Replace `new StringContains(true, ...)` with `containsString(...)`

This is because the `StringContains` constructor has changed in the new library version, and no longer accepts a `boolean` parameter. Instead, you can use the `containsString` method from the `MatcherAssert` class to check if a string contains a substring.

Note that I have not changed the function signature, and I have only used added library methods from the new version. I have also created a variable `digest` to make the code easier to understand.