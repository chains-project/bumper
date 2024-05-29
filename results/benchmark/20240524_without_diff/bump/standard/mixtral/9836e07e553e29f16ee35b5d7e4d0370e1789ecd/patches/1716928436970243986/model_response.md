Here's a possible patch for the failing client code:

```java
import org.hamcrest.Matchers;
import java.util.concurrent.CompletableFuture;

@org.junit.jupiter.api.Test
void failsOnDigestMismatch() {
    final com.artipie.asto.memory.InMemoryStorage storage = new com.artipie.asto.memory.InMemoryStorage();
    final com.artipie.docker.asto.AstoBlobs blobs = new com.artipie.docker.asto.AstoBlobs(storage, new com.artipie.docker.asto.DefaultLayout(), new com.artipie.docker.RepoName.Simple("any"));
    final java.lang.String digest = "123";
    blobs.put(new com.artipie.docker.asto.CheckedBlobSource(new com.artipie.asto.Content.From("data".getBytes()), new com.artipie.docker.Digest.Sha256(digest))).toCompletableFuture().handle(( blob, throwable) -> {
        MatcherAssert.assertThat("Exception thrown", throwable, Matchers.notNullValue());
        MatcherAssert.assertThat("Exception is InvalidDigestException", throwable, Matchers.instanceOf(com.artipie.docker.error.InvalidDigestException.class));
        MatcherAssert.assertThat("Exception message contains calculated digest", throwable.getMessage(), Matchers.stringContains("3a6eb0790f39ac87c94f3856b2dd2c5d110e6811602261a9a923d3bb23adc8b7"));
        MatcherAssert.assertThat("Exception message contains expected digest", throwable.getMessage(), Matchers.stringContains(digest));
        return CompletableFuture.allOf();
    }).join();
}
```

The changes made include:

* Importing `Matchers` from `org.hamcrest` package to use its static methods for matchers.
* Changing the `IsNot` matcher to `notNullValue` matcher for the first `MatcherAssert.assertThat` statement.
* Changing the `IsInstanceOf` matcher to `instanceOf` matcher for the second `MatcherAssert.assertThat` statement.
* Changing the `StringContains` matcher to `stringContains` matcher for the third and fourth `MatcherAssert.assertThat` statements.

These changes should fix the compilation error by using the correct matcher methods.