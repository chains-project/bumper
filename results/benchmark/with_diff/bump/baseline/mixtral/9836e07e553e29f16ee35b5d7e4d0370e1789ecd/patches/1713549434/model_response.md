Here is the proposed patch:

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

* Replace `new StringContains(true, "3a6eb0790f39ac87c94f3856b2dd2c5d110e6811602261a9a923d3bb23adc8b7")` with `containsString("3a6eb0790f39ac87c94f3856b2dd2c5d110e6811602261a9a923d3bb23adc8b7")`
* Replace `new StringContains(true, digest)` with `containsString(digest)`

The reason for these changes is that the `StringContains` constructor has been changed in the new library version to only accept a single argument, instead of two. The `containsString` method can be used instead to check if a string contains a substring.