Here's the fixed version of the method, using a custom `StringContains` matcher instead of the one from Hamcrest, which seems to have been removed:

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
                new CustomStringContains("3a6eb0790f39ac87c94f3856b2dd2c5d110e6811602261a9a923d3bb23adc8b7")
            );
            MatcherAssert.assertThat(
                "Exception message contains expected digest",
                Throwables.getRootCause(throwable).getMessage(),
                new CustomStringContains(digest)
            );
            return CompletableFuture.allOf();
        }
    ).join();
}

private static class CustomStringContains implements ArgumentMatcher<String> {
    private final String expectedSubstring;

    public CustomStringContains(String expectedSubstring) {
        this.expectedSubstring = expectedSubstring;
    }

    @Override
    public boolean matches(String actual) {
        return actual.contains(expectedSubstring);
    }

    @Override
    public void describeTo(Description description) {
        description.appendText("a string containing ").appendValue(expectedSubstring);
    }
}
```

This version defines a `CustomStringContains` matcher, which checks if a given string contains a specified substring. It can be used in place of the removed `StringContains` matcher.