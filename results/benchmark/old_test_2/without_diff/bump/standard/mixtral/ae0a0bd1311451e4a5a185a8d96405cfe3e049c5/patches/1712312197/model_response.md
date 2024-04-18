Here's a possible patch for the code:

```java
import org.hamcrest.MatcherAssert;
import org.hamcrest.Matchers;
import java.nio.charset.StandardCharsets;
import java.util.concurrent.CompletableFuture;
import static java.util.concurrent.CompletableFuture.allOf;

@org.junit.jupiter.api.Test
void failsOnDigestMismatch() {
    final com.artipie.asto.memory.InMemoryStorage storage = new com.artipie.asto.memory.InMemoryStorage();
    final com.artipie.docker.asto.AstoBlobs blobs = new com.artipie.docker.asto.AstoBlobs(storage, new com.artipie.docker.asto.DefaultLayout(), new com.artipie.docker.RepoName.Simple("any"));
    final java.lang.String digest = "123";
    CompletableFuture<?> future = blobs.put(new com.artipie.docker.asto.CheckedBlobSource(new com.artipie.asto.Content.From("data".getBytes(StandardCharsets.UTF_8)), new com.artipie.docker.Digest.Sha256(digest)))
        .handle((blob, throwable) -> {
            MatcherAssert.assertThat("Exception thrown", throwable, Matchers.notNullValue());
            MatcherAssert.assertThat("Exception is InvalidDigestException", throwable, Matchers.instanceOf(com.artipie.docker.error.InvalidDigestException.class));
            MatcherAssert.assertThat("Exception message contains calculated digest", throwable.getMessage(), Matchers.stringContainsInOrder(digest, "3a6eb0790f39ac87c94f3856b2dd2c5d110e6811602261a9a923d3bb23adc8b7"));
            return allOf();
        });
    future.join();
}
```

The main changes are:

* Importing `Matchers` from `org.hamcrest` package and using it instead of `StringContains`.
* Using `MatcherAssert.assertThat` method with `Matchers.notNullValue()` instead of `MatcherAssert.assertThat("Exception thrown", throwable, new com.artipie.docker.asto.IsNot<>(new com.artipie.docker.asto.IsNull<>()));`.
* Using `MatcherAssert.assertThat` method with `Matchers.instanceOf(com.artipie.docker.error.InvalidDigestException.class)` instead of `MatcherAssert.assertThat("Exception is InvalidDigestException", com.google.common.base.Throwables.getRootCause(throwable), new org.hamcrest.core.IsInstanceOf(com.artipie.docker.error.InvalidDigestException.class));`.
* Using `MatcherAssert.assertThat` method with `Matchers.stringContainsInOrder(digest, "3a6eb0790f39ac87c94f3856b2dd2c5d110e6811602261a9a923d3bb23adc8b7")` instead of `MatcherAssert.assertThat("Exception message contains calculated digest", com.google.common.base.Throwables.getRootCause(throwable).getMessage(), new org.hamcrest.core.StringContains(true, "3a6eb0790f39ac87c94f3856b2dd2c5d110e6811602261a9a923d3bb23adc8b7"));` and `MatcherAssert.assertThat("Exception message contains expected digest", com.google.common.base.Throwables.getRootCause(throwable).getMessage(), new org.hamcrest.core.StringContains(true, digest));`.
* Replacing `CompletableFuture.allOf()` with `allOf()`.
* Replacing `new Content.From("data".getBytes())` with `new Content.From("data".getBytes(StandardCharsets.UTF_8))`.