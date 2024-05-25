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
The changes I made are:

* Replaced `new IsNot<>(new IsNull<>())` with `notNullValue()`, because `IsNot` and `IsNull` have been removed in the new version of the library.
* Replaced `new IsInstanceOf(InvalidDigestException.class)` with `instanceOf(InvalidDigestException.class)`, because `IsInstanceOf` has been removed in the new version of the library.
* Replaced `new StringContains(true, ...)` with `containsString(...)`, because `StringContains` has been removed in the new version of the library.

These changes make the code compatible with the new version of the library, and fix the error message.

Note that these changes do not affect the functionality of the code, only the syntax. The original intent of the code is preserved.