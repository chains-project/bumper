Here's a possible patch for the failing code:

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
                    throwable,
                    instanceOf(InvalidDigestException.class)
                );
                MatcherAssert.assertThat(
                    "Exception message contains calculated digest",
                    throwable.getMessage(),
                    containsString(
                        "3a6eb0790f39ac87c94f3856b2dd2c5d110e6811602261a9a923d3bb23adc8b7"
                    )
                );
                MatcherAssert.assertThat(
                    "Exception message contains expected digest",
                    throwable.getMessage(),
                    containsString(digest)
                );
                return CompletableFuture.allOf();
            }
        ).join();
    }
```

The changes are:

* Replace `new IsNot<>(new IsNull<>())` with `notNullValue()`.
* Replace `new IsInstanceOf(InvalidDigestException.class)` with `instanceOf(InvalidDigestException.class)`.
* Replace `new StringContains(true, "3a6eb0790f39ac87c94f3856b2dd2c5d110e6811602261a9a923d3bb23adc8b7")` with `containsString("3a6eb0790f39ac87c94f3856b2dd2c5d110e6811602261a9a923d3bb23adc8b7")`.
* Replace `new StringContains(true, digest)` with `containsString(digest)`.

These changes use the new library methods `notNullValue()`, `instanceOf()`, and `containsString()` instead of the removed library methods `IsNot.IsNull()`, `IsInstanceOf.InstanceOf()`, and `StringContains.StringContains()`.