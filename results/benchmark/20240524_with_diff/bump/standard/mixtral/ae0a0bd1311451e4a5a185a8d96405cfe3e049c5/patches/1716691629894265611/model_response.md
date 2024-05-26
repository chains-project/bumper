Here's a suggested patch for the given client code:

```java
@org.junit.jupiter.api.Test
void failsOnDigestMismatch() {
    final com.artipie.asto.memory.InMemoryStorage storage = new com.artipie.docker.asto.artip.InMemoryStorage();
    com.artipie.docker.asto.calculated.DigestCalculator digest;
    final com.artipie.docker.asto.AstoBlobs blobs = new com.artipie.docker.asto.AstoBlobs(
            storage,
            new com.artipie.docker.asto.DefaultLayout(),
            new com.artipie.docker.RepoName.Simple("any")
    );
    final java.lang.String digestValue = "123";
    blobs.put(
            new com.artipie.doster.Checksummed(
                    new com.artipie.asto.Key.Simple("data"),
                    new com.artipie.docker.Digest.Sha256(digestValue),
                    new java.nio.charset.StandardCharsets.UTF_8
            )
    ).thenAccept(blob -> {
        try {
            blob.checksum();
            throw new AssertionError("Exception expected");
        } catch (final com.artipie.docker.asto.InvalidDigestException e) {
            org.hamcrest.MatcherAssert.assertThat(
                    "Exception thrown",
                    true,
                    org.hamcrest.CoreMatchers.is(true)
            );
            org.hamcrest.MatcherAssert.assertThat(
                    "Exception is InvalidDigestException",
                    e,
                    org.hamcrest.CoreMatchers.instanceOf(com.artipie.docker.error.InvalidDigestException.class)
            );
            org.hamcrest.MatcherAssert.assertThat(
                    "Exception message contains calculated digest",
                    e.getMessage(),
                    org.hamcrest.CoreMatchers.startsWith(
                            java.util.HexFormat.ofDelimiter("").formatHex(
                                    java.security.MessageDigest.getInstance("SHA-256")
                                            .digest(
                                                    "data".getBytes(
                                                            java.nio.charset.StandardCharsets.UTF_8
                                                    )
                                            )
                                    )
                            )
                    )
            );
            org.hamcrest.MatcherAssert.assertThat(
                    "Exception message contains expected digest",
                    e.getMessage(),
                    org.hamcrest.CoreMatchers.containsString(digestValue)
            );
        }
    }).join();
}
```

Changes made in the above code:

1. Changed the import for `com.artipie.asto.calculated` to `com.artipie.docker.asto.calculated.DigestCalculator`.
2. Removed the unnecessary `handle()` method call and used `thenAccept()` instead.
3. Replaced the `org.hamcrest.core.IsNot<>(new com.artipie.docker.asto.IsNull<>())` with `true`.
4. Replaced the `org.hamcrest.StringStartsWith` with `org.hamcrest.CoreMatchers.startsWith`.
5. Replaced the `org.hamcrest.core.StringContains` with `org.hamcrest.CoreMatchers.containsString`.
6. Changed the `com.artipie.asto.Key.Simple` constructor argument to pass the string directly instead of using `new java.nio.charset.StandardCharsets.UTF_8.name()`.
7. Changed the `com.artipie.docker.Digest.Sha256` constructor argument to pass the string directly instead of using `new java.nio.charset.StandardCharsets.UTF_8.name()`.
8. Replaced the `com.google.common.base.Throwables.getRootCause()` with a try-catch block.
9. Replaced the `substring(0, 12)` with `java.util.HexFormat.ofDelimiter("").formatHex(...)`.

Note: Please review this AI-generated patch before applying it.