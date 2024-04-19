Here is a possible patch for the failing code:
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
                String message = throwable.getMessage();
                MatcherAssert.assertThat(
                    "Exception message contains calculated digest",
                    message,
                    stringContains("3a6eb0790f39ac87c94f3856b2dd2c5d110e6811602261a9a923d3bb23adc8b7")
                );
                MatcherAssert.assertThat(
                    "Exception message contains expected digest",
                    message,
                    stringContains(digest)
                );
                return CompletableFuture.allOf();
            }
        ).join();
    }
```
The changes I made are:

* I replaced the `new IsNot<>(new IsNull<>())` matcher with `notNullValue()`
* I replaced the `new IsInstanceOf(InvalidDigestException.class)` matcher with `instanceOf(InvalidDigestException.class)`
* I replaced the `new StringContains(true, "3a6eb0790f39ac87c94f3856b2dd2c5d110e6811602261a9a923d3bb23adc8b7")` matcher with `stringContains("3a6eb0790f39ac87c94f3856b2dd2c5d110e6811602261a9a923d3bb23adc8b7")`
* I replaced the `new StringContains(true, "123")` matcher with `stringContains("123")`

These changes remove the need for the `boolean` argument in the `StringContains` constructor, which was causing the error message. The new matchers have the same behavior as the old ones, but use the new library methods introduced in the updated library version.