Here's a possible patch for the provided client code. I added a custom Hamcrest matcher to compare the exception message with the expected digest, since the `StringContains` matcher doesn't accept a boolean parameter.

```java
@org.junit.jupiter.api.Test
void failsOnDigestMismatch() {
    final com.artipie.asto.memory.InMemoryStorage storage = new com.artipie.asto.memory.InMemoryStorage();
    final com.artipie.docker.asto.AstoBlobs blobs = new com.artipie.docker.asto.AstoBlobs(storage, new com.artipie.docker.asto.DefaultLayout(), new com.artipie.docker.RepoName.Simple("any"));
    final java.lang.String digest = "123";
    blobs.put(new com.artipie.docker.asto.CheckedBlobSource(new com.artipie.asto.Content.From("data".getBytes()), new com.artipie.docker.asto.Digest.Sha256(digest))).toCompletableFuture().handle(( blob, throwable) -> {
        org.hamcrest.MatcherAssert.assertThat("Exception thrown", throwable, new com.artipie.docker.asto.IsNot<>(new com.artipie.docker.asto.IsNull<>()));
        org.hamcrest.MatcherAssert.assertThat("Exception is InvalidDigestException", com.google.common.base.Throwables.getRootCause(throwable), new org.hamcrest.core.IsInstanceOf(com.artipie.docker.error.InvalidDigestException.class));
        org.hamcrest.MatcherAssert.assertThat("Exception message contains calculated digest", com.google.common.base.Throwables.getRootCause(throwable).getMessage(), new ContainsDigest(true, "3a6eb0790f39ac87c94f3856b2dd2c5d110e6811602261a9a923d3bb23adc8b7"));
        org.hamcrest.MatcherAssert.assertThat("Exception message contains expected digest", com.google.common.base.Throwables.getRootCause(throwable).getMessage(), new ContainsDigest(true, digest));
        return java.util.concurrent.CompletableFuture.allOf();
    }).join();
}

private static class ContainsDigest extends com.artipie.docker.asto.StringMatcher {
    private final boolean startsWith;

    public ContainsDigest(boolean startsWith, String digest) {
        super(digest);
        this.startsWith = startsWith;
    }

    @Override
    protected boolean matchesSafely(String item) {
        if (startsWith) {
            return item.startsWith(this.description) || item.contains(" " + this.description);
        } else {
            return item.contains(this.description);
        }
    }
}
```

This code creates a new `ContainsDigest` class that extends the `StringMatcher` class from the original code. The `matchesSafely` method checks whether the exception message contains the expected digest, either at the beginning or somewhere in the message.