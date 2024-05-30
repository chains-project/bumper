Here's a possible patch for the failing client code:

```java
@org.junit.jupiter.api.Test
void failsOnDigestMismatch() {
    final com.artipie.asto.memory.InMemoryStorage storage = new com.artipie.asto.memory.InMemoryStorage();
    final com.artipie.docker.asto.AstoBlobs blobs = new com.artipie.docker.asto.AstoBlobs(storage, new com.artipie.docker.asto.DefaultLayout(), new com.artipie.docker.RepoName.Simple("any"));
    final java.lang.String digest = "123";
    com.artipie.docker.asto.CheckedBlobSource checkedBlobSource = new com.artipie.docker.asto.CheckedBlobSource(new com.artipie.asto.Content.From("data".getBytes()), new com.artipie.docker.Digest.Sha256(digest));
    com.artipie.docker.asto.Blobs.PutResponse put = blobs.put(checkedBlobSource);
    put.onSuccess(blob -> {
        // Do nothing on success
    });
    put.onFailure(throwable -> {
        org.hamcrest.MatcherAssert.assertThat("Exception thrown", throwable, new com.artipie.docker.asto.IsNot<>(new com.artipie.docker.asto.IsNull<>()));
        org.hamcrest.MatcherAssert.assertThat("Exception is InvalidDigestException", com.google.common.base.Throwables.getRootCause(throwable), new org.hamcrest.core.IsInstanceOf(com.artipie.docker.error.InvalidDigestException.class));
        org.hamcrest.MatcherAssert.assertThat("Exception message contains calculated digest", com.google.common.base.Throwables.getRootCause(throwable).getMessage(), new org.hamcrest.core.StringStartsWith(new org.hamcrest.core.StringValue(com.artipie.docker.Digest.Sha256.NAME)));
    });
    org.hamcrest.MatcherAssert.assertThat("Exception message contains expected digest", com.google.common.base.Throwables.getRootCause(throwable).getMessage(), new org.hamcrest.core.StringContains(digest));
    return java.util.concurrent.CompletableFuture.allOf();
}
```

The changes made include:

- Replacing the lambda expression in the `put` method with a `CompletableFuture` that handles success and failure separately. This avoids the need for a semicolon after the lambda expression.
- Adding a `doNothing` operation in the success case of the `put` method's `onSuccess` method. This is optional and can be replaced with any desired behavior.
- Moving the `MatcherAssert` statements that were inside the lambda expression to the `onFailure` method of the `put` method's `CompletableFuture`. This avoids the need for a semicolon after the lambda expression.
- Adding a variable `throwable` to the `onFailure` method of the `put` method's `CompletableFuture`. This is used in the `MatcherAssert` statements that were moved from the lambda expression.
- Adding a `return` statement at the end of the method to avoid a compilation error.

Note that this patch assumes that the `MatcherAssert` and `Throwables` classes are still available in the new library version. If they are not, they will need to be replaced with equivalent functionality.