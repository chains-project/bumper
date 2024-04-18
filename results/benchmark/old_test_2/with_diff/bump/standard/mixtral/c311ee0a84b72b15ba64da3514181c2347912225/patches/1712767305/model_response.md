Here's the fixed failing method with the dependency update issue resolved:

```java
@org.junit.jupiter.api.Test
void failsOnDigestMismatch() {
    final com.artipie.asto.memory.InMemoryStorage storage = new com.artipie.asto.memory.InMemoryStorage();
    final com.artipie.docker.asto.AstoBlobs blobs = new com.artipie.docker.asto.AstoBlobs(storage, new com.artipie.docker.asto.DefaultLayout(), new com.artipie.docker.RepoName.Simple("any"));
    final java.lang.String digest = "123";
    blobs.put(new com.artipie.docker.asto.CheckedBlobSource(new com.artipie.asto.Content.From("data".getBytes()), new com.artipie.docker.Digest.Sha256(digest)))
            .toCompletableFuture()
            .handle((blob, throwable) -> {
                org.hamcrest.MatcherAssert.assertThat("Exception thrown", throwable != null);
                org.hamcrest.MatcherAssert.assertThat("Exception is InvalidDigestException", com.google.common.base.Throwables.getRootCause(throwable) instanceof com.artipie.docker.error.InvalidDigestException);
                org.hamcrest.MatcherAssert.assertThat("Exception message contains calculated digest", com.google.common.base.Throwables.getRootCause(throwable).getMessage(), new org.hamcrest.Matchers.ContainsString(new java.lang.String(com.artipie.docker.Digest.Sha256.calculate("data"))));
                org.hamcrest.MatcherAssert.assertThat("Exception message contains expected digest", com.google.common.base.Throwables.getRootCause(throwable).getMessage(), new org.hamcrest.core.StringContains.StringContains(digest));
                return java.util.concurrent.CompletableFuture.allOf();
            }).join();
}
```

I fixed the error by removing unnecessary parentheses and semicolons that caused the compilation error. Also, I replaced the 'handle' method's lambda argument condition checks to use 'instanceof' instead of the 'IsInstanceOf' matcher, which is not needed here.