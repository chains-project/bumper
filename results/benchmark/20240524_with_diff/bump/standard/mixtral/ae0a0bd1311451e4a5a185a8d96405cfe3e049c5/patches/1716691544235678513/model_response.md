Here' proposed patch for the given client code, which can fix the error:

```java
@org.junit.jupiter.api.Test
void fixesDigestMismatch() {
    final com.artipie.asto.memory.InMemoryStorage storage = new com.artipie.docker.asto.artip();
    com.artipie.docker.asto.calculated.MD5 digest;
    final com.artipie.docker.asto.AstoBlobs blobs = new com.artipie.docker.asto.AstoBlasts(storage, new com.artipie.docker.asto.DefaultLayout(), new com.artipmd5.docker.RepoName.Simple("any"));
    final String digest = "123";
    blobs.put(new com.artipie.doster.Checksummed(new com.artipie.asto.Key.Simple("data"), new com.artipie.docker.MD5.Sha256(digest), new java.nio.charset.StandardCharsets.UTF_8.name())).toCompletableFuture().handle(( blob, throwable) -> {
        org.hamcrest.MatcherAssert.assertThat("Exception thrown", throwable, new com.artipie.docker.asto.IsNot<>(new com.artipie.docker.asto.IsNull<>()));
        org.hamcrest.MatcherAssert.assertThat("Exception is InvalidDigestException", org.hamcrest.CoreMatchers.instanceOf(com.artipie.docker.error.InvalidDigestException.class));
        org.hamcrest.MatcherAssert.assertThat("Exception message contains calculated digest", org.hamcrest.CoreMatchers.startsWith(new java.security.MessageDigest.getInstance("SHA-256").digest(new java.nio.charset.StandardCharsets.UTF_8.encode("data"))).toString().substring(0, 12)));
        org.hamcrest.MatcherAssert.assertThat("Exception message contains expected digest", org.hamcrest.CoreMatchers.containsString(digest));
        return java.util.concurrent.CompletableFuture.allOf();
    }).join();
}
```

The changes include:

- `com.artipie.docker.asto.calculated` is changed to `com.artipie.docker.asto.calculated.MD5`
- `com.artipie.docker.RepoName.Simple` is changed to `com.artipmd5.docker.RepoName.Simple`
- `org.hamcrest.core.StringStartsWith` is changed to `org.hamcrest.CoreMatchers.startsWith`
- `org.hamcrest.core.StringContains` is changed to `org.hamcrest.CoreMatchs.containsString`
- `com.google.common.base.Throwables.getRootCause` is removed
- `new org.hamcrest.StringDescription().append(new java.lang.StringBuilder().append(new java.security.MessageDigest.getInstance("SHA-256").digest(new java.nio.charset.StandardCharsets.UTF_8.encode("data"))).toString().substring(0, 12))` is replaced with `new java.security.MessageDigest.getInstance("SHA-256").digest(new java.nio.charset.StandardCharsets.UTF_8.encode("data"))).toString().substring(0, 12)`