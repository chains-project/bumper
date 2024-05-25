Here's a fixed version of the `failsOnDigestMismatch` method:
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
                    new InstanceOf(InvalidDigestException.class)
                );
                MatcherAssert.assertThat(
                    "Exception message contains calculated digest",
                    Throwables.getRootCause(throwable).getMessage(),
                    new StringContains(
                        "3a6eb0790f39ac87c94f3856b2dd2c5d110e6811602261a9a923d3bb23adc8b7"
                    )
                );
                MatcherAssert.assertThat(
                    "Exception message contains expected digest",
                    Throwables.getRootCause(throwable).getMessage(),
                    new StringContains(digest)
                );
                return CompletableFuture.allOf();
            }
        ).join();
    }
```
The issue was caused by the use of `new StringContains(true, ...)` in the original code. The first argument to `StringContains` should be a boolean indicating whether the contained string should be matched as a regular expression. In this case, a simple substring match is desired, so the argument should be `false` or simply omitted.

In this fixed version, I removed the `true` argument for all `StringContains` matchers. This should resolve the compilation error and make the test pass.