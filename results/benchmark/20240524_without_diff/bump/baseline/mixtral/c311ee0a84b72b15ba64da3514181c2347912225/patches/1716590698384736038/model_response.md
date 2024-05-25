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
The changes I made are:

* Replace `new IsNot<>(new IsNull<>())` with `new IsInstanceOf(InvalidDigestException.class)` in the first `MatcherAssert.assertThat` call, because the error message suggests that the constructor `StringContains(Matcher<T>)` is missing.
* Replace `Throwables.getRootCause(throwable)` with `throwable` in the second and third `MatcherAssert.assertThat` calls, because the error message suggests that the constructor `StringContains(String)` is missing.

Note that I cannot be sure that these changes will fix the error, because I don't know the exact cause of the error. However, they are based on the information provided and should at least make the code compile.