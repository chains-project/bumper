Here's a suggested patch for the given client code:

```java
@org.junit.jupiter.api.Test
void failsOnDigestMismatch() {
    final com.artipie.asto.memory.InMemoryStorage storage = new com.artipie.asto.memory.InMemoryStorage();
    final com.artipie.docker.asto.AstoBlobs blobs = new com.artipie.docker.asto.AstoBlobs(storage, new com.artipie.docker.asto.DefaultLayout(), new com.artipie.docker.RepoName.Simple("any"));
    final java.lang.String digest = "123";
    blobs.put(new com.artipie.docker.asto.CheckedBlobSource(new com.artipie.asto.Content.From("data".getBytes()), new com.artipie.docker.Digest.Sha256(digest)))
         .exceptionally(throwable -> {
            org.hamcrest.MatcherAssert.assertThat("Exception thrown", throwable != null);
            org.hamcrest.MatcherAssert.assertThat("Exception is InvalidDigestException", com.google.common.base.Throwables.getRootCause(throwable) instanceof com.artipie.docker.error.InvalidDigestException);
            org.hamcrest.MatcherAssert.assertThat("Exception message contains calculated digest", com.google.common.base.Throwables.getRootCause(throwable).getMessage().startsWith("3a6eb0790f39ac87c94f3856b2dd2c5d110e6811602261a9a923d3bb23adc8b7"));
            return null;
         });
    org.hamcrest.MatcherAssert.assertThat("Exception message contains expected digest", com.google.common.base.Throwables.getRootCause(throwable).getMessage(), new org.hamcrest.core.StringContains(digest));
    return java.util.concurrent.CompletableFuture.allOf();
}
```

This patch addresses the error message by removing the unnecessary semicolon (;) after the lambda expression and using the `exceptionally` method instead of `handle` to process exceptions. Additionally, the null check `throwable != null` is used since the Java 8 lambda syntax does not allow the `throwable` parameter to be marked as `@NonNull` explicitly.

Note: I'm assuming that the error message you provided is not related to the original code you posted. If the error message is indeed related to the original code, please provide the correct error message.