Here is the proposed patch for the failing client code:
```java
@org.junit.jupiter.api.Test
void failsOnDigestMismatch() {
    final com.artipie.asto.memory.InMemoryStorage storage = new com.artipie.asto.memory.InMemoryStorage();
    final com.artipie.docker.asto.AstoBlobs blobs = new com.artipie.docker.asto.AstoBlobs(storage, new com.artipie.docker.asto.DefaultLayout(), new com.artipie.docker.RepoName.Simple("any"));
    final java.lang.String digest = "123";
    blobs.put(new com.artipie.docker.asto.CheckedBlobSource(new com.artipie.asto.Content.From("data".getBytes()), new com.artipie.docker.Digest.Sha256(digest))).toCompletableFuture().handle(( blob, throwable) -> {
        org.hamcrest.MatcherAssert.assertThat("Exception thrown", throwable, new com.artipie.docker.asto.IsNot<>(new com.artipie.docker.asto.IsNull<>()));
        org.hamcrest.MatcherAssert.assertThat("Exception is InvalidDigestException", com.google.common.base.Throwables.getRootCause(throwable), new org.hamcrest.MatcherAssert.MatchesPattern(com.google.common.base.Strings.repeat(".*", 2) + "(?s).*Calculated digest: .*3a6eb0790f39ac87c94f3856b2dd2c5d110e6811602261a9a923d3bb23adc8b7.*Expected digest: .*" + digest + ".*"));
        return java.util.concurrent.CompletableFuture.allOf();
    }).join();
}
```
The changes made to the code are:

* Replace the usage of `StringContains` matcher with `MatchesPattern` matcher, which takes a regular expression as an argument.
* The regular expression used in `MatchesPattern` checks for the presence of both calculated and expected digest in the exception message.

The error message suggests that the `StringContains` constructor used in the original code takes only one argument, while two arguments are being passed. This issue has been addressed by using `MatchesPattern` instead of `StringContains`.