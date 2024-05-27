Here's a possible patch for the given client code:

```java
import org.hamcrest.Matchers;
import org.junit.jupiter.api.Test;

@Test
void failsOnDigestMismatch() {
    final com.artipie.asto.memory.InMemoryStorage storage = new com.artipie.asto.memory.InMemoryStorage();
    final com.artipie.docker.asto.AstoBlobs blobs = new com.artipie.docker.asto.AstoBlobs(storage, new com.artipie.docker.asto.DefaultLayout(), new com.artipie.docker.RepoName.Simple("any"));
    final java.lang.String digest = "123";
    blobs.put(new com.artipie.docker.asto.CheckedBlobSource(new com.artipie.asto.Content.From("data".getBytes()), new com.artipie.docker.Digest.Sha256(digest))).toCompletableFuture().handle(( blob, throwable) -> {
        MatcherAssert.assertThat("Exception thrown", throwable, Matchers.notNullValue());
        MatcherAssert.assertThat("Exception is InvalidDigestException", throwable, Matchers.instanceOf(com.artipie.docker.error.InvalidDigestException.class));
        MatcherAssert.assertThat("Exception message contains calculated digest", throwable.getMessage(), Matchers.stringContains("3a6eb0790f39ac87c94f3856b2dd2c5d110e6811602261a9a923d3bb23adc8b7"));
        MatcherAssert.assertThat("Exception message contains expected digest", throwable.getMessage(), Matchers.stringContains(digest));
        return java.util.concurrent.CompletableFuture.allOf();
    }).join();
}
```

The changes I made include:

* Importing `Matchers` from `org.hamcrest` package.
* Replacing `org.hamcrest.core.IsNot` with `Matchers.notNullValue()`.
* Replacing `org.hamcrest.core.IsInstanceOf` with `Matchers.instanceOf()`.
* Replacing `org.hamcrest.core.StringContains` with `Matchers.stringContains()`.

The `StringContains` constructor now expects a single `String` argument instead of a `boolean` and a `String`. The `Matchers.stringContains()` method is a drop-in replacement for the deprecated constructor.

Note that I used the fully qualified name of `java.util.concurrent.CompletableFuture` to avoid any potential conflicts with other classes that may have the same name.