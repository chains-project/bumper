Here is a fixed version of the code:
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
                    new NotNullValue<>());
                MatcherAssert.assertThat(
                    "Exception is InvalidDigestException",
                    throwable,
                    new InstanceOf(InvalidDigestException.class));
                MatcherAssert.assertThat(
                    "Exception message contains calculated digest",
                    throwable.getMessage(),
                    new StringContains(
                        "3a6eb0790f39ac87c94f3856b2dd2c5d110e6811602261a9a923d3bb23adc8b7"
                    ));
                MatcherAssert.assertThat(
                    "Exception message contains expected digest",
                    throwable.getMessage(),
                    new StringContains(digest));
                return CompletableFuture.allOf();
            }
        ).join();
    }
```
The changes made to the code are:

* Replace `new IsNot<>(new IsNull<>())` with `new NotNullValue<>()` to create a matcher that matches if the given value is not null.
* Replace `new IsInstanceOf(InvalidDigestException.class)` with `new InstanceOf(InvalidDigestException.class)` to create a matcher that matches if the given value is an instance of the given class.
* Replace `new StringContains(true, "3a6eb0790f39ac87c94f3856b2dd2c5d110e6811602261a9a923d3bb23adc8b7")` with `new StringContains("3a6eb0790f39ac87c94f3856b2dd2c5d110e6811602261a9a923d3bb23adc8b7")` to create a matcher that matches if the given string contains the specified substring.
* Replace `new StringContains(true, digest)` with `new StringContains(digest)` to create a matcher that matches if the given string contains the specified substring.

These changes should fix the error in the code.