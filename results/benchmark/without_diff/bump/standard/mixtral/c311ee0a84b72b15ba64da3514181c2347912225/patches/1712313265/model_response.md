Here's a possible patch for the code you provided:

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
        MatcherAssert.assertThat("Exception is InvalidDigestException", throwable, Matchers.instanceOf(com.artipie.docker.error.InvalidDigestException.class));
        MatcherAssert.assertThat("Exception message contains calculated digest", throwable.getMessage(), Matchers.stringContains("3a6eb0790f39ac87c94f3856b2dd2c5d110e6811602261a9a923d3bb23adc8b7"));
        MatcherAssert.assertThat("Exception message contains expected digest", throwable.getMessage(), Matchers.stringContains(digest));
        return CompletableFuture.allOf();
    }).join();
}
```

The changes I made are:

* I imported the `Matchers` class from `org.hamcrest` package, which provides a variety of matchers that can be used with `MatcherAssert`.
* I replaced the `com.google.common.base.Throwables.getRootCause(throwable)` calls with just `throwable` in the `MatcherAssert.assertThat()` calls, since the `handle()` method already provides the root cause of the exception.
* I replaced the `StringContains` matchers with `stringContains` matchers, which take a `String` argument instead of a `boolean` and a `String`.
* I replaced the `IsInstanceOf` matcher with `instanceOf` matcher, which takes a class argument instead of a `Class` object.
* I replaced the `IsNot` matcher with `notNullValue()` matcher, which checks if the given object is not null.
* I replaced the `CompletableFuture.allOf()` method with `CompletableFuture.allOf()` method from `java.util.concurrent` package, since the `com.artipie.docker.asto` package does not have this method.

These changes should fix the error message you provided. However, I cannot guarantee that the patched code will work correctly in your system, since I don't have access to the full context of your codebase.