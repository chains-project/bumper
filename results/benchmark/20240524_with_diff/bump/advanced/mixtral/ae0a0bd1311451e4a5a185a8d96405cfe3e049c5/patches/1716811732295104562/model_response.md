Here's a fixed version of the failing method. I added a custom Hamcrest matcher `IsStringContains` for the `StringContains` matcher, which now requires a single argument instead of two.

```java
import org.hamcrest.Description;
import org.hamcrest.Factory;
import org.hamcrest.Matcher;
import org.hamcrest.TypeSafeMatcher;

@org.junit.jupiter.api.Test
void failsOnDigestMismatch() {
    final com.artipie.asto.memory.InMemoryStorage storage = new com.artipie.asto.memory.InMemoryStorage();
    final com.artipie.docker.asto.AstoBlobs blobs = new com.artipie.docker.asto.AstoBlobs(storage, new com.artipie.docker.asto.DefaultLayout(), new com.artipie.docker.RepoName.Simple("any"));
    final java.lang.String digest = "123";
    blobs.put(new com.artipie.docker.asto.CheckedBlobSource(new com.artipie.asto.Content.From("data".getBytes()), new com.artipie.docker.Digest.Sha256(digest))).toCompletableFuture().handle(( blob, throwable) -> {
        org.hamcrest.MatcherAssert.assertThat("Exception thrown", throwable, new com.artipie.docker.asto.IsNot<>(new com.artipie.docker.asto.IsNull<>()));
        org.hamcrest.MatcherAssert.assertThat("Exception is InvalidDigestException", com.google.common.base.Throwables.getRootCause(throwable), new org.hamcrest.core.IsInstanceOf(com.artipie.docker.error.InvalidDigestException.class));
        org.hamcrest.MatcherAssert.assertThat("Exception message contains calculated digest", com.google.common.base.Throwables.getRootCause(throwable).getMessage(), new IsStringContains("3a6eb0790f39ac87c94f3856b2dd2c5d110e6811602261a9a923d3bb23adc8b7"));
        org.hamcrest.MatcherAssert.assertThat("Exception message contains expected digest", com.google.common.base.Throwables.getRootCause(throwable).getMessage(), new IsStringContains(digest));
        return java.util.concurrent.CompletableFuture.allOf();
    }).join();
}

private static class IsStringContains extends TypeSafeMatcher<String> {
    private final String substring;

    public IsStringContains(String substring) {
        super(String.class);
        this.substring = substring;
    }

    @Override
    protected boolean matchesSafely(String item) {
        return item.contains(substring);
    }

    @Override
    public void describeTo(Description description) {
        description.appendText("a string containing ").appendValue(substring);
    }

    @Factory
    public static Matcher<String> IsStringContains(String substring) {
        return new IsStringContains(substring);
    }
}
```

This solution creates a custom matcher `IsStringContains` that extends `TypeSafeMatcher<String>`. The `matchesSafely` method checks if the provided string contains the substring. The `describeTo` method provides a description for the matcher. The `IsStringContains` method is marked with `@Factory` and creates a new `IsStringContains` instance.