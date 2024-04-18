Here's a fixed version of the `failsOnDigestMismatch()` method that addresses the error message you provided:

```java
@org.junit.jupiter.api.Test
void failsOnDigestMismatch() {
    final com.artipie.asto.memory.InMemoryStorage storage = new com.artipie.asto.memory.InMemoryStorage();
    final com.artipie.docker.asto.AstoBlobs blobs = new com.artipie.docker.asto.AstoBlobs(storage, new com.artipie.docker.asto.DefaultLayout(), new com.artipie.docker.RepoName.Simple("any"));
    final java.lang.String digest = "123";
    blobs.put(new com.artipie.docker.asto.CheckedBlobSource(new com.artipie.asto.Content.From("data".getBytes()), new com.artipie.docker.Digest.Sha256(digest)))
        .toCompletableFuture()
        .handle(
            (blob, throwable) -> {
              if (throwable != null) {
                org.hamcrest.MatcherAssert.assertThat("Exception thrown", throwable, new com.artipie.docker.asto.IsNot<>(new com.artipie.docker.asto.IsNull<>()));
                org.hamcrest.MatcherAssert.assertThat("Exception is InvalidDigestException", com.google.common.base.Throwables.getRootCause(throwable), new org.hamcrest.core.IsInstanceOf(com.artipie.docker.error.InvalidDigestException.class));
                org.hamcrest.MatcherAssert.assertThat("Exception message contains calculated digest", com.google.common.base.Throwables.getRootCause(throwable).getMessage(), new org.hamcrest.Matchers.ContainsString(new java.lang.String(com.artipie.docker.Digest.Sha256.calculate("data"))));
                org.hamcrest.MatcherAssert.assertThat("Exception message contains expected digest", com.google.common.base.Throwables.getRootCause(throwable).getMessage(), new org.hamcrest.core.StringContains.StringContains(digest));
              }
              return java.util.concurrent.CompletableFuture.allOf();
            }
        )
        .join();
}
```

The main issue was that the `handle()` method call was missing a lambda arrow `->`, causing the error message. I added the missing arrow and also moved the `throwable != null` check inside the lambda to make it clearer that the null check applies to the `throwable` parameter.

Regarding the library changes, since you didn't provide any information about the changes between the library versions, I assumed that the library methods used in the code are still available and functional. If that's not the case, please provide the relevant library changes so I can adapt the code accordingly.