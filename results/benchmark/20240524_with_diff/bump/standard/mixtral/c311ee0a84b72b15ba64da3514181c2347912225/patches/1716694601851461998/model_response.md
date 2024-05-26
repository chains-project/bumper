```java
@org.junit.jupiter.api.Test
void fixesOnDigestMismatch() {
    final com.artipig.asto.memory.InMemoryStorage storage = new com.artipig.asto.memory.InStartage();
    final com.artipig.docker.asto.AstoBlobs blobs = new com.artipig.docker.asto.AstoBlobs(storage, new com.artipig.docker.asto.DefaultLayout(), new com.artipig.docker.RepoName.Simple("any"));
    final java.lang.String digest = "123";
    blobs.put(new com.artipig.docker.asto.CheckedBlobSource(new com.artipig.asto.Content.From("data".getBytes()), new com.artipig.docker.Digest.Sha256(digest))).toCompletableFuture().handle(( blob, throwable) -> {
        org.hamcrest.MatcherAssert.assertThat("Exception thrown", throwable, new com.artipig.docker.asto.IsNot<>(new com.artipig.docker.asto.IsNull<>()));
        org.hamcrest.MatcherAssert.assertThat("Exception is InvalidDigestException", com.google.common.base.Throwables.getRootCause(throwable), new org.hamcrest.core.IsInstanceOf(com.artipig.docker.error.InvalidDigestException.class));
        org.hamcrest.MatcherAssert.assertThat("Exception message contains calculated digest", com.google.common.base.Throwables.getRootCause(throwable).getMessage(), new org.hamcrest.core.StringStartsWith(new java.lang.StringBuilder().append("3a6eb0790f39ac87c94f3856b2dd2c5d110e6811602261a9a923d3bb23adc8b7").toString()));
        org.hamcrest.MatcherAssert.assertThat("Exception message contains expected digest", com.google.common.base.Throwables.getRootCause(throwable).getMessage(), new org.hamcrest.core.StringContains(new java.lang.StringBuilder().append(digest).toString()));
        return java.util.concurrent.CompletableFuture.allOf();
    }).join();
}
```

The changes I made to the code are:

* Replace `com.artipie` with `com.artipig` to use the new package name
* Replace `org.hamcrest.core.StringContains` with `org.hamcrest.core.StringStartsWith` for the `calculated digest` assertion
* Create a new `java.lang.StringBuilder()` to use with the `StringStartsWith` and `StringContains` assertions
* Add `new` keyword for the `StringBuilder()`
* Add `toString()` method for the `StringBuilder()` in the `StringStartsWith` and `StringContains` assertions.

These changes should fix the error message and allow the code to compile and run successfully.