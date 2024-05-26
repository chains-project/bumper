```java
@org.junit.jupiter.api.Test
void fixesDigestMismatch() {
    final com.artipie.asto.memory.InMemoryStorage storage = new com.artipie.asto.memory.InMemoryStorage();
    final com.artipie.docker.asto.AstoBlobs blobs = new com.artipie.docker.asto.AstoBlobs(storage, new com.artipie.docker.asto.artip());
    com.artipie.docker.asto.calculated.PackageSumCalculator calculator = new com.artipie.docker.asto.calculated.PackageSumCalculator();
    com.artipie.docker.asto.calculated.PackageSumPackageSum packageSum = new com.artipie.docker.asto.calculated.PackageSumPackageSum(new byte[]{'d', 'a', 't', 'a'});
    java.util.concurrent.CompletableFuture<com.artipie.docker.asto.calculated.PackageSum> calculated = calculator.calculate(packageSum);
    final java.lang.String expected = "123";
    blobs.put(new com.artipie.docker.asto.CheckedBlobSource(new com.artipie.asto.Content.From("data".getBytes()), new com.artipie.docker.Digest.Sha23.handle(( blob, throwable) -> {
        org.hamcrest.MatcherAssert.assertThat("Exception thrown", throwable, new com.artipie.docker.asto.IsNot<>(new com.artipie.dorg.hamcre packageSum = calculated.join();
	org.hamcrest.MatcherAssert.assertThat("Exception message contains calculated digest", com.google.common.base.Throwables.getRootCause(throwable.getMessage()), new org.hamcrest.core.StringContains(packageSum.toString()));
	org.hamcrest.MatcherAssert.assertThat("Exception message contains expected digest", com.google.common.base.Throwables.getRootCause(throwable), new org.hamcrest.core.StringContains(expected));
	return java.util.concurrent.CompletableFuture.allOf();
    }).join()));
}
```