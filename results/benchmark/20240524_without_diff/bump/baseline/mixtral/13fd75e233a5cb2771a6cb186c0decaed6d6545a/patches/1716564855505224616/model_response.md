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
    ).exceptionally(throwable -> {
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
        return null;
    });
}
```

The main change is the use of `exceptionally` instead of `handle` for the `CompletableFuture`. The `handle` method expects a success handler in addition to the failure handler, which is not provided in the original code. In this case, you can use `exceptionally` to handle only the failure case.