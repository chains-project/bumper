Here's a possible patch for the failing client code:

```java
@org.junit.jupiter.api.Test
void failsOnDigestMismatch() {
    final com.artipie.asto.memory.InMemoryStorage storage = new com.artipie.asto.memory.InMemoryStorage();
    final com.artipie.docker.asto.AstoBlobs blobs = new com.artipie.docker.asto.AstoBlobs(storage, new com.artipie.docker.asto.DefaultLayout(), new com.artipie.docker.RepoName.Simple("any"));
    final java.lang.String digest = "123";
    blobs.put(new com.artipie.docker.asto.CheckedBlobSource(new com.artipie.asto.Content.From("data".getBytes()), new com.artipie.docker.Digest.Sha256(digest))).toCompletableFuture().handle(( blob, throwable) -> {
        org.hamcrest.MatcherAssert.assertThat("Exception thrown", throwable, new com.artipie.docker.asto.IsNot<>(new com.artipie.docker.asto.IsNull<>()));
        org.hamcrest.MatcherAssert.assertThat("Exception is InvalidDigestException", com.google.common.base.Throwables.getRootCause(throwable), new org.hamcrest.Matchers.InstanceOf(com.artipie.docker.error.InvalidDigestException.class));
        String message = com.google.common.base.Throwables.getRootCause(throwable).getMessage();
        org.hamcrest.MatcherAssert.assertThat("Exception message contains calculated digest", message, new org.hamcrest.core.StringContains.Containing(new org.hamcrest.CoreMatchers.StringDescription("3a6eb0790f39ac87c94f3856b2dd2c5d110e6811602261a9a923d3bb23adc8b7")));
        org.hamcrest.MatcherAssert.assertThat("Exception message contains expected digest", message, new org.hamcrest.core.StringContains.Containing(new org.hamcrest.CoreMatchers.StringDescription(digest)));
        return java.util.concurrent.CompletableFuture.allOf();
    }).join();
}
```

The changes I made are:

- Replace `new org.hamcrest.core.StringContains(true, "3a6eb0790f39ac87c94f3856b2dd2c5d110e6811602261a9a923d3bb23adc8b7")` with `new org.hamcrest.core.StringContains.Containing(new org.hamcrest.CoreMatchers.StringDescription("3a6eb0790f39ac87c94f3856b2dd2c5d110e6811602261a9a923d3bb23adc8b7"))`.
- Replace `new org.hamcrest.core.StringContains(true, digest)` with `new org.hamcrest.core.StringContains.Containing(new org.hamcrest.CoreMatchers.StringDescription(digest))`.

The reason for these changes is that the constructor of `StringContains` has changed in the new library version, and now it takes a `DescribedAs` object instead of a boolean and a string. The `Containing` class is a new addition that can be used to create a `DescribedAs` object from a string description.