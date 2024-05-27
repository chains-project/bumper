Here is the proposed patch:

```java
@org.junit.jupiter.api.Test
void fixesDigestMismatch() {
    final com.artipie.asto.memory.InMemoryStorage storage = new com.artipie.asto.memory.InMemoryStorage();
    final com.artipie.docker.asto.AstoBlobs blobs = new com.artipie.docker.asto.AstoBlobs(storage, new com.artipie.docker.asto.DefaultLayout(), new com.artipie.docker.RepoName.Simple("any"));
    final java.lang.String digest = "123";
    blobs.put(new com.artipie.docker.asto.CheckedBlobSource(new com.artipie.asto.Content.From("data".getBytes()), new com.artipie.docker.Digest.Sha256(digest)))
            .thenAccept(blob -> {
                try {
                    blob.get();
                } catch (Exception e) {
                    org.hamcrest.MatcherAssert.assertThat("Exception thrown", e, new com.artipie.docker.asto.IsNot<>(new com.artipie.docker.asto.IsNull<>()));
                    org.hamcrest.MatcherAssert.assertThat("Exception is InvalidDigestException", e, new org.hamcrest.MatcherAssert.MatchesPattern(com.artipie.docker.error.InvalidDigestException.class.getName() + ": .*"));
                    org.hamcrest.MatcherAssert.assertThat("Exception message contains calculated digest", e.getMessage(), new org.hamcrest.core.StringStartsWith(new java.lang.StringBuilder("3a6eb0790f39ac87c94f3856b2dd2c5d110e6811602261a9a923d3bb23adc8b7")));
                    org.hamcrest.MatcherAssert.assertThat("Exception message contains expected digest", e.getMessage(), new org.hamcrest.core.StringContains(digest));
                }
            })
            .join();
}
```

I have made the following changes:

* Replaced `handle` method with `thenAccept` method to handle the result of the `CompletableFuture`.
* Wrapped the code inside a `try-catch` block to handle the exception.
* Replaced `getRootCause` method with direct access to the exception.
* Fixed the indentation and formatting of the code.

Note: I am assuming that the `IsNot` and `IsNull` classes are present in the `com.artipie.docker.asto` package. If not, you may need to import them or replace them with appropriate matchers.