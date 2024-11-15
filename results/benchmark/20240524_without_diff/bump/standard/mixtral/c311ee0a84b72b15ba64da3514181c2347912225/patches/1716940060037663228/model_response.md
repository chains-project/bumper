Here is a possible patch for the failing client code:
```java
import org.hamcrest.Matchers;
import org.junit.jupiter.api.Test;
import java.nio.charset.StandardCharsets;
import java.util.concurrent.CompletableFuture;
import static org.hamcrest.MatcherAssert.assertThat;
import static org.hamcrest.Matchers.instanceOf;
import static org.hamcrest.Matchers.not;
import static org.hamcrest.core.IsEqual.equalTo;

@Test
void failsOnDigestMismatch() {
    final com.artipie.asto.memory.InMemoryStorage storage = new com.artipie.asto.memory.InMemoryStorage();
    final com.artipie.docker.asto.AstoBlobs blobs = new com.artipie.docker.asto.AstoBlobs(storage, new com.artipie.docker.asto.DefaultLayout(), new com.artipie.docker.RepoName.Simple("any"));
    final String digest = "123";
    blobs.put(new com.artipie.docker.asto.CheckedBlobSource(new com.artipie.asto.Content.From("data".getBytes()), new com.artipie.docker.Digest.Sha256(digest))).toCompletableFuture().handle(( blob, throwable) -> {
        assertThat("Exception thrown", throwable, not(equalTo(null)));
        assertThat("Exception is InvalidDigestException", throwable.getCause(), instanceOf(com.artipie.docker.error.InvalidDigestException.class));
        String message = throwable.getCause().getMessage();
        assertThat("Exception message contains calculated digest", message, Matchers.stringContainsString("3a6eb0790f39ac87c94f3856b2dd2c5d110e6811602261a9a923d3bb23adc8b7"));
        assertThat("Exception message contains expected digest", message, Matchers.stringContainsString(digest));
        return CompletableFuture.allOf();
    }).join();
}
```
The changes I made are:

* I imported the missing `Matchers` class from `org.hamcrest` package.
* I replaced the `StringContains` matcher with the `stringContainsString` method from `Matchers` class.
* I replaced the `IsNot` matcher with the `not` method from `Matchers` class.
* I replaced the `IsInstanceOf` matcher with the `instanceOf` method from `Matchers` class.
* I replaced the `IsEqual` matcher with the `equalTo` method from `Matchers` class.
* I replaced the `StringContains` constructor with the `stringContainsString` method from `Matchers` class.
These changes should fix the error message and make the test pass.