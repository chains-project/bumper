Here is a possible patch for the failing client code:
```java
@org.junit.jupiter.api.Test
void fixesDigestMismatch() {
    final com.artipie.asto.memory.InMemoryStorage storage = new com.artipie.asto.memory.InMemoryStorage();
    final com.artipie.docker.asto.AstoBlobs blobs = new com.artipie.docker.asto.AstoBlobs(storage, new com.artipie.docker.asto.DefaultLayout(), new com.artipie.docker.RepoName.Simple("any"));
    final java.lang.String digest = "123";
    blobs.put(new com.artipie.docker.asto.CheckedBlobSource(new com.artipie.asto.Content.From("data".getBytes()), new com.artipie.docker.Digest.Sha256(digest))).toCompletableFuture().handle(( blob, throwable) -> {
        org.hamcrest.MatcherAssert.assertThat("Exception thrown", throwable, new com.artipie.docker.asto.IsNot<>(new com.artipie.docker.asto.IsNull<>()));
        org.hamcrest.MatcherAssert.assertThat("Exception is InvalidDigestException", com.google.common.base.Throwables.getRootCause(throwable), new org.hamcrest.core.IsInstanceOf(com.artipie.docker.error.InvalidDigestException.class));
        org.junit.jupiter.api.Assertions.assertTrue("Exception message contains calculated digest", com.google.common.base.Throwables.getRootCause(throwable).getMessage().contains("3a6eb0790f39ac87c94f3856b2dd2c5d110e6811602261a9a923d3bb23adc8b7"));
        org.junit.jupiter.api.Assertions.assertTrue("Exception message contains expected digest", com.google.common.base.Throwables.getRootCause(throwable).getMessage().contains(digest));
        return java.util.concurrent.CompletableFuture.allOf();
    }).join();
}
```
The failure is caused by the fact that the `StringContains` constructor expects a single argument (the expected substring), but it is called with two arguments (a boolean flag and the expected substring).

To fix the failure, I replaced the `MatcherAssert.assertThat` method calls with `Assertions.assertTrue` method calls, and used the `contains` method of the `String` class to check if the exception message contains the expected substrings.

Note that this patch assumes that the `junit-jupiter-api` library is available in the classpath, and that the `Assertions` class is imported as follows:
```java
import static org.junit.jupiter.api.Assertions.*;
```
If the `junit-jupiter-api` library is not available, a similar patch can be obtained by using the `hamcrest` library instead of `junit-jupiter-api`. In this case, the patch would look like this:
```java
@org.junit.jupiter.api.Test
void fixesDigestMismatch() {
    final com.artipie.asto.memory.InMemoryStorage storage = new com.artipie.asto.memory.InMemoryStorage();
    final com.artipie.docker.asto.AstoBlobs blobs = new com.artipie.docker.asto.AstoBlobs(storage, new com.artipie.docker.asto.DefaultLayout(), new com.artipie.docker.RepoName.Simple("any"));
    final java.lang.String digest = "123";
    blobs.put(new com.artipie.docker.asto.CheckedBlobSource(new com.artipie.asto.Content.From("data".getBytes()), new com.artipie.docker.Digest.Sha256(digest))).toCompletableFuture().handle(( blob, throwable) -> {
        org.hamcrest.MatcherAssert.assertThat("Exception thrown", throwable, new com.artipie.docker.asto.IsNot<>(new com.artipie.docker.asto.IsNull<>()));
        org.hamcrest.MatcherAssert.assertThat("Exception is InvalidDigestException", com.google.common.base.Throwables.getRootCause(throwable), new org.hamcrest.core.IsInstanceOf(com.artipie.docker.error.InvalidDigestException.class));
        org.hamcrest.MatcherAssert.assertThat("Exception message contains calculated digest", com.google.common.base.Throwables.getRootCause(throwable).getMessage(), org.hamcrest.CoreMatchers.stringContains("3a6eb0790f39ac87c94f3856b2dd2c5d110e6811602261a9a923d3bb23adc8b7"));
        org.hamcrest.MatcherAssert.assertThat("Exception message contains expected digest", com.google.common.base.Throwables.getRootCause(throwable).getMessage(), org.hamcrest.CoreMatchers.stringContains(digest));
        return java.util.concurrent.CompletableFuture.allOf();
    }).join();
}
```
In this case, the `stringContains` method of the `CoreMatchers` class is used to check if the exception message contains the expected substrings. Note that the `CoreMatchers` class is imported as follows:
```java
import static org.hamcrest.CoreMatchers.*;
```