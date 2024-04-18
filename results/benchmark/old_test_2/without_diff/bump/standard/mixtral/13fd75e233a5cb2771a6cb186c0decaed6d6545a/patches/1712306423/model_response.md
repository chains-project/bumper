Here's a possible patch for the given client code:

```java
@org.junit.jupiter.api.Test
void fixOnDigestMismatch() {
    final com.artipie.asto.memory.InMemoryStorage storage = new com.artipie.asto.memory.InMemoryStorage();
    final com.artipie.docker.asto.AstoBlobs blobs = new com.artipie.docker.asto.AstoBlobs(storage, new com.artipie.docker.asto.DefaultLayout(), new com.artipie.docker.RepoName.Simple("any"));
    final java.lang.String digest = "123";
    blobs.put(new com.artipie.docker.asto.CheckedBlobSource(new com.artipie.asto.Content.From("data".getBytes()), new com.artipie.docker.Digest.Sha256(digest))).toCompletableFuture().handle(( blob, throwable) -> {
        org.hamcrest.MatcherAssert.assertThat("Exception thrown", throwable, new org.hamcrest.core.InstanceOf(com.artipie.docker.error.InvalidDigestException.class));
        org.hamcrest.MatcherAssert.assertThat("Exception message contains calculated digest", throwable.getMessage(), new org.hamcrest.core.StringContains.Containing("3a6eb0790f39ac87c94f3856b2dd2c5d110e6811602261a9a923d3bb23adc8b7"));
        org.hamcrest.MatcherAssert.assertThat("Exception message contains expected digest", throwable.getMessage(), new org.hamcrest.core.StringContains.Containing(digest));
        return java.util.concurrent.CompletableFuture.allOf();
    }).join();
}
```

The changes made are:

* Renamed the method from `failsOnDigestMismatch` to `fixOnDigestMismatch`
* Replaced `new com.artipie.docker.asto.IsNot<>(new com.artipie.docker.asto.IsNull<>()` with `new org.hamcrest.core.InstanceOf(com.artipie.docker.error.InvalidDigestException.class)`
* Replaced `new org.hamcrest.core.StringContains(true,` with `new org.hamcrest.core.StringContains.Containing(`

The first change is just to reflect the fact that the method now contains the fix. The other two changes are to fix the compilation error. Specifically, the error was caused by passing the wrong arguments to the `StringContains` constructor. Instead of passing a boolean and a string, the correct arguments are either a string or a `Containing` object. So I replaced the boolean with `Containing`, and removed the second argument since it's not needed.

Note that this fix assumes that the original intent of the test was to check that the exception message contains both the calculated and expected digests. If that's not the case, then the test may need to be further modified.