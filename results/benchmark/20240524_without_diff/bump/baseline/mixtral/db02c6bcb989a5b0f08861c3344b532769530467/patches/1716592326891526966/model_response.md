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
                    containsString(
                        "3a6eb0790f39ac87c94f3856b2dd2c5d110e6811602261a9a923d3bb23adc8b7"
                    )
                );
                MatcherAssert.assertThat(
                    "Exception message contains expected digest",
                    Throwables.getRootCause(throwable).getMessage(),
                    containsString(digest)
                );
                return CompletableFuture.allOf();
            }
        ).join();
    }
```
In this patch, I replaced the `StringContains` matcher with the `containsString` matcher from the `org.hamcrest.CoreMatchers` class, which is a more general version of `StringContains` that takes a `CharSequence` instead of a `String`. I also replaced the `new IsNot<>(new IsNull<>())` and `new IsInstanceOf(InvalidDigestException.class)` matchers with `notNullValue()` and `instanceOf(InvalidDigestException.class)` from the same class. These matchers have the same behavior as the original ones but are more concise.

Note that the `MatcherAssert` class is from the `org.junit.Assert` package, which has been deprecated in favor of the `org.hamcrest.MatcherAssert` class, which is used in this patch. This change should not affect the functionality of the test, but it may affect the way the test results are reported.

I hope this helps! Let me know if you have any questions or concerns.