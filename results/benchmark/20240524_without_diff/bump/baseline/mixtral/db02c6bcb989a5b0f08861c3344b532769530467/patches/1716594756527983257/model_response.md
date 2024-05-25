Here's a fixed version of the `failsOnDigestMismatch` method:

```java
@Test
void failsOnDigestMismatch() {
    final InMemoryStorage storage = new InMemoryStorage();
    final AstoBlobs blobs = new AstoBlobs(
            storage, new DefaultLayout(), new RepoName.Simple("any")
    );
    final String digest = "123";
    blobs.put(
            new CheckedBlobSource(new Content.From("data".getBytes()), new Digest.Sha256(digest))
    ).toCompletableFuture().handle(
            (blob, throwable) -> {
                Assertions.assertThat(throwable).isNotNull();
                Assertions.assertThat(throwable).isInstanceOf(InvalidDigestException.class);
                Assertions.assertThat(throwable.getMessage()).contains("3a6eb0790f39ac87c94f3856b2dd2c5d110e6811602261a9a923d3bb23adc8b7");
                Assertions.assertThat(throwable.getMessage()).contains(digest);
                return CompletableFuture.allOf();
            }
    ).join();
}
```

In this fixed version, I replaced the `MatcherAssert` class with `Assertions` from the `org.junit.jupiter.api` package. This package is a part of JUnit 5, which is a successor of JUnit 4.13. The `MatcherAssert` class is not present in JUnit 5, hence the original code didn't compile.

The `JUnit413StringContains` class was replaced with a lambda expression that uses the `contains` method from the `String` class.

Note that I didn't change the method signature or remove the `@Override` decorator, as it was not necessary. I also didn't introduce any new variables, as the code was easy to understand without them.