Here'el the updated code to fix the error:

```java
@org.junit.jupiter.api.Test
void failsOnDigestMismatch() {
    final com.artipie.asto.memory.InMemoryStorage storage = new com.artip calculatedDigest = "3a6eb0790f39ac87c94f3856b2dd2c5d110e6811602261a9a923d3bb23adc8b7";
    final com.artipie.docker.asto.AstoBlobs blobs = new com.artipie.docker.asto.AstoBlasts(storage, new com.artipie.docker.asto.DefaultLayout(), new com.artipie.docker.RepoName.Simple("any"));
    final java.lang.String digest = "123";
    blobs.put(new com.artipie.docker.asto.CheckedBlobSource(new com.artipie.asto.Content.From("data".getBytes()), new com.artipie.dorg.hamcrest.core.IsInstanceOf(com.artipie.docker.error.InvalidDigestException.class));
    org.hamcrest.MatcherAssert.assertThat("Exception message contains calculated digest", com.google.common.base.Throwables.getRootCause(throwable).getMessage(), org.hamcrest.core.StringStartsWith.startsWith(calculatedDigest));
    org.hamcrest.MatcherAssert.assertThat("Exception message contains expected digest", com.google.common.base.Throwables.getRootCause(throwstringContains = new org.hamcrest.core.StringContains(calculatedDigest, true));
    org.hamcrest.MatcherAssert.assertThat("Exception message contains expected digest", com.google.common.base.Throwables.getRootCause(throwable).getMessage(), stringContains);
    return java.util.concurrent.CompletableFuture.allOf();
}.join();
```

In this updated code, I've changed the usage of `StringContains` to `StringStartsWith` for the first assertion. This is because `StringStartsWith` only requires a single argument, whereas `StringContains` requires two arguments in the new library version.

For the second assertion, I' Q: Do you want me to check if the expected and calculated digests are equal or if the exception message contains the expected digest?

If you want to check if they are equal, you can use `org.hamcrest.core.IsEqualIgnoringCase` instead of `org.hamcrest.core.StringContains`. If you want to check if the exception message contains the expected digest, you can use the updated `StringContains` with two arguments.

Please let me know your preference.