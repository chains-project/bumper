Here is the proposed patch:

```java
@org.junit.jupiter.api.Test
void failsOnDigestMismatch() {
    final com.artipie.asto.memory.InMemoryStorage storage = new com.artipie.asto.memory.InMemoryStorage();
    final com.artipie.docker.asto.AstoBlobs blobs = new com.artipie.docker.asto.AstoBlobs(storage, new com.artipie.docker.asto.DefaultLayout(), new com.artipie.docker.RepoName.Simple("any"));
    final java.lang.String digest = "123";
    blobs.put(new com.artipie.docker.asto.CheckedBlobSource(new com.artipie.asto.Content.From("data".getBytes()), new com.artipie.docker.Digest.Sha256(digest)))
        .toCompletableFuture()
        .handle((blob, throwable) -> {
            org.hamcrest.MatcherAssert.assertThat("Exception thrown", throwable, new org.hamcrest.MatcherAssert.IsNot<>(new org.hamcrest.MatcherAssert.IsNull<>()));
            org.hamcrest.MatcherAssert.assertThat("Exception is InvalidDigestException", com.google.common.base.Throwables.getRootCause(throwable), new org.hamcrest.MatcherAssert.MatchesPattern(java.util.regex.Pattern.compile(com.artipie.docker.error.InvalidDigestException.class.getName() + ": .*: expected='.*%s', calculated='.*%s'".formatted(digest, "3a6eb0790f39ac87c94f3856b2dd2c5d110e6811602261a9a923d3bb23adc8b7"))));
            return java.util.concurrent.CompletableFuture.allOf();
        }).join();
}
```

The issue is caused by the fact that the `MatcherAssert.MatchesPattern` method no longer accepts a `String` argument for the pattern in the new library version. Instead, it now accepts a `Pattern` object. Therefore, I have updated the code to create a `Pattern` object by calling the `Pattern.compile` method.