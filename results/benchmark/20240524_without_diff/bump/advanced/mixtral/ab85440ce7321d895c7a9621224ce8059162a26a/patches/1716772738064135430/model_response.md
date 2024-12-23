Here's a possible patch for the given client code:

```java
import static org.hamcrest.MatcherAssert.assertThat;
import static org.hamcrest.Matchers.instanceOf;
import static org.hamcrest.Matchers.not;
import static org.hamcrest.Matchers.nullValue;
import java.nio.charset.StandardCharsets;
import java.util.concurrent.CompletableFuture;
import org.hamcrest.Matcher;
import org.junit.jupiter.api.Test;
import com.artipie.asto.Content;
import com.artipie.asto.Key;
import com.artipie.asto.Memory;
import com.artipie.asto.Storage;
import com.artipie.asto.ext.Ext;
import com.artipie.docker.asto.CheckedBlobSource;
import com.artipie.docker.asto.AstoBlobs;
import com.artipie.docker.asto.DefaultLayout;
import com.artipie.docker.Digest;
import com.artipie.docker.RepoName;
import com.google.common.base.Throwables;

@Test
void failsOnDigestMismatch() {
    final Storage storage = new Memory();
    final AstoBlobs blobs = new AstoBlobs(
        storage,
        new DefaultLayout(),
        new RepoName.Simple("any")
    );
    final String digest = "123";
    final Matcher<Throwable> notNullOrIsInstanceOf = not(nullValue()).and(instanceOf(InvalidDigestException.class));
    blobs.put(
        new CheckedBlobSource(
            Content.From("data".getBytes(StandardCharsets.UTF_8)),
            new Digest.Sha256(digest)
        )
    ).toCompletableFuture().handle(
        (blob, throwable) -> {
            assertThat("Exception thrown", throwable, notNullOrIsInstanceOf);
            assertThat(
                "Exception message contains calculated digest",
                Throwables.getRootCause(throwable).getMessage(),
                new StringContains("3a6eb0790f39ac87c94f3856b2dd2c5d110e6811602261a9a923d3bb23adc8b7")
            );
            assertThat(
                "Exception message contains expected digest",
                Throwables.getRootCause(throwable).getMessage(),
                new StringContains(digest)
            );
            return CompletableFuture.allOf();
        }
    ).join();
}

private static Matcher<String> stringContains(final String substring) {
    return new StringContains(substring);
}

private static class StringContains implements Matcher<String> {
    private final String substring;

    StringContains(final String substring) {
        this.substring = substring;
    }

    @Override
    public boolean matches(final Object item) {
        return item != null && ((String) item).contains(substring);
    }

    @Override
    public void describeTo(final org.hamcrest.Description description) {
        description.appendText("a string containing ").appendText(substring);
    }
}
```

The patch defines a new `StringContains` class that implements the `Matcher<String>` interface, and uses it instead of the `org.hamcrest.core.StringContains` class. The `StringContains` class takes a `substring` argument in its constructor, and checks whether the `item` argument contains the `substring` using the `contains` method of the `String` class.