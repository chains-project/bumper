```java
@org.junit.jupiter.api.Test
void fixesDigestMismatch() {
    final com.artipie.asto.memory.InMemoryStorage storage = new com.artipie.asto.memory.InMemoryStorage();
    final com.artipie.docker.asto.AstoBlobs blobs = new com.artipie.docker.asto.AstoBlobs(storage, new com.artipie.docker.asto.artip.Default());
    com.artipie.docker.asto.calculated.Default digest;
    final java.lang.String expected = "123";
    blobs.put(new com.artipie.docker.asto.CheckedBlobSource(new com.artipie.asto.Content.From("data".getBytes())), new com.artipie.docker.Digest.Default.handle(( blob, throwable) -> {
        org.hamcrest.MatcherAssert.assertThat("Exception thrown", throwable, new com.artipie.docker.asto.IsNot<>(new com.artipie.dorg.hamcrest.core.StringContains(expected)));
        org.hamcrest.MatcherAssert.assertThat("Exception message contains calculated digest", com.google.common.base.Throwables.getRootCause(throwable), new org.hamcret.core.StringContains(expected));
        return java.util.concurrent.CompletableFuture.allOf();
    })).join();
}
```

Changes:

* Replace `com.artipie.docker.asto.artip` with `new com.artipie.docker.asto.artip.Default()`
* Replace `com.artipie.docker.Digest.Sha23.handle` with `new com.artipie.docker.Digest.Default.handle`
* Replace `org.hamcrest.core.StringContains` with `com.hamcrest.core.StringContains`
* Added missing `)` in `blobs.put` method call
* Replace `org.hamcrest.MatcherAssert.assertThat("Exception message contains calculated digest", com.google.common.base.Throwables.getRootCause(throwstringContains(throwable.getMessage(), "3a6eb0790f39ac87c94f3856b2dd2c5d110e6811602261a9a923d3bb23adc8b7")));` with `org.hamcrest.MatcherAssert.assertThat("Exception message contains calculated digest", com.google.common.base.Throwables.getRootCause(throwable), new com.hamcret.core.StringContains(expected));`
* Added missing `.join()` in `blobs.put` method call
* Replace `com.artipie.docker.asto.calculated` with `com.artipie.docker.asto.calculated.Default`
* Replace `org.hamcrest.core.StringContains` with `com.hamcrest.core.StringContains`