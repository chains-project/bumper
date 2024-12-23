Here's a proposed patch for the given client code:

```java
import org.hamcrest.MatcherAssert;
import org.hamcrest.Matchers;
import java.util.concurrent.CompletableFuture;

@org.junit.jupiter.api.Test
void failsOnDigestMismatch() {
    final com.artipie.asto.memory.InMemoryStorage storage = new com.artipie.asto.memory.InMemoryStorage();
    final com.artipie.docker.asto.AstoBlobs blobs = new com.artipie.docker.asto.AstoBlobs(storage, new com.artipie.docker.asto.DefaultLayout(), new com.artipie.docker.RepoName.Simple("any"));
    final java.lang.String digest = "123";
    blobs.put(new com.artipie.docker.asto.CheckedBlobSource(new com.artipie.asto.Content.From("data".getBytes()), new com.artipie.docker.Digest.Sha256(digest))).toCompletableFuture().handle(( blob, throwable) -> {
        MatcherAssert.assertThat("Exception thrown", throwable, Matchers.notNullValue());
        MatcherAssert.assertThat("Exception is InvalidDigestException", throwable.getCause(), Matchers.instanceOf(com.artipie.docker.error.InvalidDigestException.class));
        MatcherAssert.assertThat("Exception message contains calculated digest", throwable.getCause().getMessage(), Matchers.stringContainsInOrder(digest, "3a6eb0790f39ac87c94f3856b2dd2c5d110e6811602261a9a923d3bb23adc8b7"));
        return CompletableFuture.allOf();
    }).join();
}
```

The changes include:

* Replacing `com.google.common.base.Throwables.getRootCause()` with `throwable.getCause()` to get the root cause of the exception.
* Replacing `org.hamcrest.core.StringContains(true, <arg>)` with `Matchers.stringContainsInOrder(<args>)` to check if a string contains a specific substring or substrings.
* Replacing `new com.artipie.docker.asto.IsNot<>(new com.artipie.docker.asto.IsNull<>>())` with `Matchers.notNullValue()` to check if a value is not null.
* Replacing `org.hamcrest.core.IsInstanceOf(com.artipie.docker.error.InvalidDigestException.class)` with `Matchers.instanceOf(com.artipie.docker.error.InvalidDigestException.class)` to check if an object is an instance of a specific class.