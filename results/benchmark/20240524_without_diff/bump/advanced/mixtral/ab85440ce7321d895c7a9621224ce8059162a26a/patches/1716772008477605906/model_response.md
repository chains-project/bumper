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
The patch fixes the compilation error by importing the `Matchers` class from `org.hamcrest` package, and using its static methods `notNullValue()`, `instanceOf()`, `stringContains()` instead of the corresponding methods from the `com.artipie.docker.asto` package.
The `stringContains()` method now takes a single argument, which is the expected substring.
The `getBytes()` method of the `String` class now takes a `Charset` argument, which is set to `StandardCharsets.UTF_8`.
Finally, the `MatcherAssert.assertThat()` method now takes a variable number of arguments, which are the actual value, the matcher, and the matcher arguments.
This patch should fix the compilation error and make the test pass, assuming that the mocked dependencies and the behavior of the `AstoBlobs` class are correct.