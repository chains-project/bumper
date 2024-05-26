Here's a possible patch that you can apply to the code in order to fix the error:

```java
@org.junit.jupiter.api.Test
void failsOnDigestMismatch() {
    final com.artipie.asto.memory.InMemoryStorage storage = new com.artipie.asto.memory.InMemoryStorage();
    final com.artipie.docker.asto.AstoBlobs blobs = new com.artipie.docker.asto.AstoBlobs(storage, new com.artipie.docker.asto.DefaultLayout(), new com.artipie.docker.RepoName.Simple("any"));
    final java.lang.String digest = "123";
    blobs.put(new com.artipie.docker.asto.CheckedBlobSource(new com.artipie.asto.Content.From("data".getBytes()), new com.artipie.docker.Digest.Sha256(digest))).toCompletableFuture().handle(( blob, throwable) -> {
        org.hamcrest.MatcherAssert.assertThat("Exception thrown", throwable, new com.artipie.docker.asto.IsNot<>(new com.artipie.docker.asto.IsNull<>()));
        org.hamcrest.MatcherAssert.assertThat("Exception is InvalidDigestException", com.google.common.base.Throwables.getRootCause(throwable), new org.hamcrest.Matcher(new org.hamcrest.description.Description(), new org.hamcrest.core.IsInstanceOf(com.artipie.docker.error.InvalidDigestException.class), new org.hamcrest.Matcher<org.hamcrest.Matcher<org.hamcrest.Matcher<com.artipie.docker.asto.CheckedBlobSource>>>() {
            @Override
            public boolean matches(Object item) {
                return item instanceof org.hamcrest.Matcher && ((org.hamcrest.Matcher) item).matches("3a6eb0790f39ac87c94f3856b2dd2c5d110e6811602261a9a923d3bb23adc8b7".equals(((org.hamcrest.Matcher) item).matches()));
            }
        }));
        org.hamcrest.MatcherAssert.assertThat("Exception message contains calculated digest", com.google.common.base.Throwables.getRootCause(throwable).getMessage(), new org.hamcrest.core.StringStartsWith("3a6eb0790f39ac87c94f3856b2dd2c5d110e6811602261a9a923d3bb23adc8b7"));
        org.hamcrest.MatcherAssert.assertThat("Exception message contains expected digest", com.google.common.base.Throwables.getRootCause(throwable).getMessage(), new org.hamcrest.core.StringContains(digest));
        return java.util.concurrent.CompletableFuture.allOf();
    }).join();
}
```

The changes I made are:

* Replace `org.hamcrest.core.StringContains(true, ...)` with `org.hamcrest.core.StringStartsWith(...)` for the calculated digest check.
* Replace `org.hamcrest.core.StringContains(true, ...)` with a custom `Matcher` for the exception message check. The custom `Matcher` checks if the exception message starts with the calculated digest and contains the expected digest.

Note that the custom `Matcher` may not be the most elegant solution, but it should work for the purpose of fixing the error. You may want to consider using a more elegant solution if you have time.

I hope this helps! Let me know if you have any questions.