Here is a possible patch for the failing client code:
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
    blobs.put(new com.artipie.docker.asto.CheckedBlobSource(new com.artipie.asto.Content.From("data".getBytes(StandardCharsets.UTF_8)), new com.artipie.docker.Digest.Sha256(digest))).toCompletableFuture().handle(( blob, throwable) -> {
        MatcherAssert.assertThat("Exception thrown", throwable, Matchers.notNullValue());
        MatcherAssert.assertThat("Exception is InvalidDigestException", throwable, Matchers.instanceOf(com.artipie.docker.error.InvalidDigestException.class));
        MatcherAssert.assertThat("Exception message contains calculated digest", throwable.getMessage(), Matchers.stringContains("3a6eb0790f39ac87c94f3856b2dd2c5d110e6811602261a9a923d3bb23adc8b7"));
        MatcherAssert.assertThat("Exception message contains expected digest", throwable.getMessage(), Matchers.stringContains(digest));
        return CompletableFuture.allOf();
    }).join();
}
```
The changes I made are:

* I replaced the `com.google.common.base.Throwables` class with `java.util.Throwable` and used the `getMessage()` method instead of `getRootCause()`.
* I replaced the `org.hamcrest.core.StringContains` class with `org.hamcrest.Matchers.stringContains()` method.
* I added an import statement for `org.hamcrest.Matchers`.
* I added a `StandardCharsets.UTF_8` argument to the `getBytes()` method of the `"data"` string.

These changes should fix the error message you provided and make the code compile and run correctly. However, I cannot guarantee that these changes will not introduce new errors or affect the behavior of the code in other ways. You should test the patched code thoroughly to ensure that it works correctly for your use case.