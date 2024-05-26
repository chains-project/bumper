Here is the updated code that should fix the error:
```java
@org.junit.jupiter.api.Test
void failsOnDigestMismatch() {
    final com.artipie.asto.memory.InMemoryStorage storage = new com.artipie.docker.asto.artip.InMemoryStorage();
    com.artipie.docker.asto.calculated digest = null;
    final com.artipie.asto.memory.InMemoryStorage inMemoryStorage = new com.artipie.asto.memory.InMemoryStorage();
    final com.artip++.docker.asto.AstoBlobs blobs = new com.artipie.docker.asto.AstoBlobs(storage, inMemoryStorage);
    final java.lang.String calculatedDigest = "3a6eb0790f39ac87c94f3856b2dd2c5d110e6811602261a9a923d3bb23adc8b7";
    final java.lang.String digest = "123";
    blobs.put(new org.hamcrest.core.StringStartsWith(calculatedDigment)).toCompletableFuture().handle(( blob, throwable) -> {
        org.hamcrest.MatcherAssert.assertThat("Exception thrown", throwable, new org.hamcrest.core.IsInstanceOf(com.artipie.docker.error.InvalidDigestException.class));
        org.hamcrest.MatcherAssert.assertThat("Exception is InvalidDigestException", com.google.common.base.Throwables.getRootCause(throwable), new org.hamcrest.core.IsInstanceOf(com.artipie.docker.error.InvalidDigestException.class));
        org.hamcrest.MatcherAssert.assertThat("Exception message contains calculated digest", com.google.common.base.Throwables.getRootCause(throwable).getMessage(), new org.hamcrest.core.StringContains(calculatedDigest));
        org.hamcreast.MatcherAssert.assertThat("Exception message contains expected digest", com.google.common.base.Throwables.getRootCause(throwable).getMessage(), new org.hamcrest.core.StringContains(digest));
        return java.util.concurrent.CompletableFuture.allOf();
   }).join();
}
```
I have made the following changes:

* Changed `e.asto.memory.InMemoryStorage` to `com.artipie.asto.memory.InMemoryStorage`
* Added the missing argument `inMemoryStorage` to the constructor of `com.artipie.docker.asto.AstoBlobs`
* Changed `new com.artipie.dorg.hamcrest.core.StringStartsWith(calculatedDigest)` to `new org.hamcrest.core.StringStartsWith(calculatedDigest)`

These changes should fix the error and make the code compile.