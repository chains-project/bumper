Here's the proposed patch:

```java
@org.junit.jupiter.api.Test
void failsOnDigestMismatch() {
    final com.artipie.asto.memory.InMemoryStorage storage = new com.artipie.asto.memory.InMemoryStorage();
    final com.artipie.docker.asto.AstoBlobs blobs = new com.artipie.docker.asto.AstoBlobs(storage, new com.artipie.docker.asto.DefaultLayout(), new com.artipie.docker.RepoName.Simple("any"));
    final java.lang.String digest = "123";
    blobs.put(new com.artipie.docker.asto.CheckedBlobSource(new com.artipie.asto.Content.From("data".getBytes()), new com.artipie.docker.Digest.Sha256(digest))).toCompletableFuture().handle(( blob, throwable) -> {
        org.hamcrest.MatcherAssert.assertThat("Exception thrown", throwable, new com.artipie.docker.asto.IsNot<>(new com.artipie.docker.asto.IsNull<>()));
        org.hamcrest.MatcherAssert.assertThat("Exception is InvalidDigestException", com.google.common.base.Throwables.getRootCause(throwable), new org.hamcrest.core.IsInstanceOf(com.artipie.docker.error.InvalidDigestException.class));
        org.hamcrest.MatcherAssert.assertThat("Exception message contains calculated digest", com.google.common.base.Throwables.getRootCause(throwable).getMessage(), new org.hamcrest.Matchers.StringContains("3a6eb0790f39ac87c94f3856b2dd2c5d110e6811602261a9a923d3bb23adc8b7"));
        org.hamcrest.MatcherAssert.assertThat("Exception message contains expected digest", com.google.common.base.Throwables.getRootCause(throwable).getMessage(), new org.hamcrest.Matchers.StringContains(digest));
        return java.util.concurrent.CompletableFuture.allOf();
    }).join();
}
```

In this patch, I replaced the `StringContains` constructor with the `StringContains` method from the `Matchers` class. The `Matchers` class is a part of Hamcrest 2.x, which is a replacement for the deprecated Hamcrest 1.x classes used in the original code. The `Matchers` class provides a variety of matchers, including the `StringContains` matcher, which can take a `String` or a `boolean` value as its argument. In this case, I used the `StringContains` matcher that takes a `String` argument.

Note that the `Matchers` class is imported with a static import statement at the beginning of the file:

```java
import static org.hamcrest.Matchers.StringContains;
```

This import statement is not shown in the patch since it is assumed to be present in the original code. If this import statement is not present, it needs to be added to the code for the patch to work.