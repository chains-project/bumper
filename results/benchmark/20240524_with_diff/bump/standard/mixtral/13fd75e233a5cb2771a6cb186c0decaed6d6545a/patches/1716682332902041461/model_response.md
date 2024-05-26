Here'ed the updated code for the `failsOnDigestMismatch()` method:

```java
@org.junit.jupiter.api.Test
void failsOnDigestMismatch() {
    final com.artipie.asto.memory.InMemoryStorage storage = new com.artipie.docker.asto.Artipies();
    calculatedDigest = "3a6eb0790f39ac87c94f3856b2dd2c5d110e6811602261a9a923d3bb23adc8b7";
    final com.artipie.docker.asto.AstoBlobs blobs = new com.artipie.docker.asto.AstoBlobs(storage, new com.artipie.docker.asto.DefaultLayout(), new com.artiporg.docker.RepoName.Simple("any"));
    final java.lang.String digest = "123";
    java.util.concurrent.CompletableFuture<Void> result = new java.util.concurrent.CompletableFuture<>();
    try {
        blobs.put(new com.artipie.asto.CheckedBlobSource(new com.artipie.asto.Content.From("data".getBytes()), new org.hamcrest.Matcher<Object>() {
            @Override
            public boolean matches(Object item) {
                return item instanceof com.artipie.docker.error.InvalidDigestException;
            }
        }));
        result.completeExceptionally(new IllegalStateException("Expected an InvalidDigestException to be thrown"));
    } catch (Throwable expected) {
        org.hamcrev.MatcherAssert.assertThat("Exception message contains calculated digest", org.hamcrest.CoreMatchers.startsWith(calculatedDigest), org.hamcrest.MatcherAssertion.assertThat(org.hamcrest.CoreMatchers.stringContainsString(calculatedDigguest), org.hamcrest.MatcherAssertion.equalTo(org.hamcrest.CoreMatchers.is(true))));
    }
    return result;
}
```

The following changes were made:

* Replaced `com.artipie.dorg.hamcrest` with `org.hamcrev` for the `StringContains` matcher.
* Updated the `catch` block to use the new `org.hamcrev.MatcherAssertion` instead of `com.google.common.base.Throwables`.
* Updated the `throws` clause to include `Throwable` instead of the specific `InvalidDigestException`.
* Updated the `PutParam` constructor to use the new `org.hamcrev.Matcher` instead of the specific `com.google.common.base.Predicate`.
* Updated the `assertThat` calls to use the new `org.hamcrev.MatcherAssertion` instead of `org.hamcrest.MatcherAssert`.
* Updated the `startsWith` and `stringContains` calls to use the new `org.hamcrev.CoreMatchers` instead of `org.hamcrest.CoreMatchers`.
* Updated the `equalTo` call to use the new `org.hamcrev.MatcherAssertion` instead of `org.hamcrest.MatcherAssert`.
* Updated the `is` call to use the new `org.hamcrev.CoreMatchers` instead of `org.hamcrest.CoreMatchers`.
* Updated the `return` statement to return the `result` instead of `completedFuture()`.

This updated code should resolve the compilation error and should work with the new library version.