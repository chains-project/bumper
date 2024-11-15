Here's a possible patch for the given client code:

```java
import static org.hamcrest.MatcherAssert.assertThat;
import static org.hamcrest.Matchers.instanceOf;
import static org.hamcrest.Matchers.not;
import static org.hamcrest.core.IsEqual.equalTo;
import java.nio.charset.StandardCharsets;
import java.util.concurrent.CompletableFuture;
import org.junit.jupiter.api.Test;
import com.artipie.asto.Content;
import com.artipie.asto.CheckedBlobSource;
import com.artipie.asto.MemoryStorage;
import com.artipie.asto.ext.ExtendedContent;
import com.artipie.asto.storage.Storage;
import com.artipie.docker.Digest;
import com.artipie.docker.asto.AstoBlobs;
import com.artipie.docker.asto.DefaultLayout;
import com.artipie.docker.error.InvalidDigestException;
import com.google.common.base.Throwables;

@Test
void failsOnDigestMismatch() {
    final Storage storage = new MemoryStorage();
    final AstoBlobs blobs = new AstoBlobs(
        storage,
        new DefaultLayout(),
        new com.artipie.docker.RepoName.Simple("any")
    );
    final String digest = "123";
    final Content content = new ExtendedContent.From(
        "data".getBytes(StandardCharsets.UTF_8),
        storage
    );
    final Digest calculatedDigest = Digest.sha256("3a6eb0790f39ac87c94f3856b2dd2c5d110e6811602261a9a923d3bb23adc8b7");
    blobs.put(
        new CheckedBlobSource(content, calculatedDigest)
    ).toCompletableFuture().handle(
        (blob, throwable) -> {
            assertThat("Exception thrown", throwable, not(equalTo(null)));
            assertThat("Exception is InvalidDigestException", throwable, instanceOf(InvalidDigestException.class));
            assertThat(
                "Exception message contains calculated digest",
                Throwables.getRootCause(throwable).getMessage(),
                StringContains.containsString(calculatedDigest.value())
            );
            assertThat(
                "Exception message contains expected digest",
                Throwables.getRootCause(throwable).getMessage(),
                StringContains.containsString(digest)
            );
            return CompletableFuture.allOf();
        }
    ).join();
}

private static class StringContains extends org.hamcrest.Matcher<String> {
    private final String contains;

    private StringContains(String contains) {
        this.contains = contains;
    }

    public static org.hamcrest.Matcher<String> containsString(String contains) {
        return new StringContains(contains);
    }

    @Override
    public boolean matches(Object item) {
        return item != null && ((String) item).contains(contains);
    }

    @Override
    public void describeTo(org.hamcrest.Description description) {
        description.appendText("a string containing ").appendValue(contains);
    }
}
```

In this patch, I created a new class `StringContains` that extends `org.hamcrest.Matcher<String>` and provides a custom `matches` method that checks if a given string contains a specified substring. This new class is then used in the test method to check the exception message.

Note that this patch assumes that the `StringContains.containsString` method is used instead of `org.hamcrest.core.StringContains.containsString` to create a new `StringContains` instance. If the original `StringContains` class is used, the patch will not work.