Here is a fixed version of the failing method:
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
                new CoreMatchers.notNullValue()
            );
            MatcherAssert.assertThat(
                "Exception is InvalidDigestException",
                Throwables.getRootCause(throwable),
                new InstanceOf(InvalidDigestException.class)
            );
            MatcherAssert.assertThat(
                "Exception message contains calculated digest",
                Throwables.getRootCause(throwable).getMessage(),
                new StringContains.ContainsString(
                        "3a6eb0790f39ac87c94f3856b2dd2c5d110e6811602261a9a923d3bb23adc8b7"
                )
            );
            MatcherAssert.assertThat(
                "Exception message contains expected digest",
                Throwables.getRootCause(throwable).getMessage(),
                new StringContains.ContainsString(digest)
            );
            return CompletableFuture.allOf();
        }
    ).join();
}
```
The changes made are:

* Replace `new IsNot<>(new IsNull<>())` with `new CoreMatchers.notNullValue()`
* Replace `new IsInstanceOf(InvalidDigestException.class)` with `new InstanceOf(InvalidDigestException.class)`
* Replace `new StringContains(true, "3a6eb0790f39ac87c94f3856b2dd2c5d110e6811602261a9a923d3bb23adc8b7")` with `new StringContains.ContainsString("3a6eb0790f39ac87c94f3856b2dd2c5d110e6811602261a9a923d3bb23adc8b7")`
* Replace `new StringContains(true, digest)` with `new StringContains.ContainsString(digest)`

These changes are necessary because the `StringContains` constructor has been removed and replaced with a `ContainsString` method in the `StringContains` class. The `IsNot`, `IsInstanceOf`, and `InstanceOf` classes have also been removed and replaced with `notNullValue`, `IsInstanceOf`, and `InstanceOf` methods in the `CoreMatchers` class.