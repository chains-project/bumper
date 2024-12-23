Here's a fixed version of the code that should resolve the error:

```java
@org.junit.jupiter.api.Test
void failsOnDigestMismatch() {
    final com.artipie.asto.memory.InMemoryStorage storage = new com.artipie.asto.memory.InMemoryStorage();
    final com.artipie.docker.asto.AstoBlobs blobs = new com.artipie.docker.asto.AstoBlobs(storage, new com.artipie.docker.asto.DefaultLayout(), new com.artipie.docker.RepoName.Simple("any"));
    final java.lang.String digest = "123";
    blobs.put(new com.artipie.docker.asto.CheckedBlobSource(new com.artipie.asto.Content.From("data".getBytes()), new com.artipie.docker.Digest.Sha256(digest))).toCompletableFuture().handle(( blob, throwable) -> {
        org.hamcrest.MatcherAssert.assertThat("Exception thrown", throwable, new com.artipie.docker.asto.IsNot<>(new com.artipie.docker.asto.IsNull<>()));
        org.hamcrest.MatcherAssert.assertThat("Exception is InvalidDigestException", com.google.common.base.Throwables.getRootCause(throwable), new org.hamcrest.Matcher(new org.hamcrest.description.Description(), new org.hamcrest.core.IsInstanceOf(com.artipie.docker.error.InvalidDigestException.class), new org.hamcrest.Matcher<org.hamcrest.Matcher<? super org.hamcrest.Matcher<? super Throwable>>>(){
            @Override
            public boolean matches(Object item) {
                return item instanceof InvalidDigestException;
            }

            @Override
            public void describeTo(Description description) {
                description.appendText("Exception is InvalidDigestException");
            }

            @Override
            public void describeMismatch(Object item, Description description) {
                description.appendText("was ").appendValue(item);
            }
        }));
        org.hamcrest.MatcherAssert.assertThat("Exception message contains calculated digest", com.google.common.base.Throwables.getRootCause(throwable).getMessage(), new org.hamcrest.core.StringStartsWith("3a6eb0790f39ac87c94f3856b2dd2c5d110e6811602261a9a923d3bb23adc8b7"));
        org.hamcrest.MatcherAssert.assertThat("Exception message contains expected digest", com.google.common.base.Throwables.getRootCause(throwable).getMessage(), new org.hamcrest.core.StringContains(digest));
        return java.util.concurrent.CompletableFuture.allOf();
    }).join();
}
```

The changes made are:

* Replaced the `StringContains` constructor with a custom `Matcher` that checks for `InstanceOf` and `StringStartsWith` instead of `StringContains`.
* Added a custom `Matcher` implementation that checks for `InstanceOf` and `StringContains`.
* Removed the `true` argument from the `StringContains` matcher.

These changes should resolve the compilation error and allow the code to run successfully.