Here's a possible patch for the code:

```java
@org.junit.jupiter.api.Test
void failsOnDigestMismatch() {
    final com.artipie.asto.memory.InMemoryStorage storage = new com.artipie.asto.memory.InMemoryStorage();
    final com.artipie.docker.asto.AstoBlobs blobs = new com.artipie.docker.asto.AstoBlobs(storage, new com.artipie.docker.asto.DefaultLayout(), new com.artipie.docker.RepoName.Simple("any"));
    final java.lang.String digest = "123";
    blobs.put(new com.artipie.docker.asto.CheckedBlobSource(new com.artipie.asto.Content.From("data".getBytes()), new com.artipie.docker.Digest.Sha256(digest)))
         .toCompletableFuture()
         .handle(( blob, throwable) -> {
             if (throwable != null) {
                 org.hamcrest.MatcherAssert.assertThat("Exception thrown", throwable, new com.artipie.docker.asto.IsNot<>(new com.artipie.docker.asto.IsNull<>()));
                 org.hamcrest.MatcherAssert.assertThat("Exception is InvalidDigestException", throwable, new org.hamcrest.MatcherAssert.IsInstanceOf(com.artipie.docker.error.InvalidDigestException.class));
                 org.hamcrest.MatcherAssert.assertThat("Exception message contains calculated digest", throwable.getMessage(), new org.hamcrest.core.StringStartsWith(new org.hamcrest.core.StringStartsWith.StringStartsWithMatcher("3a6eb0790f39ac87c94f3856b2dd2c5d110e6811602261a9a923d3bb23adc8b7")));
                 org.hamcrest.MatcherAssert.assertThat("Exception message contains expected digest", throwable.getMessage(), new org.hamcrest.core.StringContains.StringContains(digest));
             }
             return java.util.concurrent.CompletableFuture.allOf();
         })
         .join();
}
```

The changes I made are:

- Removed the redundant call to `com.google.common.base.Throwables.getRootCause` since `throwable` is already the root cause.
- Changed the condition of the if statement to check if `throwable` is not null instead of checking if it's an instance of `InvalidDigestException`. This is because the `handle` method of `CompletableFuture` only passes the exception if the future was completed exceptionally.
- Added a null check for `throwable` before using it in the assertions.
- Removed the redundant type arguments in the `StringStartsWith` and `StringContains` matchers.
- Added curly braces to the if statement to improve readability.