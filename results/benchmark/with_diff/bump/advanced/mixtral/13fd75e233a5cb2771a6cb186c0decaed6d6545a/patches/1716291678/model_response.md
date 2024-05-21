Here's a possible patch for the given client code:

```java
@org.junit.jupiter.api.Test
void fixOnDigestMismatch() {
    final com.artipie.asto.memory.InMemoryStorage storage = new com.artipie.asto.memory.InMemoryStorage();
    final com.artipie.docker.asto.AstoBlobs blobs = new com.artipie.docker.asto.AstoBlobs(storage, new com.artipie.docker.asto.DefaultLayout(), new com.artipie.docker.RepoName.Simple("any"));
    final java.lang.String digest = "123";
    blobs.put(new com.artipie.docker.asto.CheckedBlobSource(new com.artipie.asto.Content.From("data".getBytes()), new com.artipie.docker.Digest.Sha256(digest))).toCompletableFuture().handle(( blob, throwable) -> {
        org.hamcrest.MatcherAssert.assertThat("Exception thrown", throwable, new com.artipie.docker.asto.IsNot<>(new com.artipie.docker.asto.IsNull<>()));
        org.hamcrest.MatcherAssert.assertThat("Exception is InvalidDigestException", throwable, new org.hamcrest.core.IsInstanceOf(com.artipie.docker.error.InvalidDigestException.class));
        org.hamcrest.MatcherAssert.assertThat("Exception message contains calculated digest", throwable.getMessage(), new org.hamcrest.core.StringContains.ContainingSubstring("3a6eb0790f39ac87c94f3856b2dd2c5d110e6811602261a9a923d3bb23adc8b7"));
        org.hamcrest.MatcherAssert.assertThat("Exception message contains expected digest", throwable.getMessage(), new org.hamcrest.core.StringContains.ContainingSubstring(digest));
        return java.util.concurrent.CompletableFuture.allOf();
    }).join();
}
```

The changes are:

* Replace `com.google.common.base.Throwables.getRootCause` with a simple `throwable` parameter, since the former method is no longer available.
* Replace `new org.hamcrest.core.StringContains(true, "substring")` with `new org.hamcrest.core.StringContains.ContainingSubstring("substring")`, since the former constructor is no longer available.

Note that these changes are based on the assumption that the new library version removes the `getRootCause` method from `com.google.common.base.Throwables` and the `StringContains` constructor that takes a boolean parameter from `org.hamcrest.core`. If the actual changes are different, the patch may need to be adjusted accordingly.