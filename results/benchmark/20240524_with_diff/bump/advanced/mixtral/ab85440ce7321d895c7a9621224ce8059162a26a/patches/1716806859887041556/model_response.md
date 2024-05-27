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
    blobs.put(new com.artipie.docker.asto.CheckedBlobSource(new com.artipie.asto.Content.From("data".getBytes(StandardCharsets.UTF_8)), new com.artipie.docker.Digest.Sha256(digest))).toCompletableFuture().handle(( blob, throwable) -> {
        MatcherAssert.assertThat("Exception thrown", throwable, Matchers.notNullValue());
        MatcherAssert.assertThat("Exception is InvalidDigestException", throwable, Matchers.instanceOf(com.artipie.docker.error.InvalidDigestException.class));
        MatcherAssert.assertThat("Exception message contains calculated digest", throwable.getMessage(), Matchers.stringContainsInOrder(digest, "3a6eb0790f39ac87c94f3856b2dd2c5d110e6811602261a9a923d3bb23adc8b7"));
        return CompletableFuture.allOf();
    }).join();
}
```

The changes made include:

* Importing `Matchers` from `org.hamcrest` to use the `stringContainsInOrder` method instead of `StringContains`.
* Changing the `StringContains` constructor call to use `stringContainsInOrder` instead, which takes a variable number of `String` arguments.
* Adding an explicit `StandardCharsets.UTF_8` argument to `"data".getBytes()` to ensure that the byte array is created using the correct character encoding.
* Changing the `MatcherAssert.assertThat` call that checks if the exception message contains the calculated digest to use `stringContainsInOrder` instead of `StringContains`.
* Removing the unnecessary `new` keyword before `IsNot` and `IsNull` in the first `MatcherAssert.assertThat` call.
* Changing the `MatcherAssert.assertThat` call that checks if the exception message contains the expected digest to use `stringContainsInOrder` instead of `StringContains`.