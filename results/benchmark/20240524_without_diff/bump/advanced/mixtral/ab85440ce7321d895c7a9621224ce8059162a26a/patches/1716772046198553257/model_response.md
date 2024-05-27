Here's the fixed failsOnDigestMismatch method:

```java
import org.hamcrest.MatcherAssert;
import org.junit.jupiter.api.Test;
import java.nio.charset.StandardCharsets;
import java.util.concurrent.CompletableFuture;
import java.util.concurrent.ExecutionException;

@Test
void failsOnDigestMismatch() throws ExecutionException, InterruptedException {
    final com.artipie.asto.memory.InMemoryStorage storage = new com.artipie.asto.memory.InMemoryStorage();
    final com.artipie.docker.asto.AstoBlobs blobs = new com.artipie.docker.asto.AstoBlobs(storage, new com.artipie.docker.asto.DefaultLayout(), new com.artipie.docker.RepoName.Simple("any"));
    final java.lang.String digest = "123";
    blobs.put(new com.artipie.docker.asto.CheckedBlobSource(new com.artipie.asto.Content.From("data".getBytes(StandardCharsets.UTF_8)), new com.artipie.docker.Digest.Sha256(digest))).toCompletableFuture().handle(( blob, throwable) -> {
        MatcherAssert.assertThat("Exception thrown", throwable, new com.artipie.docker.asto.IsNot<>(new com.artipie.docker.asto.IsNull<>()));
        MatcherAssert.assertThat("Exception is InvalidDigestException", throwable, new org.hamcrest.core.IsInstanceOf(com.artipie.docker.error.InvalidDigestException.class));
        MatcherAssert.assertThat("Exception message contains calculated digest", throwable.getMessage(), new org.hamcrest.core.StringContains.ContainingSubstring("3a6eb0790f39ac87c94f3856b2dd2c5d110e6811602261a9a923d3bb23adc8b7"));
        MatcherAssert.assertThat("Exception message contains expected digest", throwable.getMessage(), new org.hamcrest.core.StringContains.ContainingSubstring(digest));
        return CompletableFuture.allOf();
    }).join();
}
```

The changes include:

1. Importing `java.nio.charset.StandardCharsets` to fix the compilation error by providing the correct Charset to `getBytes()` method.
2. Changing `new org.hamcrest.core.StringContains(true, "3a6eb0790f39ac87c94f3856b2dd2c5d110e6811602261a9a923d3bb23adc8b7")` to `new org.hamcrest.core.StringContains.ContainingSubstring("3a6eb0790f39ac87c94f3856b2dd2c5d110e6811602261a9a923d3bb23adc8b7")`.
3. Changing `new org.hamcrest.core.StringContains(true, digest)` to `new org.hamcrest.core.StringContains.ContainingSubstring(digest)`.

The first change is necessary to fix the compilation error. The second and third changes are to use the correct constructor of `StringContains` class, as the original constructor with `(boolean, String)` is deprecated.