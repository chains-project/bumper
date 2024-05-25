Here is a fixed version of the method that should resolve the error:

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
                        new CoreMatchers.IsNot<>(new CoreMatchers.IsNull<>())
                );
                MatcherAssert.assertThat(
                        "Exception is InvalidDigestException",
                        Throwables.getRootCause(throwable),
                        new CoreMatchers.IsInstanceOf(InvalidDigestException.class)
                );
                MatcherAssert.assertThat(
                        "Exception message contains calculated digest",
                        Throwables.getRootCause(throwable).getMessage(),
                        new CoreMatchers.StringContains.StringContains(
                                "3a6eb0790f39ac87c94f3856b2dd2c5d110e6811602261a9a923d3bb23adc8b7"
                        )
                );
                MatcherAssert.assertThat(
                        "Exception message contains expected digest",
                        Throwables.getRootCause(throwable).getMessage(),
                        new CoreMatchers.StringContains.StringContains(true, digest)
                );
                return CompletableFuture.allOf();
            }
    ).join();
}
```

The changes made include:

1. Replacing the `StringContains` class from the `org.hamcrest.core` package with the `StringContains` class from the `org.hamcrest` package.
2. Replacing the `IsNot` and `IsNull` classes from the `org.hamcrest.core` package with the `IsNot` and `IsNull` classes from the `org.hamcrest` package.
3. Replacing the `IsInstanceOf` class from the `org.hamcrest.core` package with the `IsInstanceOf` class from the `org.hamcrest` package.
4. Adding the `CoreMatchers` class from the `org.hamcrest` package to the method.

These changes should resolve the error and allow the method to compile and run successfully.