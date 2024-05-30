Here's a suggested patch for the given client code:

```java
@org.junit.jupiter.api.Test
void failsOnDigestMismatch() {
    final com.artipie.asto.memory.InMemoryStorage storage = new com.artipie.asto.memory.InMemoryStorage();
    final com.artipie.docker.asto.AstoBlobs blobs = new com.artipie.docker.asto.AstoBlobs(storage, new com.artipie.docker.asto.DefaultLayout(), new com.artipie.docker.RepoName.Simple("any"));
    final java.lang.String digest = "123";
    com.artipie.docker.asto.CheckedBlobSource checkedBlobSource = new com.artipie.docker.asto.CheckedBlobSource(new com.artipie.asto.Content.From("data".getBytes()), new com.artipie.docker.Digest.Sha256(digest));
    com.artipie.docker.asto.BlobDescriptor blobDescriptor = new com.artipie.docker.asto.BlobDescriptor(new com.artipie.docker.Digest.Sha256(checkedBlobSource.digest()), checkedBlobSource.contentLength(), checkedBlobSource.mediaType());
    blobs.put(blobDescriptor).toCompletableFuture().handle(( blob, throwable) -> {
        org.hamcrest.MatcherAssert.assertThat("Exception thrown", throwable, new com.artipie.docker.asto.IsNot<>(new com.artipie.docker.asto.IsNull<>()));
        org.hamcrest.MatcherAssert.assertThat("Exception is InvalidDigestException", com.google.common.base.Throwables.getRootCause(throwable), new org.hamcrest.Matcher(new org.hamcrest.Description(), ( description, actual) -> {
            description.appendText("Instance of InvalidDigestException");
            return actual instanceof com.artipie.docker.error.InvalidDigestException;
        }));
    });
    org.hamcrest.MatcherAssert.assertThat("Exception message contains calculated digest", com.google.common.base.Throwables.getRootCause(throwable).getMessage(), new org.hamcrest.Matcher<java.lang.String>() {
        @java.lang.Override
        public boolean matches(java.lang.Object item) {
            java.lang.String message = ((java.lang.String) (item));
            return message.contains("3a6eb0790f39ac87c94f3856b2dd2c5d110e6811602261a9a923d3bb23adc8b7") && message.contains(digest);
        }

        @java.lang.Override
        public void describeTo(com.artipie.docker.asto.Description description) {
            description.appendText("String contains calculated and expected digests");
        }
    });
    return java.util.concurrent.CompletableFuture.allOf();
}
```

The patch includes the following changes:

1. Create a `com.artipie.docker.asto.CheckedBlobSource` and a `com.artipie.docker.asto.BlobDescriptor` to replace the deprecated `CheckedBlobSource` constructor.
2. Use the `blobDescriptor` object in the `blobs.put()` method.

These changes should resolve the "';' expected" error and make the code compatible with the new library version.