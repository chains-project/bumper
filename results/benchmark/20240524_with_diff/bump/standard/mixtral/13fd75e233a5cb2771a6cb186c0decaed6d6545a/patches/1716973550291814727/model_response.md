Here's a possible patch for the failing client code:

```java
import org.hamcrest.Matchers;
import static org.hamcrest.Matchers.instanceOf;
import static org.hamcrest.Matchers.isA;
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
        MatcherAssert.assertThat("Exception message contains calculated digest", throwable.getMessage(), Matchers.stringContainsInOrder(new String[]{"3a6eb0790f39ac87c94f3856b2dd2c5d110e6811602261a9a923d3bb23adc8b7"}));
        MatcherAssert.assertThat("Exception message contains expected digest", throwable.getMessage(), Matchers.stringContainsIgnoringCase(digest));
        return java.util.concurrent.CompletableFuture.allOf();
    }).join();
}
```

The changes include:

* Importing the `Matchers` class and some static methods from it, such as `not`, `instanceOf`, `isA`, and `stringContainsInOrder`.
* Using `MatcherAssert.assertThat` instead of `org.hamcrest.MatcherAssert.assertThat`.
* Using `MatcherAssert.assertThat` with the `not` matcher instead of `new com.artipie.docker.asto.IsNot<>(new com.artipie.docker.asto.IsNull<>())`.
* Using `MatcherAssert.assertThat` with the `instanceOf` matcher instead of `new org.hamcrest.core.IsInstanceOf(com.artipie.docker.error.InvalidDigestException.class)`.
* Using `MatcherAssert.assertThat` with the `stringContainsInOrder` matcher instead of `new org.hamcrest.core.StringContains(true, "3a6eb0790f39ac87c94f3856b2dd2c5d110e6811602261a9a923d3bb23adc8b7")`.
* Using `MatcherAssert.assertThat` with the `stringContainsIgnoringCase` matcher instead of `new org.hamcrest.core.StringContains(true, digest)`.

These changes should fix the error message, which was caused by the wrong number of arguments passed to the `stringContains` matcher. The new library version includes a new matcher called `stringContainsInOrder`, which can take an array of strings as an argument. The `stringContainsIgnoringCase` matcher can be used instead of `stringContains` to ignore the case of the substring.