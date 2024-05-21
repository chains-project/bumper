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
        org.hamcrest.MatcherAssert.assertThat("Exception thrown", throwable, new com.artipie.docker.asto.IsNot<>(new com.artipie.docker.asto.IsNull<>()));
        org.hamcrest.MatcherAssert.assertThat("Exception is InvalidDigestException", throwable, Matchers.instanceOf(com.artipie.docker.error.InvalidDigestException.class));
        org.hamcrest.MatcherAssert.assertThat("Exception message contains calculated digest", throwable.getMessage(), Matchers.stringContainsInOrder(digest, "3a6eb0790f39ac87c94f3856b2dd2c5d110e6811602261a9a923d3bb23adc8b7"));
        return CompletableFuture.allOf();
    }).join();
}
```

The changes made include:

* Importing `Matchers` from `org.hamcrest` to use its `stringContainsInOrder` method.
* Changing the second argument of `stringContains` to `throwable.getMessage()` to match the expected type.
* Using `Matchers.instanceOf` instead of `new IsInstanceOf` for the second assertion.
* Using `Matchers.stringContainsInOrder` instead of `new StringContains` for the third assertion.

Note that the `stringContainsInOrder` method is being used to assert that the exception message contains both the expected digest and the calculated digest, separated by a space. If the order of the digests in the message is not guaranteed, you may need to modify this assertion accordingly.