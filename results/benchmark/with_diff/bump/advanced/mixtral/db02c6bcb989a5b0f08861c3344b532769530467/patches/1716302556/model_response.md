Here's a fixed version of the code that should work with the new library version:

```java
@org.junit.jupiter.api.Test
void failsOnDigestMismatch() {
    final com.artipie.asto.memory.InMemoryStorage storage = new com.artipie.asto.memory.InMemoryStorage();
    final com.artipie.docker.asto.AstoBlobs blobs = new com.artipie.docker.asto.AstoBlobs(storage, new com.artipie.docker.asto.DefaultLayout(), new com.artipie.docker.RepoName.Simple("any"));
    final java.lang.String digest = "123";
    blobs.put(new com.artipie.docker.asto.CheckedBlobSource(new com.artipie.asto.Content.From("data".getBytes()), new com.artipie.docker.Digest.Sha256(digest))).toCompletableFuture().handle(( blob, throwable) -> {
        org.hamcrest.MatcherAssert.assertThat("Exception thrown", throwable, new com.artipie.docker.asto.IsNot<>(new com.artipie.docker.asto.IsNull<>()));
        org.hamcrest.MatcherAssert.assertThat("Exception is InvalidDigestException", com.google.common.base.Throwables.getRootCause(throwable), new org.hamcrest.Matcher(new org.hamcrest.description.Description(), new org.hamcrest.BaseMatcher<Throwable>() {
            @Override
            public boolean matches(Object item) {
                return item instanceof com.artipie.docker.error.InvalidDigestException;
            }

            @Override
            public void describeTo(org.hamcrest.Description description) {
                description.appendText("Exception is InvalidDigestException");
            }
        }));
        org.hamcrest.MatcherAssert.assertThat("Exception message contains calculated digest", com.google.common.base.Throwables.getRootCause(throwable).getMessage(), new org.hamcrest.core.StringStartsWith(new org.hamcrest.description.Description(), "3a6eb0790f39ac87c94f3856b2dd2c5d110e6811602261a9a923d3bb23adc8b7"));
        org.hamcrest.MatcherAssert.assertThat("Exception message contains expected digest", com.google.common.base.Throwables.getRootCause(throwable).getMessage(), new org.hamcrest.core.StringContains(new org.hamcrest.description.Description(), digest));
        return java.util.concurrent.CompletableFuture.allOf();
    })
    .join();
}
```

The changes I made are:

* Replace `new org.hamcrest.core.StringContains(true, "3a6eb0790f39ac87c94f3856b2dd2c5d110e6811602261a9a923d3bb23adc8b7")` with `new org.hamcrest.core.StringStartsWith(new org.hamcrest.description.Description(), "3a6eb0790f39ac87c94f3856b2dd2c5d110e6811602261a9a923d3bb23adc8b7")`
* Replace `new org.hamcrest.core.StringContains(true, digest)` with `new org.hamcrest.core.StringContains(new org.hamcrest.description.Description(), digest)`
* Replace `new org.hamcrest.core.IsInstanceOf(com.artipie.docker.error.InvalidDigestException.class)` with a custom matcher that checks if the throwable is an instance of `com.artipie.docker.error.InvalidDigestException`.

These changes are necessary because the `StringContains` constructor now requires a `Description` object instead of a boolean value, and the `IsInstanceOf` constructor has been removed. The custom matcher for `IsInstanceOf` is needed because the library no longer provides a built-in matcher for checking if an object is an instance of a specific class.