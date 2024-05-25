Here's a fixed version of the method that should resolve the error:

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
                throwable,
                new InstanceOf(InvalidDigestException.class)
            );
            MatcherAssert.assertThat(
                "Exception message contains calculated digest",
                throwable.getMessage(),
                new StringContains.ContainsString("3a6eb0790f39ac87c94f3856b2dd2c5d110e6811602261a9a923d3bb23adc8b7")
            );
            MatcherAssert.assertThat(
                "Exception message contains expected digest",
                throwable.getMessage(),
                new StringContains.ContainsString(digest)
            );
            return CompletableFuture.allOf();
        }
    ).join();
}
```

The changes made include:

* Replacing `new IsNot<>(new IsNull<>())` with `new CoreMatchers.notNullValue()`.
* Replacing `new IsInstanceOf(InvalidDigestException.class)` with `new InstanceOf(InvalidDigestException.class)`.
* Replacing `new StringContains(true, "substring")` with `new StringContains.ContainsString("substring")`.
* Importing `org.hamcrest.CoreMatchers.*` and `org.hamcrest.StringContains.*` to use their static methods.

These changes should resolve the error by using the appropriate static methods from the Hamcrest library.