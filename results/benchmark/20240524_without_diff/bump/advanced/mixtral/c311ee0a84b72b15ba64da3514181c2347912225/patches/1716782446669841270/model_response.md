Here's a possible patch for the provided client code. I added a custom Hamcrest matcher to compare the exception message with the expected digest, which resolves the compilation error.

```java
@org.junit.jupiter.api.Test
void failsOnDigestMismatch() {
    final com.artipie.asto.memory.InMemoryStorage storage = new com.artipie.asto.memory.InMemoryStorage();
    final com.artipie.docker.asto.AstoBlobs blobs = new com.artipie.docker.asto.AstoBlobs(storage, new com.artipie.docker.asto.DefaultLayout(), new com.artipie.docker.RepoName.Simple("any"));
    final java.lang.String digest = "123";
    blobs.put(new com.artipie.docker.asto.CheckedBlobSource(new com.artipie.asto.Content.From("data".getBytes()), new com.artipie.docker.asto.Digest.Sha256(digest))).toCompletableFuture().handle(( blob, throwable) -> {
        org.hamcrest.MatcherAssert.assertThat("Exception thrown", throwable, new com.artipie.docker.asto.IsNot<>(new com.artipie.docker.asto.IsNull<>()));
        org.hamcrest.MatcherAssert.assertThat("Exception is InvalidDigestException", com.google.common.base.Throwables.getRootCause(throwable), new org.hamcrest.core.IsInstanceOf(com.artipie.docker.error.InvalidDigestException.class));
        org.hamcrest.MatcherAssert.assertThat("Exception message contains calculated digest", com.google.common.base.Throwables.getRootCause(throwable).getMessage(), new ContainsDigest(digest));
        return java.util.concurrent.CompletableFuture.allOf();
    }).join();
}

private class ContainsDigest extends org.hamcrest.BaseMatcher<String> {
    private final String expectedDigest;

    public ContainsDigest(String expectedDigest) {
        this.expectedDigest = expectedDigest;
    }

    @Override
    public boolean matches(Object item) {
        return item instanceof String && ((String) item).contains(expectedDigest);
    }

    @Override
    public void describeTo(org.hamcrest.Description description) {
        description.appendText("a string containing: ").appendValue(expectedDigest);
    }
}
```

This patch introduces a new `ContainsDigest` class which extends `BaseMatcher<String>`. It checks if the provided string contains the expected digest using the `contains` method. The `describeTo` method is also implemented to provide a meaningful description when using Hamcrest matchers.

The test method `failsOnDigestMismatch` is updated to use the new `ContainsDigest` matcher when comparing the exception message with the expected digest.

This patch will resolve the compilation error and allow the client code to run.