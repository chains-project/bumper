Here's a possible patch for the given code. This patch creates a new `JUnit413StringContains` instance for each assertion which should resolve the compilation error.

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
                MatcherAssert.assertThat(
                        "Exception thrown",
                        throwable,
                        new IsNot<>(new IsNull<>())
                );
                MatcherAssert.assertThat(
                        "Exception is InvalidDigestException",
                        Throwables.getRootCause(throwable),
                        new IsInstanceOf(InvalidDigestException.class)
                );
                MatcherAssert.assertThat(
                        "Exception message contains calculated digest",
                        Throwables.getRootCause(throwable).getMessage(),
                        new JUnit413StringContains("3a6eb0790f39ac87c94f3856b2dd2c5d110e6811602261a9a923d3bb23adc8b7")
                );
                MatcherAssert.assertThat(
                        "Exception message contains expected digest",
                        Throwables.getRootCause(throwable).getMessage(),
                        new JUnit413StringContains(digest)
                );
                return CompletableFuture.allOf();
            }
    ).join();
}

private static class JUnit413StringContains extends BaseMatcher<String, String> {
    private final String substring;

    private JUnit413StringContains(String substring) {
        this.substring = substring;
    }

    @Override
    public boolean matches(String s) {
        return s.contains(substring);
    }

    @Override
    public void describeTo(Description description) {
        description.appendText("a string containing ").appendValue(substring);
    }

    @Override
    public void describeMismatch(String s, Description description) {
        description.appendText("was ").appendValue(s);
    }
}
```

This patch introduces a new `JUnit413StringContains` class that extends `BaseMatcher`. This new class is used for the `MatcherAssert.assertThat` calls instead of the original `JUnit413StringContains` class.