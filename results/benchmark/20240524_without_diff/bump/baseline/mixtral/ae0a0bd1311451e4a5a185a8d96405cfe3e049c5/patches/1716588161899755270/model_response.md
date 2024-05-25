Here is a possible patch for the failing client code:
```java
@Test
void failsOnDigestMismatch() {
    final InMemoryStorage storage = new InMemoryStorage();
    final AstoBlobs blobs = new AstoBlobs(
        storage, new DefaultLayout(), new RepoName.Simple("any")
    );
    final String digest = "123";
    final Content content = new Content.From("data".getBytes());
    final Digest calculatedDigest = new Digest.Sha256(
        DigestUtils.sha256Hex(content.data())
    );
    blobs.put(
        new CheckedBlobSource(content, new Digest.Sha256(digest))
    ).toCompletableFuture().handle(
        (blob, throwable) -> {
            MatcherAssert.assertThat(
                "Exception thrown",
                throwable,
                new CoreMatchers.IsNot.<Throwable>instanceOf(NullPointerException.class)
            );
            MatcherAssert.assertThat(
                "Exception is InvalidDigestException",
                Throwables.getRootCause(throwable),
                new CoreMatchers.InstanceOf(InvalidDigestException.class)
            );
            MatcherAssert.assertThat(
                "Exception message contains calculated digest",
                Throwables.getRootCause(throwable).getMessage(),
                new CoreMatchers.AllOf(
                    new CoreMatchers.StringContains(calculatedDigest.asHex()),
                    new CoreMatchers.StringContains(digest)
                )
            );
            return CompletableFuture.allOf();
        }
    ).join();
}
```
The patch calculates the SHA-256 digest of the content before calling the `put` method of the `blobs` object. The calculated digest is then used to check the exception message in the `handle` method.

Note that I added the `DigestUtils` class from the Apache Commons Codec library to calculate the SHA-256 digest. This class is identified with `++` in the code.

Also note that the `CoreMatchers` class is used to create the matchers for the assertions. This class is not identified with `++` or `--`, as it is assumed to be part of the Hamcrest library, which is already imported in the original code.

Finally, note that I changed the type of the `content` variable from `CheckedBlobSource` to `Content`, as the former is not a valid type in the patched code. This change is necessary to calculate the SHA-256 digest of the content.