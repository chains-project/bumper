Here is a possible patch for the failing client code:
```java
@org.junit.jupiter.api.Test
void failsOnDigestMismatch() {
    final com.artipie.asto.memory.InMemoryStorage storage = new com.artipie.asto.memory.InMemoryStorage();
    final com.artipie.docker.asto.AstoBlobs blobs = new com.artipie.docker.asto.AstoBlobs(storage, new com.artipie.docker.asto.DefaultLayout(), new com.artipie.docker.RepoName.Simple("any"));
    final java.lang.String digest = "123";
    blobs.put(new com.artipie.docker.asto.CheckedBlobSource(new com.artipie.asto.Content.From("data".getBytes()), new com.artipie.docker.Digest.Sha256(digest))).toCompletableFuture().handle(( blob, throwable) -> {
        org.hamcrest.MatcherAssert.assertThat("Exception thrown", throwable, new com.artipie.docker.asto.IsNot<>(new com.artipie.docker.asto.IsNull<>()));
        org.hamcrest.MatcherAssert.assertThat("Exception is InvalidDigestException", com.google.common.base.Throwables.getRootCause(throwable), new org.hamcrest.core.IsInstanceOf(com.artipie.docker.error.InvalidDigestException.class));
        org.hamcrest.MatcherAssert.assertThat("Exception message contains calculated digest", com.google.common.base.Throwables.getRootCause(throwable).getMessage(), new org.hamcrest.Matchers.StringContains("3a6eb0790f39ac87c94f3856b2dd2c5d110e6811602261a9a923d3bb23adc8b7"));
        org.hamcrest.MatcherAssert.assertThat("Exception message contains expected digest", com.google.common.base.Throwables.getRootCause(throwable).getMessage(), new org.hamcrest.core.StringContains.Containing(digest));
        return java.util.concurrent.CompletableFuture.allOf();
    }).join();
}
```
The changes I made are:

* I replaced `new org.hamcrest.core.StringContains(true, "3a6eb0790f39ac87c94f3856b2dd2c5d110e6811602261a9a923d3bb23adc8b7")` with `new org.hamcrest.Matchers.StringContains("3a6eb0790f39ac87c94f3856b2dd2c5d110e6811602261a9a923d3bb23adc8b7")`. The reason for this change is that the constructor `StringContains(boolean, String)` is no longer available in the new version of Hamcrest, and has been replaced by a constructor `StringContains(String)` that takes a single argument.
* I replaced `new org.hamcrest.core.StringContains(true, digest)` with `new org.hamcrest.core.StringContains.Containing(digest)`. The reason for this change is that the constructor `StringContains(boolean, String)` is no longer available in the new version of Hamcrest, and has been replaced by a method `Containing(String)` that achieves the same effect.

Note that these changes are based on the assumption that the new version of the library includes the following changes:

* The constructor `StringContains(boolean, String)` in `org.hamcrest.core.StringContains` has been removed.
* A constructor `StringContains(String)` has been added to `org.hamcrest.Matchers.StringContains`.
* A method `Containing(String)` has been added to `org.hamcrest.core.StringContains`.

If these assumptions are incorrect, the patch may not work as expected. In that case, please provide more information about the changes in the new library version, so that I can adjust the patch accordingly.