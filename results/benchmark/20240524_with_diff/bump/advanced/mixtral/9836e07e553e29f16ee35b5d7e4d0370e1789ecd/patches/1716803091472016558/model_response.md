Here's a possible patch for the failing client code:

```java
import org.hamcrest.Matchers;

@org.junit.jupiter.api.Test
void failsOnDigestMismatch() {
    final com.artipie.asto.memory.InMemoryStorage storage = new com.artipie.asto.memory.InMemoryStorage();
    final com.artipie.docker.asto.AstoBlobs blobs = new com.artipie.docker.asto.AstoBlobs(storage, new com.artipie.docker.asto.DefaultLayout(), new com.artipie.docker.RepoName.Simple("any"));
    final java.lang.String digest = "123";
    blobs.put(new com.artipie.docker.asto.CheckedBlobSource(new com.artipie.asto.Content.From("data".getBytes()), new com.artipie.docker.Digest.Sha256(digest))).toCompletableFuture().handle(( blob, throwable) -> {
        org.hamcrest.MatcherAssert.assertThat("Exception thrown", throwable, Matchers.notNullValue());
        org.hamcrest.MatcherAssert.assertThat("Exception is InvalidDigestException", throwable, Matchers.instanceOf(com.artipie.docker.error.InvalidDigestException.class));
        org.hamcrest.MatcherAssert.assertThat("Exception message contains calculated digest", Matchers.containsString(Throwables.getRootCause(throwable).getMessage(), "3a6eb0790f39ac87c94f3856b2dd2c5d110e6811602261a9a923d3bb23adc8b7"));
        org.hamcrest.MatcherAssert.assertThat("Exception message contains expected digest", Matchers.containsString(Throwables.getRootCause(throwable).getMessage(), digest));
        return java.util.concurrent.CompletableFuture.allOf();
    }).join();
}
```

The changes made are:

* Import `org.hamcrest.Matchers` to use its static methods for readability and compatibility with the new library version.
* Replace the deprecated `StringContains` matcher with the equivalent `containsString` method from `Matchers`.
* Replace the deprecated `IsNot` matcher with the equivalent `notNullValue` method from `Matchers`.
* Replace the deprecated `IsInstanceOf` matcher with the equivalent `instanceOf` method from `Matchers`.

These changes should fix the compilation error and make the test pass.