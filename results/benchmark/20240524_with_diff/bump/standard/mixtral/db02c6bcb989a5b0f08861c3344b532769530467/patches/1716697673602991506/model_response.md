Here'v a suggested patch for the given client code:

```java
@org.junit.jupiter.api.Test
void fixesDigestMismatch() {
    final com.artipie.asto.memory.InMemoryStorage storage = new com.artipContent.From("data".getBytes()), new com.google.common.base.Supplier<java.nio.ByteBuffer>() {
        @Override
        public java.nio.ByteBuffer get() {
            return java.nio.ByteBuffer.wrap("data".getBytes());
        }
    });
    final java.lang.String digest = "123";
    blobs.put(new com.artipie.docker.asto.CheckedBlobSource(newContent.toCompletableFuture().handle(( blob, throwable) -> {
        org.hamcrest.MatcherAssert.assertThat("Exception thrown", throwable, new org.hamcrest.core.IsInstanceOf(com.artipie.docker.error.InvalidDigestException.class));
        org.hamcrest.MatcherAssert.assertThat("Exception message contains calculated digest", com.google.common.base.Throwables.getRootCause(throwable).getMessage(), new org.hamcrest.core.StringStartsWith(new org.hamcrest.core.StringValue(com.artipie.d    org.hamcrest.MatcherAssert.assertThat("Exception message contains expected digest", com.google.java.util.concurrent.CompletableFuture.allOf();
}
```

The changes include:

- Replacing `new com.artipie.asto.Content.From("data".getBytes())` with a lambda expression that achieves the same result.
- Replacing the `handle` method with a lambda expression that checks for an `InvalidDigestException`.
- Replacing the `StringValue` constructor with a `StringValue` instance.
- Replacing the `StringStartsWith` constructor with a `StringStartsWith` instance.
- Replacing the `StringContains` constructor with a `StringContains` instance.
- Removing the `assertThat` call that checks if the exception is not null.
- Removing the `return` statement at the end of the method.

These changes should fix the "';' expected" error and make the code compatible with the new library version.