Here is a possible patch for the given code:
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
                assertTrue(throwable != null);
                assertTrue(throwable instanceof InvalidDigestException);
                assertTrue(Throwables.getRootCause(throwable).getMessage().contains("3a6eb0790f39ac87c94f3856b2dd2c5d110e6811602261a9a923d3bb23adc8b7"));
                assertTrue(Throwables.getRootCause(throwable).getMessage().contains(digest));
                return CompletableFuture.allOf();
            }
    ).join();
}
```
The changes I made are:

* Replace `MatcherAssert.assertThat` with `assertTrue` and `new IsNot<>(new IsNull<>())` with `throwable != null`, `new IsInstanceOf(InvalidDigestException.class)` with `throwable instanceof InvalidDigestException`, `new JUnit413StringContains("3a6eb0790f39ac87c94f3856b2dd2c5d110e6811602261a9a923d3bb23adc8b7")` with `Throwables.getRootCause(throwable).getMessage().contains("3a6eb0790f39ac87c94f3856b2dd2c5d110e6811602261a9a923d3bb23adc8b7")`, and `new JUnit413StringContains(digest)` with `Throwables.getRootCause(throwable).getMessage().contains(digest)`. This is because the `MatcherAssert.assertThat` method is not available in the code, and the `assertTrue` method can be used instead to check if a condition is true.
* Remove the `Override` decorator from the method, as the method is not overriding any method in the new version.
* Add the `import static org.junit.Assert.assertTrue.` statement at the beginning of the file to use the `assertTrue` method.

Note that this patch assumes that the `Throwables` class and the `InvalidDigestException` class are available in the code. If not, you may need to import them or define them before using them in the code.