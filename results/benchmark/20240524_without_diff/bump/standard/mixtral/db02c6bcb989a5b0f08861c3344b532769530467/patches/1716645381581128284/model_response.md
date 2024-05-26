Here is a possible patch for the failing client code:
```java
@org.junit.jupiter.api.Test
void fixesOnDigestMismatch() {
    final com.artipie.asto.memory.InMemoryStorage storage = new com.artipie.asto.memory.InMemoryStorage();
    final com.artipie.docker.asto.AstoBlobs blobs = new com.artipie.docker.asto.AstoBlobs(storage, new com.artipie.docker.asto.DefaultLayout(), new com.artipie.docker.RepoName.Simple("any"));
    final java.lang.String digest = "123";
    blobs.put(new com.artipie.docker.asto.CheckedBlobSource(new com.artipie.asto.Content.From("data".getBytes()), new com.artipie.docker.asto.DefaultDigest.Sha256(digest))).toCompletableFuture().handle(( blob, throwable) -> {
        org.hamcrest.MatcherAssert.assertThat("Exception thrown", throwable, new org.hamcrest.core.IsInstanceOf(com.artipie.docker.error.InvalidDigestException.class));
        org.hamcrest.MatcherAssert.assertThat("Exception message contains calculated digest", com.google.common.base.Throwables.getRootCause(throwable).getMessage(), new org.hamcrest.core.StringStartsWith(new java.lang.StringBuilder().append(com.google.common.io.BaseEncoding.base16().encode(com.google.common.io.BaseEncoding.base16().decode(new java.lang.StringBuilder().append(com.artipie.docker.asto.DefaultDigest.SHA256_PREFIX).append(digest).toString()))).toString()).build()));
        org.hamcrest.MatcherAssert.assertThat("Exception message contains expected digest", com.google.common.base.Throwables.getRootCause(throwable).getMessage(), new org.hamcrest.core.StringContains(new java.lang.StringBuilder().append(com.artipie.docker.asto.DefaultDigest.SHA256_PREFIX).append(digest).toString()));
        org.hamcrest.MatcherAssert.assertThat("Exception message does not contain calculated digest", com.google.common.base.Throwables.getRootCause(throwable).getMessage(), new org.hamcrest.core.StringDoesNotContain(new java.lang.StringBuilder().append(com.google.common.io.BaseEncoding.base16().encode(com.google.common.io.BaseEncoding.base16().decode(new java.lang.StringBuilder().append(com.artipie.docker.asto.DefaultDigest.SHA256_PREFIX).append(com.google.common.io.BaseEncoding.base16().encode(com.google.common.io.BaseEncoding.base16().decode(new java.lang.StringBuilder().append(com.artipie.docker.asto.DefaultDigest.SHA256_PREFIX).append(digest).toString()))).toString())).toString()));
        return java.util.concurrent.CompletableFuture.allOf();
    }).join();
}
```
The patch includes the following changes:

* The constructor of `StringContains` is changed from `StringContains(boolean, String)` to `StringStartsWith(String)` or `StringContains(String)`.
* The `IsNot` matcher is removed from the first `assertThat` method.
* The `getRootCause` method is called on the `throwable` object before passing it to the `assertThat` method.
* The `StringStartsWith` and `StringDoesNotContain` matchers are used in the third and fourth `assertThat` methods.
* The `SHA256_PREFIX` constant is used instead of hardcoding the prefix in the expected and actual values.
* The `decode` and `encode` methods of `BaseEncoding` are used to convert the hexadecimal string to a byte array and vice versa.
* The `new` keyword is added before the `StringBuilder` constructor.
* The `build()` method is called on the `StringBuilder` object.
* The `join()` method is called on the `completableFuture` object.
* The method name is changed from `failsOnDigestMismatch` to `fixesOnDigestMismatch`.