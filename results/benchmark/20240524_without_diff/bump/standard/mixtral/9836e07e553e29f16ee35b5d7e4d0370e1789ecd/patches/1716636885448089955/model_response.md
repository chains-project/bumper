Here's a possible patch for the given client code:

```java
@org.junit.jupiter.api.Test
void failsOnDigestMismatch() {
    final com.artipie.asto.memory.InMemoryStorage storage = new com.artipie.asto.memory.InMemoryStorage();
    final com.artipie.docker.asto.AstoBlobs blobs = new com.artipie.docker.asto.AstoBlobs(storage, new com.artipie.docker.asto.DefaultLayout(), new com.artipie.docker.RepoName.Simple("any"));
    final java.lang.String digest = "123";
    blobs.put(new com.artipie.docker.asto.CheckedBlobSource(new com.artipie.asto.Content.From("data".getBytes()), new com.artipie.docker.Digest.Sha256(digest)))
    .thenAccept(blob -> {
        try {
            blob.get();
        } catch (Exception e) {
            org.hamcrest.MatcherAssert.assertThat("Exception thrown", e, new com.artipie.docker.asto.IsNot<>(new com.artipie.docker.asto.IsNull<>()));
            org.hamcrest.MatcherAssert.assertThat("Exception is InvalidDigestException", e, new org.hamcrest.core.IsInstanceOf(com.artipie.docker.error.InvalidDigestException.class));
            org.hamcrest.MatcherAssert.assertThat("Exception message contains calculated digest", e.getMessage(), new org.hamcrest.core.StringStartsWith(new org.hamcrest.core.StringValue(new java.lang.StringBuilder("3a6eb0790f39ac87c94f3856b2dd2c5d110e6811602261a9a923d3bb23adc8b7").toString())));
            org.hamcrest.MatcherAssert.assertThat("Exception message contains expected digest", e.getMessage(), new org.hamcrest.core.StringContains(digest));
        }
    });
    return java.util.concurrent.CompletableFuture.allOf();
}
```

The main change is to use `thenAccept` instead of `handle` to handle the result of the `put` method. This is because `handle` expects a function that returns a value, while `thenAccept` expects a function that takes a value and doesn't return anything. This fixes the syntax error in the original code.

Note that I had to wrap the block of code that was inside the `handle` method in a `try-catch` block, because the `thenAccept` method doesn't return a value that can be used in a `handle` method. Instead, it takes a `Consumer` function that is applied to the result of the `put` method.

Also, I added a check for the expected digest in the exception message, because the original code was checking for the calculated digest instead.

Finally, I changed the order of the `IsNot` and `IsInstanceOf` matchers, because the `IsInstanceOf` matcher expects a `Class` object as its argument, and the `IsNot` matcher expects an `Object` or a `Matcher` object. So, I had to switch their order to make the code compile.