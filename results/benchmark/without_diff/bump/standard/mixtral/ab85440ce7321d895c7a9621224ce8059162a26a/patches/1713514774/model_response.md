Here's a possible patch for the provided client code that should fix the error:

```java
@org.junit.jupiter.api.Test
void failsOnDigestMismatch() {
    final com.artipie.asto.memory.InMemoryStorage storage = new com.artipie.asto.memory.InMemoryStorage();
    final com.artipie.docker.asto.AstoBlobs blobs = new com.artipie.docker.asto.AstoBlobs(storage, new com.artipie.docker.asto.DefaultLayout(), new com.artipie.docker.RepoName.Simple("any"));
    final java.lang.String digest = "123";
    blobs.put(new com.artipie.docker.asto.CheckedBlobSource(new com.artipie.asto.Content.From("data".getBytes()), new com.artipie.docker.Digest.Sha256(digest))).toCompletableFuture().handle(( blob, throwable) -> {
        org.hamcrest.MatcherAssert.assertThat("Exception thrown", throwable, new com.artipie.docker.asto.IsNot<>(new com.artipie.docker.asto.IsNull<>()));
        org.hamcrest.MatcherAssert.assertThat("Exception is InvalidDigestException", com.google.common.base.Throwables.getRootCause(throwable), new org.hamcrest.core.IsInstanceOf(com.artipie.docker.error.InvalidDigestException.class));
        org.hamcrest.MatcherAssert.assertThat("Exception message contains calculated digest", com.google.common.base.Throwables.getRootCause(throwable).getMessage(), new org.hamcrest.core.StringStartsWith(new java.lang.StringBuilder("3a6eb0790f39ac87c94f3856b2dd2c5d110e6811602261a9a923d3bb23adc8b7").toString()));
        org.hamcrest.MatcherAssert.assertThat("Exception message contains expected digest", com.google.common.base.Throwables.getRootCause(throwable).getMessage(), new org.hamcrest.core.StringContains.StringContains(digest));
        return java.util.concurrent.CompletableFuture.allOf();
    }).join();
}
```

The error message indicates that the `StringContains` constructor in `org.hamcrest.core.StringContains` cannot be applied to a boolean value. The `StringStartsWith` matcher was used instead of `StringContains` for the first assertion. The `StringContains` constructor that accepts a boolean value was deprecated and removed in Hamcrest 2.2. Instead, the `StringStartsWith` matcher can be used for the first assertion.

The `StringStartsWith` matcher checks if the given string starts with the specified prefix, while the `StringContains` matcher checks if the given string contains the specified substring.

The `StringContains` constructor that accepts a boolean value was removed in Hamcrest 2.2, so the `StringContains` constructor that accepts a `String` value is used for the second assertion.

The `StringContains` constructor that accepts a `String` value takes a `String` value as its argument, which is the expected digest in this case.

The `StringStartsWith` and `StringContains` matchers are both from the `org.hamcrest.core` package, so no import statement changes are necessary.