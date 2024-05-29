Here's a possible patch for the given client code:

```java
import org.hamcrest.Matchers;
import java.util.concurrent.CompletableFuture;

@org.junit.jupiter.api.Test
void failsOnDigestMismatch() {
    final com.artipie.asto.memory.InMemoryStorage storage = new com.artipie.asto.memory.InMemoryStorage();
    final com.artipie.docker.asto.AstoBlobs blobs = new com.artipie.docker.asto.AstoBlobs(storage, new com.artipie.docker.asto.DefaultLayout(), new com.artipie.docker.RepoName.Simple("any"));
    final java.lang.String digest = "123";
    blobs.put(new com.artipie.docker.asto.CheckedBlobSource(new com.artipie.asto.Content.From("data".getBytes()), new com.artipie.docker.Digest.Sha256(digest))).toCompletableFuture().handle(( blob, throwable) -> {
        org.hamcrest.MatcherAssert.assertThat("Exception thrown", throwable, Matchers.notNullValue());
        org.hamcrest.MatcherAssert.assertThat("Exception is InvalidDigestException", throwable, Matchers.instanceOf(com.artipie.docker.error.InvalidDigestException.class));
        org.hamcrest.MatcherAssert.assertThat("Exception message contains calculated digest", throwable.getMessage(), Matchers.stringContains("3a6eb0790f39ac87c94f3856b2dd2c5d110e6811602261a9a923d3bb23adc8b7"));
        org.hamcrest.MatcherAssert.assertThat("Exception message contains expected digest", throwable.getMessage(), Matchers.stringContains(digest));
        return CompletableFuture.allOf();
    }).join();
}
```

The changes made are:

* Replace `new com.artipie.docker.asto.IsNot<>(new com.artipie.docker.asto.IsNull<>()` with `Matchers.notNullValue()`
* Replace `new org.hamcrest.core.StringContains(true,` with `Matchers.stringContains(`
* Replace `com.google.common.base.Throwables.getRootCause(throwable)` with `throwable`
* Import `org.hamcrest.Matchers`
* Remove unnecessary imports `com.google.common.base.Throwables` and `com.artipie.docker.asto.IsNot`
* Remove unnecessary argument `true` from `Matchers.stringContains`
* Replace `org.hamcrest.core.IsInstanceOf` with `Matchers.instanceOf`

The error was caused by using `new org.hamcrest.core.StringContains(true,` instead of `Matchers.stringContains(`, which expects a single argument instead of two. The `true` argument is not needed in this case, as the `Matchers.stringContains` method already includes a boolean argument to indicate whether the match should be case-sensitive or not.