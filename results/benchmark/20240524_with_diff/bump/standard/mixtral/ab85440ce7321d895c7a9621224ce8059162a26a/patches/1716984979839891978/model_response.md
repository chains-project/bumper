Here's a proposed patch for the failing client code:

```java
import org.hamcrest.Matchers;
import static org.hamcrest.Matchers.instanceOf;
import static org.hamcrest.Matchers.not;
import static org.hamcrest.Matchers.nullValue;

@org.junit.jupiter.api.Test
void failsOnDigestMismatch() {
    final com.artipie.asto.memory.InMemoryStorage storage = new com.artipie.asto.memory.InMemoryStorage();
    final com.artipie.docker.asto.AstoBlobs blobs = new com.artipie.docker.asto.AstoBlobs(storage, new com.artipie.docker.asto.DefaultLayout(), new com.artipie.docker.RepoName.Simple("any"));
    final java.lang.String digest = "123";
    blobs.put(new com.artipie.docker.asto.CheckedBlobSource(new com.artipie.asto.Content.From("data".getBytes()), new com.artipie.docker.Digest.Sha256(digest))).toCompletableFuture().handle(( blob, throwable) -> {
        MatcherAssert.assertThat("Exception thrown", throwable, not(nullValue()));
        MatcherAssert.assertThat("Exception is InvalidDigestException", throwable, instanceOf(com.artipie.docker.error.InvalidDigestException.class));
        MatcherAssert.assertThat("Exception message contains calculated digest", throwable.getMessage(), Matchers.stringContains("3a6eb0790f39ac87c94f3856b2dd2c5d110e6811602261a9a923d3bb23adc8b7"));
        MatcherAssert.assertThat("Exception message contains expected digest", throwable.getMessage(), Matchers.stringContains(digest));
        return java.util.concurrent.CompletableFuture.allOf();
    }).join();
}
```

The changes I made are:

* Import the `Matchers` class from `org.hamcrest` package.
* Replace the `new StringContains(true, ...)` calls with `stringContains(...)` calls using `Matchers` class.
* Replace the `new IsNot<>(new IsNull<>())` call with `not(nullValue())` call using `Matchers` class.
* Replace the `new IsInstanceOf(com.artipie.docker.error.InvalidDigestException.class)` call with `instanceOf(com.artipie.docker.error.InvalidDigestException.class)` call using `Matchers` class.

These changes should fix the compilation error caused by the changes in the library version.