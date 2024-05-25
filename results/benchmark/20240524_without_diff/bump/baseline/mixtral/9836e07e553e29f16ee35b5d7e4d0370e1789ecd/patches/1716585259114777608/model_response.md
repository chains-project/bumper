Here's a possible patch for the failing client code:

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
                    new IsInstanceOf(InvalidDigestException.class)
                );
                MatcherAssert.assertThat(
                    "Exception message contains calculated digest",
                    throwable.getMessage(),
                    new StringContains(
                        "3a6eb0790f39ac87c94f3856b2dd2c5d110e6811602261a9a923d3bb23adc8b7"
                    )
                );
                MatcherAssert.assertThat(
                    "Exception message contains expected digest",
                    throwable.getMessage(),
                    new StringContains(digest)
                );
                return CompletableFuture.allOf();
            }
        ).join();
    }
```

The changes made are:

* Replace `new IsNot<>(new IsNull<>())` with `new IsInstanceOf(InvalidDigestException.class)` in the first `MatcherAssert.assertThat()` call.
* Replace `Throwables.getRootCause(throwable)` with `throwable` in the second and third `MatcherAssert.assertThat()` calls.
* Replace `StringContains(true, ...)` with `StringContains(...)` in the second and third `MatcherAssert.assertThat()` calls.

The `MatcherAssert.assertThat()` method accepts a `Matcher` object as its second argument. `IsNot<>(new IsNull<>())` is a matcher that matches if the given object is not null. However, it seems that the `StringContains` matcher has been changed to no longer accept a `boolean` argument indicating whether the match should be case-sensitive or not. Instead, it now always performs a case-insensitive match. Therefore, we can simply remove the `true` argument from the `StringContains` matchers.

The `Throwables.getRootCause()` method has been removed, so we need to replace it with the original throwable object.

The `IsInstanceOf` matcher can be used instead of `IsNot<>(new IsNull<>())` to check if the throwable is an instance of `InvalidDigestException`.