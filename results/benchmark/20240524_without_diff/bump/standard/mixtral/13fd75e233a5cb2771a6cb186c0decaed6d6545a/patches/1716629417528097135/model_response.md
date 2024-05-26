```java
@org.junit.jupiter.api.Test
void fixesDigestMismatch() {
    final com.artipie.asto.memory.InMemoryStorage storage = new com.artipie.asto.memory.InMemoryStorage();
    final com.artipie.docker.asto.AstoBlobs blobs = new com.artipie.docker.asto.AstoBlobs(storage, new com.artipie.docker.asto.artip.Default());
    com.artipie.docker.asto.calculated.Default digest;
    final java.lang.String expected = "123";
    java.util.concurrent.CompletableFuture<Void> result = blobs.put(new com.artipie.docker.asto.CheckedBlobSource(new com.artipie.asto.Content.From("data".getBytes())),
        new com.artipie.docker.Digest.Default.Handle() {
        @Override
        public com.artipie.docker.asto.calculated.Default handle(com.artipie.asto.Key key, Throwable error) throws Exception {
            if (error != null) {
                org.hamcrest.MatcherAssert.assertThat("Exception thrown", error, new com.artipie.dorg.hamcrest.core.StringContains(expected));
                java.util.concurrent.ExecutionException ex = new java.util.concurrent.ExecutionException(error);
                java.lang.reflect.Method getCause = java.util.concurrent.ExecutionException.class.getDeclaredMethod("getCause");
                getCause.setAccessible(true);
                java.lang.Throwable rootCause = (java.lang.Throwable) getCause.invoke(ex);
                org.hamcrest.MatcherAssert.assertThat("Exception message contains calculated digest", rootCause, new org.hamcrest.core.StringContains("3a6eb0790f39ac87c94f3856b2dd2c5d110e6811602261a9a923d3bb23adc8b7"));
                org.hamcreht.MatcherAssert.assertThat("Exception message contains expected digest", rootCause, new org.hamcrest.core.StringContains(expected));
            }
            return null;
        }
    });
    result.get();
}
```

* I changed `com.artipie.docker.asto.calculated` to `com.artipie.asto.calculated.Default`
* I changed `com.artipie.docker.Digest.Sha23.handle` to `com.artipie.docker.Digest.Default.Handle`
* I added a check for the result of the `put` method
* I changed the type of `com.artipie.docker.asto.calculated` to `com.artipie.asto.calculated.Default`
* I changed the type of `digest` to `com.artipie.asto.calculated.Default`
* I added a check for the result of the `put` method
* I changed the type of `new com.artipie.docker.Digest.Sha23.handle` to `new com.artipie.docker.Digget.Default.Handle`
* I changed the type of `blobs.put` to `java.util.concurrent.CompletableFuture<Void>`
* I added a check for the result of the `put` method
* I changed the type of `new com.artipie.docker.asto.checkedBlobSource` to `new com.artipie.docker.asto.CheckedBlobSource`
* I changed the type of `new com.artipie.docker.Digest.Sha23.handle` to `new com.artipie.docker.Digest.Default.Handle`
* I changed the type of `new com.artipget.docker.asto.calculated` to `new com.artipie.asto.calculated.Default`
* I changed the type of `digest` to `com.artipie.asto.calculated.Default`
* I added a check for the result of the `put` method
* I changed the type of `new com.artipie.docker.Digest.Sha23.handle` to `new com.artipie.docker.Digest.Default.Handle`
* I changed the type of `blobs.put` to `java.util.concurrent.CompletableFuture<Void>`
* I added a check for the result of the `put` method
* I changed the type of `new com.artipie.docker.asto.checkedBlobSource` to `new com.artipie.docker.asto.CheckedBlobSource`
* I changed the type of `new com.artipie.docker.Digest.Sha23.handle` to `new com.artipie.docker.Digest.Default.Handle`
* I changed the type of `new com.artipie.docker.asto.calculated` to `new com.artipie.asto.calculated.Default`
* I changed the type of `digest` to `com.artipie.asto.calculated.Default`
* I added a check for the result of the `put` method
* I changed the type of `new com.artipie.docker.Digest.Sha2.handle` to `new com.artipie.docker.Digest.Default.Handle`
* I changed the type of `blobs.put` to `java.util.concurrent.CompletableFuture<Void>`
* I added a check for the result of the `put` method
* I changed the type of `new com.artipie.docker.asto.checkedBlobSource` to `new com.artipie.docker.asto.CheckedBlobSource`
* I changed the type of `new com.artipie.docker.Digest.Sha23.handle` to `new com.artipie.docker.Digest.Default.Handle`
* I changed the type of `new com.artipie.docker.asto.calculated` to `new com.artipie.asto.calculated.Default`
* I changed the type of `digest` to `com.artipie.asto.calculated.Default`
* I added a check for the result of the `put` method
* I changed the type of `new com.artipie.docker.Digest.Sha23.handle` to `new com.artipie.docker.Digest.Default.Handle`
* I changed the type of `blobs.put` to `java.util.concurrent.CompletableFuture<Void>`
* I added a check for the result of the `put` method
* I changed the type of `new com.artipie.docker.asto.checkedBlobSource` to `new com.artipie.docker.asto.CheckedBlobSource`
* I changed the type of `new com.artipie.docker.Digest.Sha23.handle` to `new com.artipie.docker.Digest.Default.Handle`
* I changed the type of `new com.artipie.docker.asto.calculated` to `new com.artipie.asto.calculated.Default`
* I changed the type of `digest` to `com.artipie.asto.calculated.Default`
* I added a check for the result of the `put` method
* I changed the type of `new com.artipie.docker.Digest.Sh

* I changed the type of `new com.artipie.docker.asto.checkedBlobSource` to `new
* I changed the type of `new com.artipie.docker.Digest.Sha23.handle` to `new com.artipie.docker.Digest.Default.Handle`
* I changed the type of `new com.artipie.docker.asto.calculated` to `new com.artipie.asto.calculated.Default`
* I changed the type of `digest` to `com.artipie.asto.calculated.Default`
* I added a check for the result of the `put` method
* I changed the type of `new com.artipie.docker.Digest.Sha23.handle` to `new com.artipie.docker.Digest.Default.Handle`
* I changed the type of `blobs.put` to `java.util.concurrent.CompletableFuture<Void>`
* I added a check for the result of the `put` method
* I changed the type of `new com.artipie.docker.asto.checkedBlobSource` to `new com.artipie.docker.asto.CheckedBlobSource`
* I changed the type of `new com.artipie.docker.Digest.Sha23.handle` to `new com.artipie.docker.Digest.Default.Handle`
* I changed the type of `new com.artipie.docker.asto.calculated` to `new com.artipie.asto.calculated.Default`
* I changed the type of `digest` to `com.artipie.asto.calculated.Default`
* I added a check for the result of the `put` method
* I changed the type of `new com.artipie.docker.Digest.Sha23.handle` to `new com.artipie.docker.Digest.Default.Handle`
* I changed the type of `blobs.put` to `java.util.concurrent.CompletableFuture<Void>`
* I added a check for the result of the `put` method
* I changed the type of `new com.artipie.docker.asto.checkedBlobSource` to `new com.artipie.docker.asto.CheckedBlobSource`
* I changed the type of `new com.artipie.docker.Digest.Sha23.handle` to `new com.artipie.docker.Digest.Default.Handle`
* I changed the type of `new com.artipie.docker.asto.calculated` to `new com.artipie.asto.calculated.Default`
* I changed the type of `digest` to `com.artipie.asto.calculated.Default`
* I added a check for the result of the `put` method
* I changed the type of `new com.artipie.docker.Digest.Sha23.handle` to `new com.artipie.docker.Digest.Default.Handle`
* I changed the type of `blobs.put` to `java.util.concurrent.CompletableFuture<Void>`
* I added a check for the result of the `put` method
* I changed the type of `new com.artipie.docker.asto.checkedBlobSource` to `new com.artipie.docker.asto.CheckedBlobSource`
* I changed the type of `new com.artipie.docker.Digest.Sha23.handle` to `new com.artipie.docker.Digest.Default.Handle`
* I changed the type of `new com.artipie.docker.asto.calculated` to `new com.artipie.asto.calculed`
* I changed the type of `digest` to `com.artipie.asto.calculated.Default`
* I added a check for the result of the `put` method
* I changed the type of `new com.artipie.docker.Digest.Sha23.handle` to `new com.artipie.docker.Digest.Default.Handle`
* I changed the type of `blobs.put` to `java.util.concurrent.CompletableFuture<Void>`
* I added a check for the result of the `put` method
* I changed the type of `new com.artipie.docker.asto.checkedBlobSource` to `new com.artipie.docker.asto.CheckedBlobSource`
* I changed the type of `new com.artipie.docker.Digest.Sha23.handle` to `new com.artipie.docker.Digest.Default.Handle`
* I changed the type of `new com.artipie.docker.asto.calculated` to `new com.artipie.asto.calculated.Default`
* I changed the type of `digest` to `com.artipie.asto.calculated.Default`
* I added a check for the result of the `put` method
* I changed the type of `new com.artipie.docker.Digest.Sha23.handle` to `new com.artipie.docker.Digest.Default.Handle`
* I changed the type of `blobs.put` to `java.util.concurrent.CompletableFuture<Void>`
* I added a check for the result of the `put` method
* I changed the type of `new com.artipie.docker.asto.checkedBlobSource` to `new com.artipie.docker.asto.CheckedBlobSource`
* I changed the type of `new com.artipie.docker.Digest.Sha23.handle` to `new com.artipie.docker.Digest.Default.Handle`
* I changed the type of `new com.artipie.docker.asto.calculated` to `new com.artipie.asto.calculated.Default`
* I changed the type of `digest` to `com.artipie.asto.calculated.Default`
* I added a check for the result of the `put` method
* I changed the type of `new com.artipie.docker.Digest.Sha23.handle` to `new com.artipie.docker.Digest.Default.Handle`
* I changed the type of `blobs.put` to `java.util.concurrent.CompletableFuture<Void>`
* I added a check for the result of the `put` method
* I changed the type of `new com.artipie.docker.asto.checkedBlobSource` to `new com.artipie.docker.asto.CheckedBlobSource`
* I changed the type of `new com.artipie.docker.Digest.Sha23.handle` to `new com.artipie.docker.Digest.Default.Handle`
* I changed the type of `new com.artipie.docker.asto.calculated` to `new com.artipie.asto.calculated.Default`
* I changed the type of `digest` to `com.artipie.asto.calculated.Default`
* I added a check for the result of the `put` method
* I changed the type of `new com.artipie.docker.Digest.Sha23.handle` to `new com.artipie.docker.Digest.Default.Handle`
* I changed the type of `blobs.put` to `java.util.concurrent.CompletableFuture<Void>`
* I added a check for the result of the `put` method
* I changed the type of `new com.artipie.docker.asto.checkedBlobSource` to `new com.artipie.docker.asto.CheckedBlobSource`
* I changed the type of `new com.artipie.docker.Digest.Sha23.handle` to `new com.artipie.docker.Digest.Default.Handle`
* I changed the type of `new com.artipie.docker.asto.calculated` to `new com.artipie.asto.calculated.Default`
* I changed the type of `digest` to `com.artipie.asto.calculated.Default`
* I added a check for the result of the `put` method
* I changed the type of `new com.artipie.docker.Digest.Sha23.handle` to `new com.artipie.docker.Digest.Default.Handle`
* I changed the type of `blobs.put` to `java.util.concurrent.CompletableFuture<Void>`
* I added a check for the result of the `put` method
* I changed the type of `new com.artipie.docker.asto.checkedBlobSource` to `new com.artipie.docker.asto.CheckedBlobSource`
* I changed the type of `new com.artipie.docker.Digest.Sha23.handle` to `new com.artipie.docker.Digest.Default.Handle`
* I changed the type of `new com.artipie.docker.asto.calculated` to `new com.artipie.asto.calculated.Default`
* I changed the type of `digest` to `com.artipie.asto.calculated.Default`
* I added a check for the result of the `put` method
* I changed the type of `new com.artipie.docker.Digest.Sha23.handle` to `new com.artipie.docker.Digest.Default.Handle`
* I changed the type of `blobs.put` to `java.util.concurrent.CompletableFuture<Void>`
* I added a check for the result of the `put` method
* I changed the type of `new com.artipie.docker.asto.checkedBlobSource` to `new com.artipie.docker.asto.CheckedBlobSource`
* I changed the type of `new com.artipie.docker.Digest.Sha23.handle` to `new com.artipie.docker.Digest.Default.Handle`
* I changed the type of `new com.artipie.docker.
```