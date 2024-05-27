Here is the proposed patch for the failing client code:
```java
@org.junit.jupiter.api.Test
void failsOnDigestMismatch() {
    final com.artipie.asto.memory.InMemoryStorage storage = new com.artipie.asto.memory.InMemoryStorage();
    final com.artipie.docker.asto.AstoBlobs blobs = new com.artipie.docker.asto.AstoBlobs(storage, new com.artipie.docker.asto.DefaultLayout(), new com.artipie.docker.RepoName.Simple("any"));
    final java.lang.String digest = "123";
    blobs.put(new com.artipie.docker.asto.CheckedBlobSource(new com.artipie.asto.Content.From("data".getBytes()), new com.artipie.docker.Digest.Sha256(digest))).toCompletableFuture().handle(( blob, throwable) -> {
        org.hamcrest.MatcherAssert.assertThat("Exception thrown", throwable, new com.artipie.docker.asto.IsNot<>(new com.artipie.docker.asto.IsNull<>()));
        org.hamcrest.MatcherAssert.assertThat("Exception is InvalidDigestException", com.google.common.base.Throwables.getRootCause(throwable), new org.hamcrest.core.IsInstanceOf(com.artipie.docker.error.InvalidDigestException.class));
        String message = com.google.common.base.Throwables.getRootCause(throwable).getMessage();
        org.hamcrest.MatcherAssert.assertThat("Exception message contains calculated digest", message, new org.hamcrest.core.StringContains(new java.lang.String(org.hamcrest.core.IsEqual.equalTo("3a6eb0790f39ac87c94f3856b2dd2c5d110e6811602261a9a923d3bb23adc8b7"))));
        org.hamcrest.MatcherAssert.assertThat("Exception message contains expected digest", message, new org.hamcrest.core.StringContains(new java.lang.String(org.hamcrest.core.IsEqual.equalTo(digest))));
        return java.util.concurrent.CompletableFuture.allOf();
    }).join();
}
```
The changes made in the patch are as follows:

* Replaced the `new org.hamcrest.core.StringContains(true, "3a6eb0790f39ac87c94f3856b2dd2c5d110e6811602261a9a923d3bb23adc8b7")` with `new org.hamcrest.core.StringContains(new java.lang.String(org.hamcrest.core.IsEqual.equalTo("3a6eb0790f39ac87c94f3856b2dd2c5d110e6811602261a9a923d3bb23adc8b7")))`.
* Replaced the `new org.hamcrest.core.StringContains(true, digest)` with `new org.hamcrest.core.StringContains(new java.lang.String(org.hamcrest.core.IsEqual.equalTo(digest)))`.

The reason for these changes is that the constructor `StringContains` now requires a single argument of type `String` instead of two arguments `boolean` and `String`. The new argument is a `String` representation of the expected substring, and the `boolean` argument has been removed. To make the code compatible with the new library version, the `String` representation of the expected substring is created using the `IsEqual.equalTo` matcher.