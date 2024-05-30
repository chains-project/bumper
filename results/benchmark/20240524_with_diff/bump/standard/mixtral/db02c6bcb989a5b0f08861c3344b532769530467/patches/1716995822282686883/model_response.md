Here's a possible patch for the failing client code:

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
    blobs.put(new com.artipie.docker.asto.CheckedBlobSource(new com.artipie.asto.Content.From("data".getBytes(StandardCharsets.UTF_8)), new com.artipie.docker.Digest.Sha256(digest))).toCompletableFuture().handle(( blob, throwable) -> {
        MatcherAssert.assertThat("Exception thrown", throwable, Matchers.notNullValue());
        MatcherAssert.assertThat("Exception is InvalidDigestException", throwable, Matchers.instanceOf(com.artipie.docker.error.InvalidDigestException.class));
        MatcherAssert.assertThat("Exception message contains calculated digest", throwable.getMessage(), Matchers.stringContains("3a6eb0790f39ac87c94f3856b2dd2c5d110e6811602261a9a923d3bb23adc8b7"));
        MatcherAssert.assertThat("Exception message contains expected digest", throwable.getMessage(), Matchers.stringContains(digest));
        return allOf();
    }).join();
}
```

The changes made are:

* Replace `com.google.common.base.Throwables.getRootCause(throwable)` with `throwable` directly, as the former is no longer available in the new library version.
* Replace `new com.artipie.docker.asto.IsNot<>(new com.artipie.docker.asto.IsNull<>()`)` with `Matchers.notNullValue()`, as the former is no longer available in the new library version.
* Replace `new org.hamcrest.core.StringContains(true, "3a6eb0790f39ac87c94f3856b2dd2c5d110e6811602261a9a923d3bb23adc8b7")` with `Matchers.stringContains("3a6eb0790f39ac87c94f3856b2dd2c5d110e6811602261a9a923d3bb23adc8b7")`, as the former is no longer available in the new library version.
* Add `import java.nio.charset.StandardCharsets;` to specify the character set used in `"data".getBytes()`.
* Add `import static java.util.concurrent.CompletableFuture.allOf;` to use `allOf()` without having to qualify it with the package name.
* Replace `new org.hamcrest.core.IsInstanceOf(com.artipie.docker.error.InvalidDigestException.class)` with `Matchers.instanceOf(com.artipie.docker.error.InvalidDigestException.class)`, as the former is no longer available in the new library version.
* Replace `new org.hamcrest.core.StringContains(true, digest)` with `Matchers.stringContains(digest)`, as the former is no longer available in the new library version.
* Add `MatcherAssert.assertThat("Exception thrown", throwable, Matchers.notNullValue());` to check that `throwable` is not null.
* Replace `com.google.common.base.Throwables.getRootCause(throwable)` with `throwable` directly, as the former is no longer available in the new library version.
* Replace `new com.artipie.docker.asto.IsNot<>(new com.artipie.docker.asto.IsNull<>()`)` with `Matchers.notNullValue()`, as the former is no longer available in the new library version.
* Replace `new org.hamcrest.core.StringContains(true, "3a6eb0790f39ac87c94f3856b2dd2c5d110e6811602261a9a923d3bb23adc8b7")` with `Matchers.stringContains("3a6eb0790f39ac87c94f3856b2dd2c5d110e6811602261a9a923d3bb23adc8b7")`, as the former is no longer available in the new library version.
* Add `import org.hamcrest.Matchers;` to use `Matchers` without having to qualify it with the package name.
* Replace `java.util.concurrent.CompletableFuture.allOf()` with `allOf()`, as it has been imported with `import static java.util.concurrent.CompletableFuture.allOf;`.