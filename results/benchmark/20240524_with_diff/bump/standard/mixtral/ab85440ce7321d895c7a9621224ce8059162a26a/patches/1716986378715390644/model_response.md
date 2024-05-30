Here's a possible patch for the given client code:

```java
import org.hamcrest.Matchers;
import org.junit.jupiter.api.Test;

import java.nio.charset.StandardCharsets;
import java.util.concurrent.CompletableFuture;

@Test
void failsOnDigestMismatch() {
    final com.artipie.asto.memory.InMemoryStorage storage = new com.artipie.asto.memory.InMemoryStorage();
    final com.artipie.docker.asto.AstoBlobs blobs = new com.artipie.docker.asto.AstoBlobs(storage, new com.artipie.docker.asto.DefaultLayout(), new com.artipie.docker.RepoName.Simple("any"));
    final String digest = "123";
    blobs.put(new com.artipie.docker.asto.CheckedBlobSource(new com.artipie.asto.Content.From("data".getBytes(StandardCharsets.UTF_8)), new com.artipie.docker.Digest.Sha256(digest))).toCompletableFuture().handle((blob, throwable) -> {
        MatcherAssert.assertThat("Exception thrown", throwable, Matchers.notNullValue());
        MatcherAssert.assertThat("Exception is InvalidDigestException", throwable, Matchers.instanceOf(com.artipie.docker.error.InvalidDigestException.class));
        MatcherAssert.assertThat("Exception message contains calculated digest", throwable.getMessage(), Matchers.stringContainsInOrder(
                "3a6eb0790f39ac87c94f3856b2dd2c5d110e6811602261a9a923d3bb23adc8b7",
                digest
        ));
        return CompletableFuture.allOf();
    }).join();
}
```

Changes made:

* Imported `Matchers` from `org.hamcrest` package.
* Replaced `new com.google.common.base.Throwables.getRootCause(throwable)` with `throwable` in the first `MatcherAssert.assertThat` call.
* Changed `new org.hamcrest.core.StringContains(true, "3a6eb0790f39ac87c94f3856b2dd2c5d110e6811602261a9a923d3bb23adc8b7")` to `"3a6eb0790f39ac87c94f3856b2dd2c5d110e6811602261a9a923d3bb23adc8b7"` in the second `MatcherAssert.assertThat` call.
* Replaced `new org.hamcrest.core.StringContains(true, digest)` with `digest` in the third `MatcherAssert.assertThat` call.
* Replaced `new org.hamcrest.core.IsInstanceOf(com.artipie.docker.error.InvalidDigestException.class)` with `Matchers.instanceOf(com.artipie.docker.error.InvalidDigestException.class)` in the third `MatcherAssert.assertThat` call.
* Replaced `new org.hamcrest.core.IsNot<>(new org.hamcrest.core.IsNull<>())` with `Matchers.notNullValue()` in the first `MatcherAssert.assertThat` call.
* Replaced `new org.hamcrest.core.StringContains(true, "3a6eb0790f39ac87c94f3856b2dd2c5d110e6811602261a9a923d3bb23adc8b7")` and `new org.hamcrest.core.StringContains(true, digest)` with `MatcherAssert.assertThat("Exception message contains calculated digest", throwable.getMessage(), Matchers.stringContainsInOrder(` in the third `MatcherAssert.assertThat` call.
* Changed `new com.artipie.asto.Content.From("data".getBytes())` to `new com.artipie.asto.Content.From("data".getBytes(StandardCharsets.UTF_8))` to fix the compilation error.

Note that I assumed that the `data` string should be encoded using UTF-8 charset. If this is not the case, you may need to adjust the code accordingly.