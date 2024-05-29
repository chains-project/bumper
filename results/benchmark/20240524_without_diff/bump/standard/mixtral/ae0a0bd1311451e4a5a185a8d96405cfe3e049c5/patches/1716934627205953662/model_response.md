Here is the proposed patch for the failing client code:
```java
@org.junit.jupiter.api.Test
void fixedOnDigestMismatch() {
    final com.artipie.asto.memory.InMemoryStorage storage = new com.artipie.asto.memory.InMemoryStorage();
    final com.artipie.docker.asto.AstoBlobs blobs = new com.artipie.docker.asto.AstoBlobs(storage, new com.artipie.docker.asto.DefaultLayout(), new com.artipie.docker.RepoName.Simple("any"));
    final java.lang.String digest = "123";
    blobs.put(new com.artipie.docker.asto.CheckedBlobSource(new com.artipie.asto.Content.From("data".getBytes()), new com.artipie.docker.Digest.Sha256(digest))).toCompletableFuture().handle(( blob, throwable) -> {
        org.hamcrest.MatcherAssert.assertThat("Exception thrown", throwable, new com.artipie.docker.asto.IsNot<>(new com.artipie.docker.asto.IsNull<>()));
        org.hamcrest.MatcherAssert.assertThat("Exception is InvalidDigestException", com.google.common.base.Throwables.getRootCause(throwable), new org.hamcrest.core.IsInstanceOf(com.artipie.docker.error.InvalidDigestException.class));
        org.hamcrest.MatcherAssert.assertThat("Exception message contains calculated digest", com.google.common.base.Throwables.getRootCause(throwable).getMessage(), new org.hamcrest.core.StringStartsWith(new java.lang.StringBuilder("3a6eb0790f39ac87c94f3856b2dd2c5d110e6811602261a9a923d3bb23adc8b7").toString()));
        org.hamcrest.MatcherAssert.assertThat("Exception message contains expected digest", com.google.common.base.Throwables.getRootCause(throwable).getMessage(), new org.hamcrest.core.StringContains(digest));
        return java.util.concurrent.CompletableFuture.allOf();
    }).join();
}
```
The changes made in the code are:

1. Renamed the method name from `failsOnDigestMismatch` to `fixedOnDigestMismatch` to reflect the fact that it has been fixed.
2. Replaced the `org.hamcrest.core.StringContains` matcher with `org.hamcrest.core.StringStartsWith` for the calculated digest check. This is because the `StringContains` constructor that takes a boolean as the second argument has been removed in a later version of Hamcrest. Instead, we can use `StringStartsWith` to check if the calculated digest starts with the expected digest.
3. Kept the `StringContains` matcher for the expected digest check.

Note: The `StringStartsWith` matcher is used here as an alternative to `StringContains` to check if the calculated digest starts with the expected digest. However, depending on the specific requirements of the test, other matchers such as `StringContains` or `StringEndsWith` may be more appropriate.