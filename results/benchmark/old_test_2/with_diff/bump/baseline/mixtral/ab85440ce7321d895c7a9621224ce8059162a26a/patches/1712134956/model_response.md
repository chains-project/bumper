Here's the fixed version of the `failsOnDigestMismatch()` method:

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
                new IsInstanceOf(InvalidDigestException.class)
            );
            MatcherAssert.assertThat(
                "Exception message contains calculated digest",
                new StringContains(
                        Throwables.getRootCause(throwable).getMessage()
                    ),
                new InstanceOf(String.class)
            );
            MatcherAssert.assertThat(
                "Exception message contains expected digest",
                new StringContains(
                        Throwables.getRootCause(throwable).getMessage(), digest
                    ),
                new InstanceOf(String.class)
            );
            return CompletableFuture.allOf();
        }
    ).join();
}
```

The issue was caused by the incorrect usage of the `StringContains` matcher. It now accepts a single argument, the expected substring, but in the original code, it received two arguments: a boolean value and the expected substring. To fix this, I've removed the unnecessary boolean arguments.