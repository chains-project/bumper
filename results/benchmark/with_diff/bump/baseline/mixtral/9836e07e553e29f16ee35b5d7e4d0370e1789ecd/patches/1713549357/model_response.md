Here is the proposed patch to fix the error:
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
                    stringContains("3a6eb0790f39ac87c94f3856b2dd2c5d110e6811602261a9a923d3bb23adc8b7")
                );
                MatcherAssert.assertThat(
                    "Exception message contains expected digest",
                    Throwables.getRootCause(throwable).getMessage(),
                    stringContains(digest)
                );
                return CompletableFuture.allOf();
            }
        ).join();
    }
```
The changes I made are:

* Replace `new IsNot<>(new IsNull<>())` with `notNullValue()`
* Replace `new IsInstanceOf(InvalidDigestException.class)` with `instanceOf(InvalidDigestException.class)`
* Replace `new StringContains(true, "3a6eb0790f39ac87c94f3856b2dd2c5d110e6811602261a9a923d3bb23adc8b7")` with `stringContains("3a6eb0790f39ac87c94f3856b2dd2c5d110e6811602261a9a923d3bb23adc8b7")`
* Replace `new StringContains(true, digest)` with `stringContains(digest)`