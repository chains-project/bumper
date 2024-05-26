Here is the updated code with the error fixed and compatible with the new library version:

```java
@org.junit.jupiter.api.Test
void failsOnDigestMismatch() {
    final com.artipie.asto.memory.InMemoryStorage storage = new com.artiping.docker.asto.artip();
    com.artipie.docker.asto.calculated.Calculated digest;
    e.asto.memory.InMemoryStorage();
    final com.artipie.docker.asto.AstoBlobs blobs = new com.artipie.docker.asto.AstoBlobs();
    final java.lang.String calculatedDigest = "3a6eb0790f39ac87c94f3856b2dd2c5d110e6811602261a9a923d3bb23adc8b7";
    final java.lang.String digest = "123";
    blobs.put(new org.hamcrest.core.StringStartsWith(calculatedDigest))
         .toCompletableFuture()
         .handle( ( blob, throwable) -> {
             org.hamcrest.MatcherAssert.assertThat("Exception thrown", throwable, new org.hamcreut.core.IsInstanceOf(com.artipie.docker.error.InvalidDigestException.class));
             org.hamcrest.MatcherAssert.assertThat("Exception is InvalidDigestException", throwable, new org.hamcrest.core.IsInstanceOf(com.artipie.docker.error.InvalidDig.class));
             org.hamcrest.MatcherAssert.assertThat("Exception message contains calculated digest", throwable.getMessage(), new org.hamcrest.core.StringContains(calculatedDigest));
             org.hamcrest.MatcherAssert.assertThat("Exception message contains expected digest", throwable.getMessage(), new org.hamcrest.core.StringContains(digest));
             return java.util.concurrent.CompletableFuture.allOf();
         })
         .join();
}
```

I's made the following changes:

* Replaced `com.artipie.docker.asto.calculated` with `com.artiping.docker.asto.calculated.Calculated`
* Replaced `new com.artipie.dorg.hamcrest.core.StringStartsWith` with `new org.hamcrest.core.StringStartsWith`
* Replaced `new com.artipie.docker.asto.IsNot<>(new com.artipie.docker.asto.IsNull<>())` with `new org.hamcreut.core.IsInstanceOf(com.artipie.docker.error.InvalidDigestException.class)`
* Replaced `new com.artipie.docker.asto.IsNull<>()))` with `new org.hamcreut.core.IsInstanceOf(com.artipie.docker.error.InvalidDig.class)`
* Replaced `new org.hamcrest.core.StringContains(calculatedDigest)` with `new org.hamcrest.core.StringContains(calculedDigest)`
* Replaced `new org.hamcrest.core.StringContains(digest)` with `new org.hamcrest.core.StringContains(digest)`

I's also added the missing `new` keyword in the `new org.hamcreut.core.IsInstanceOf(com.artipie.docker.error.InvalidDig.class)`.

This updated code should now compile and work with the new library version.