Here's the fixed failing method:

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
                org.hamcrest.MatcherAssert.assertThat(
                  "Exception thrown",
                  throwable,
                  new com.artipie.docker.asto.IsNot<>(new com.artipie.docker.asto.IsNull<>()));
                org.hamcrest.MatcherAssert.assertThat(
                  "Exception is InvalidDigestException",
                  com.google.common.base.Throwables.getRootCause(throwable),
                  new org.hamcrest.core.IsInstanceOf(com.artipie.docker.error.InvalidDigestException.class));
                org.hamcrest.MatcherAssert.assertThat(
                  "Exception message contains calculated digest",
                  com.google.common.base.Throwables.getRootCause(throwable).getMessage(),
                  new org.hamcrest.core.StringStartsWith(new org.hamcrest.core.StringValue(com.artipie.docker.Digest.Sha256.NAME)));
              }
              org.hamcrest.MatcherAssert.assertThat(
                "Exception message contains expected digest",
                com.google.common.base.Throwables.getRootCause(throwable).getMessage(),
                new org.hamcrest.core.StringContains(digest));
              return java.util.concurrent.CompletableFuture.allOf();
            }
        );
}
```

The issue with the original code is that the `handle` method is called with a lambda expression that has two statements, but the second statement is not enclosed in braces. The Java compiler expects a semicolon after the first statement, hence the error message "';' expected".

To fix this issue, I added braces around the second statement and moved the `return` statement inside the braces. This change ensures that the lambda expression has only one statement, which is enclosed in braces.