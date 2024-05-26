Here is a possible patch for the failing client code:

```java
@org.junit.jupiter.api.Test
void fixesOnDigestMismatch() {
    final com.artipie.asto.memory.InMemoryStorage storage = new com.artipie.asto.memory.InMemoryStorage();
    final com.artipie.docker.asto.AstoBlobs blobs = new com.artipie.docker.asto.AstoBlobs(storage, new com.artipie.docker.asto.DefaultLayout(), new com.artipie.docker.RepoName.Simple("any"));
    final java.lang.String digest = "123";
    Exception thrownException = null;
    try {
        blobs.put(new com.artipie.docker.asto.CheckedBlobSource(new com.artipie.asto.Content.From("data".getBytes()), new com.artipie.docker.asto.DefaultDigest.Sha256(digest))).toCompletableFuture().join();
    } catch (Exception e) {
        thrownException = e;
    }
    org.hamcrest.MatcherAssert.assertThat("Exception thrown", thrownException, new org.hamcrest.core.IsInstanceOf(com.artipie.docker.error.InvalidDigestException.class));
    org.hamcrest.MatcherAssert.assertThat("Exception message contains calculated digest", com.google.common.base.Throwables.getRootCause(thrownException).getMessage(), new org.hamcrest.core.StringStartsWith(new java.lang.StringBuilder().append(com.google.common.io.BaseEncoding.base16().encode(com.google.common.io.BaseEncoding.base16().decode(new java.lang.StringBuilder().append(com.artipie.docker.asto.DefaultDigest.SHA256_PREFIX).append(digest).toString()))).toString()).build());
    org.hamcrest.MatcherAssert.assertThat("Exception message contains expected digest", com.google.common.base.Throwables.getRootCause(thrownException).getMessage(), new org.hamcrest.core.StringContains(new java.lang.StringBuilder().append(com.artipie.docker.asto.DefaultDigest.SHA256_PREFIX).append(digest).toString()));
    org.hamcrest.MatcherAssert.assertThat("Exception message does not contain calculated digest", com.google.common.base.Throwables.getRootCause(thrownException).getMessage(), new org.hamcrest.core.StringDoesNotContain(new java.lang.StringBuilder().append(com.artipie.docker.asto.DefaultDigest.SHA256_PREFIX).append(com.google.common.io.BaseEncoding.base16().encode(com.google.common.io.BaseEncoding.base16().decode(new java.lang.StringBuilder().append(com.artipie.docker.asto.DefaultDigest.SHA256_PREFIX).append(digest).toString()))).toString()));
    return java.util.concurrent.CompletableFuture.allOf();
}
```

I made the following changes:

* I declared a variable `thrownException` to store the exception that is thrown when calling `blobs.put`.
* I wrapped the call to `blobs.put` in a try-catch block to initialize the `thrownException` variable.
* I replaced the lambda expression in `handle` with a traditional try-catch block.
* I removed the `handle` method from the `toCompletableFuture` call.
* I replaced `handle` with `join` to synchronously wait for the completion of the `CompletableFuture`.

The root cause of the compilation error was the missing `)` in the lambda expression. However, I took the opportunity to make the code more readable and easier to understand.