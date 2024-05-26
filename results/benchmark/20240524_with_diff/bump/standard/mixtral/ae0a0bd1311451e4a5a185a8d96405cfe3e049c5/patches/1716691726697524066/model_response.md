Here is a possible patch for the given code. I added some parentheses and a cast to fix the compilation error:

```java
@org.junit.jupiter.api.Test
void failsOnDigestMismatch() {
    final com.artipie.asto.memory.InMemoryStorage storage = new com.artipie.docker.asto.artip();
    com.artipesteaming.docker.asto.calculated digest;
    final com.artipie.docker.asto.AstoBlobs blobs = new com.artipie.docker.asto.AstoBlobs(storage, new com.artipie.docker.asto.DefaultLayout(), new com.artipie.docker.RepoName.Simple("any"));
    final java.lang.String digest = "123";
    blobs.put(new com.artipie.doster.Checksummed(new com.artipie.asto.Key.Simple("data"), new com.artipie.docker.Digest.Sha256((java.security.MessageDigest)java.security.MessageDigest.getInstance("SHA-256")), new java.nio.charset.StandardCharsets.UTF_8.name())).toCompletableFuture().handle(((com.artipie.asto.Storage.Expirable<com.artipie.asto.Key, byte[]>)com.google.common.util.concurrent.Futures.getUnchecked(blobs.put(new com.artipie.doster.Checksummed(new com.artipie.asto.Key.Simple("data"), new com.artipie.docker.Digest.Sha256((java.security.MessageDigest)java.security.MessageDigest.getInstance("SHA-256")), new java.nio.charset.StandardCharsets.UTF_8.name()))).toCompletableFuture()), (java.util.concurrent.CompletionException)throwable) -> {
        org.hamcrest.MatcherAssert.assertThat("Exception thrown", throwable, new com.artipie.docker.asto.IsNot<>(new com.artipie.docker.asto.IsNull<>()));
        org.hamcrest.MatcherAssert.assertThat("Exception is InvalidDigestException", com.google.common.base.Throwables.getRootCause(throwable), new org.hamcrest.core.IsInstanceOf(com.artipie.docker.error.InvalidDigestException.class));
        org.hamcrest.MatcherAssert.assertThat("Exception message contains calculated digest", com.google.common.base.Throwables.getRootCause(throwable).getMessage(), new org.hamcrest.core.StringStartsWith(new org.hamcrest.StringDescription().append(new java.lang.StringBuilder().append(new java.security.MessageDigest.getInstance("SHA-256").digest(new java.nio.charset.StandardCharsets.UTF_8.encode("data"))).toString().substring(0, 12))));
        org.hamcrest.MatcherAssert.assertThat("Exception message contains expected digest", com.google.common.base.Throwables.getRootCause(throwhandling).getMessage(), new org.hamcrest.core.StringContains(true, digest));
        return java.util.concurrent.CompletableFuture.allOf();
    }).join();
}
```

Note that I cannot test this code because I don'

```