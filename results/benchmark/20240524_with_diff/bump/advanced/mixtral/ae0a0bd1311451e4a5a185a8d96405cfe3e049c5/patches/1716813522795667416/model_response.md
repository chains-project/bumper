Here's a fixed version of the method using the new library version:

```java
import org.hamcrest.MatcherAssert;
import org.hamcrest.Matchers;
import java.nio.charset.StandardCharsets;
import java.util.concurrent.CompletableFuture;
import static org.hamcrest.Matchers.instanceOf;
import static org.hamcrest.Matchers.not;
import static org.hamcrest.Matchers.stringContainsInOrder;

@org.junit.jupiter.api.Test
void failsOnDigestMismatch() {
    final com.artipie.asto.memory.InMemoryStorage storage = new com.artipie.asto.memory.InMemoryStorage();
    final com.artipie.docker.asto.AstoBlobs blobs = new com.artipie.docker.asto.AstoBlobs(storage, new com.artipie.docker.asto.DefaultLayout(), new com.artipie.docker.RepoName.Simple("any"));
    final java.lang.String digest = "123";
    blobs.put(new com.artipie.docker.asto.CheckedBlobSource(new com.artipie.asto.Content.From("data".getBytes(StandardCharsets.UTF_8)), new com.artipie.docker.Digest.Sha256(digest))).toCompletableFuture().handle(( blob, throwable) -> {
        MatcherAssert.assertThat("Exception thrown", throwable, not(Matchers.nullValue()));
        MatcherAssert.assertThat("Exception is InvalidDigestException", throwable, instanceOf(com.artipie.docker.error.InvalidDigestException.class));
        MatcherAssert.assertThat("Exception message contains calculated digest", throwable.getMessage(), stringContainsInOrder(new String[]{"3a6eb0790f39ac87c94f3856b2dd2c5d110e6811602261a9a923d3bb23adc8b7"}));
        MatcherAssert.assertThat("Exception message contains expected digest", throwable.getMessage(), stringContainsInOrder(new String[]{digest}));
        return CompletableFuture.allOf();
    }).join();
}
```

The changes made are:

* Importing the new `Matchers` class from `org.hamcrest` package.
* Replacing `com.google.common.base.Throwables.getRootCause()` with `throwable.getMessage()` to get the exception message.
* Replacing `org.hamcrest.core.StringContains(true, ...)` with `stringContainsInOrder(new String[]{...})` from the new `Matchers` class.
* Adding `import static org.hamcrest.Matchers.not;` to import the `not` matcher.
* Adding `import static org.hamcrest.Matchers.instanceOf;` to import the `instanceOf` matcher.
* Adding `import java.nio.charset.StandardCharsets;` to import the `StandardCharsets` class.
* Replacing `"data".getBytes()` with `"data".getBytes(StandardCharsets.UTF_8)` to specify the character encoding.
* Replacing `new org.hamcrest.core.IsInstanceOf(com.artipie.docker.error.InvalidDigestException.class)` with `instanceOf(com.artipie.docker.error.InvalidDigestException.class)` from the new `Matchers` class.
* Replacing `new com.artipie.docker.asto.IsNot<>(new com.artipie.docker.asto.IsNull<>)` with `not(Matchers.nullValue())` from the new `Matchers` class.