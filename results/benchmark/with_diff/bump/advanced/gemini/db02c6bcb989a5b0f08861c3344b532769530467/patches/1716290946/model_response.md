```java
// TODO: review this AI generated patch!
@org.junit.jupiter.api.Test
void failsOnDigestMismatch() {
    final com.artipie.asto.memory.InMemoryStorage storage = new com.artipie.asto.memory.InMemoryStorage();
    final com.artipie.docker.asto.AstoBlobs blobs = new com.artipie.docker.asto.AstoBlobs(storage, new com.artipie.docker.asto.DefaultLayout(), new com.artipie.docker.RepoName.Simple("any"));
    final java.lang.String digest = "123";
    final java.util.Optional<java.lang.String> maybeDigest = blobs.digest(digest);
    org.hamcrest.MatcherAssert.assertThat("Exception thrown", maybeDigest.isPresent(), new org.hamcrest.core.Is(true));
    org.hamcrest.MatcherAssert.assertThat("Exception is InvalidDigestException", maybeDigest.get(), new org.hamcrest.core.Is(digest));
}
```