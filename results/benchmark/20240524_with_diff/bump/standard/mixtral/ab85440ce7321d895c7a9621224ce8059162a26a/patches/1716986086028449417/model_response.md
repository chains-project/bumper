Here's a proposed patch for the given client code:

```java
import org.hamcrest.MatcherAssert;
import org.junit.jupiter.api.Test;
import java.nio.charset.StandardCharsets;
import java.util.concurrent.CompletableFuture;
import static org.hamcrest.Matchers.*;
import static org.hamcrest.core.IsInstanceOf.instanceOf;

@Test
void failsOnDigestMismatch() {
    final com.artipie.asto.memory.InMemoryStorage storage = new com.artipie.asto.memory.InMemoryStorage();
    final com.artipie.docker.asto.AstoBlobs blobs = new com.artipie.docker.asto.AstoBlobs(storage, new com.artipie.docker.asto.DefaultLayout(), new com.artipie.docker.RepoName.Simple("any"));
    final String digest = "123";
    blobs.put(new com.artipie.docker.asto.CheckedBlobSource(new com.artipie.asto.Content.From("data".getBytes(StandardCharsets.UTF_8)), new com.artipie.docker.Digest.Sha256(digest))).toCompletableFuture().handle((blob, throwable) -> {
        MatcherAssert.assertThat("Exception thrown", throwable, notNullValue());
        MatcherAssert.assertThat("Exception is InvalidDigestException", throwable, instanceOf(com.artipie.docker.error.InvalidDigestException.class));
        MatcherAssert.assertThat("Exception message contains calculated digest", throwable.getMessage(), stringContainsInOrder(digest, "3a6eb0790f39ac87c94f3856b2dd2c5d110e6811602261a9a923d3bb23adc8b7"));
        return CompletableFuture.allOf();
    }).join();
}
```

In this patch, I've made the following changes:

1. Imported `notNullValue` and `stringContainsInOrder` from `org.hamcrest.Matchers` and `org.hamcrest.core` respectively.
2. Replaced the usage of the deprecated `StringContains` constructor with the `stringContainsInOrder` method.
3. Changed the order of arguments in the `stringContainsInOrder` method to match the new library version.
4. Updated the `getBytes` method to include the `StandardCharsets.UTF_8` parameter.
5. Removed unnecessary imports.