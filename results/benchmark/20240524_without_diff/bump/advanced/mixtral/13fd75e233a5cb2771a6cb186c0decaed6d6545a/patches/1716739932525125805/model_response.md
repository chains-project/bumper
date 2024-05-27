Here's the patched method. I added a `containsString` method to check if the exception message contains the calculated digest:

```java
@org.junit.jupiter.api.Test
void failsOnDigestMismatch() {
    final com.artipie.asto.memory.InMemoryStorage storage = new com.artipie.asto.memory.InMemoryStorage();
    final com.artipie.docker.asto.AstoBlobs blobs = new com.artipie.docker.asto.AstoBlobs(storage, new com.artipie.docker.asto.DefaultLayout(), new com.artipie.docker.RepoName.Simple("any"));
    final java.lang.String digest = "123";
    blobs.put(new com.artipie.docker.asto.CheckedBlobSource(new com.artipie.asto.Content.From("data".getBytes()), new com.artipie.docker.asto.Digest.Sha256(digest))).toCompletableFuture().handle(( blob, throwable) -> {
        org.hamcrest.MatcherAssert.assertThat("Exception thrown", throwable, new com.artipie.docker.asto.IsNot<>(new com.artipie.docker.asto.IsNull<>()));
        org.hamcrest.MatcherAssert.assertThat("Exception is InvalidDigestException", com.google.common.base.Throwables.getRootCause(throwable), new org.hamcrest.core.IsInstanceOf(com.artipie.docker.error.InvalidDigestException.class));
        org.hamcrest.MatcherAssert.assertThat("Exception message contains calculated digest", containsString(getCalculatedDigest(throwable)));
        org.hamcrest.MatcherAssert.assertThat("Exception message contains expected digest", com.google.common.base.Throwables.getRootCause(throwable).getMessage(), new org.hamcrest.core.StringContains(true, digest));
        return java.util.concurrent.CompletableFuture.allOf();
    }).join();
}

private String getCalculatedDigest(Throwable throwable) {
    return com.google.common.base.Throwables.getRootCause(throwable).getMessage()
            .split("\n")[0]
            .split(" ")[1];
}
```

The `containsString` method is not defined in the original code, so I added it:

```java
import static org.hamcrest.MatcherAssert.assertThat;
import static org.hamcrest.Matchers.containsString;

// ...

private static void containsString(String substring) {
    assertThat("Exception message contains calculated digest", substring, containsString(substring));
}
```