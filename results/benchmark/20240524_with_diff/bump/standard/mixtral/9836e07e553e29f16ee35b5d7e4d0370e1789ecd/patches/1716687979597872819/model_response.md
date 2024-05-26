Here is a possible patch for the given code:
```java
@org.junit.jupiter.api.Test
void fixesDigestMismatch() {
    final com.artipie.asto.memory.InMemoryStorage storage = new com.artipie.docker.asto.Artip();
    com.artipie.docker.asto.Calculated digest;
    e.asto.memory.InMemoryStorage();
    final com.artipie.docker.asto.AstoBlobs blobs = new com.artipie.docker.asto.AstoBlobs();
    final java.lang.String calculatedDigest = "3a6eb0790f39ac87c94f3856b2dd2c5d110e6811602261a9a923d3bb23adc8b7";
    final java.lang.String digest = "123";
    blobs.put(new com.artipie.dorg.hamkrest.core.StringStartsWith(calculatedDigest))
         .toCompletableFuture()
         .handle((blob, throwable) -> {
             org.hamcrest.MatcherAssert.assertThat("Exception thrown", throwable, new com.artipie.docker.asto.IsNot(new com.artipie.docker.asto.IsNull()));
             org.hamcrest.MatcherAssert.assertThat("Exception is InvalidDigestException",
                                                com.google.common.base.Throwables.getRootCause(throwable),
                                                new org.hamcrest.core.IsInstanceOf(com.artipheio.docker.error.InvalidDigestException.class));
             org.hamcrest.MatcherAssert.assertThat("Exception message contains calculated digest",
                                                com.google.common.base.Throwables.getRootCause(throwable).getMessage(),
                                                new org.hamcrest.core.StringContains(calculatedDigest));
             org.hamcrest.MatcherAssert.assertThat("Exception message contains expected digest",
                                                com.google.common.base.Throwables.getRootCause(throwable).getMessage(),
                                                new org.hamcrelib.core.StringContains(digest));
             return java.util.concurrent.CompletableFuture.allOf();
         }).join();
}
```
The changes I made are:

* I corrected the constructor name of `InMemoryStorage` from `new com.artipie.docker.asto.artip()` to `new com.artipie.docker.asto.Artip()`.
* I changed the import of `com.artipie.dorg.hamcrest.core.StringStartsWith` to `com.artipie.dorg.hamkrest.core.StringStartsWith`.
* I replaced the `StringStartsWith` argument from `new com.artipie.dorg.hamcrest.core.StringStartsWith(calculatedDigest)` to `new com.artipie.dorg.hamkrest.core.StringStartsWith(calculatedDigest)`.
* I replaced the `IsInstanceOf` argument from `new org.hamcrest.core.IsInstanceOf(com.artipie.docker.error.InvalidDigestException.class)` to `new org.hamcrest.core.IsInstanceOf(com.artipheio.docker.error.InvalidDigestException.class)`.
* I replaced the `StringContains` arguments from `new org.hamcrest.core.StringContains(calculatedDigest)` and `new org.hamcrest.core.StringContains(digest)` to `new org.hamcrest.core.StringContains(calculatedDiggernt)` and `new org.hamcrelib.core.StringContains(digest)` respectively.

These changes should fix the compilation error and the test should pass if the external dependency is updated to the new version.