Here's a possible patch for the code:

```java
import static org.hamcrest.MatcherAssert.assertThat;
import static org.hamcrest.Matchers.instanceOf;
import static org.hamcrest.Matchers.not;
import static org.hamcrest.Matchers.nullValue;
import java.nio.charset.StandardCharsets;
import java.util.concurrent.CompletableFuture;
import org.junit.jupiter.api.Test;
import com.artipie.asto.Content;
import com.artipie.asto.Key;
import com.artipie.asto.MemoryStorage;
import com.artipie.asto.ext.BlobSource;
import com.artipie.asto.ext.CheckedBlobSource;
import com.artipie.asto.ext.Layouts;
import com.artipie.docker.Digest;
import com.artipie.docker.RepoName;
import com.artipie.docker.asto.AstoBlobs;
import com.google.common.base.Throwables;

@Test
void failsOnDigestMismatch() {
    final MemoryStorage storage = new MemoryStorage();
    final AstoBlobs blobs = new AstoBlobs(
        storage, Layouts.singleTar(), new RepoName.Simple("any")
    );
    final String digest = "123";
    blobs.put(
        new CheckedBlobSource(
            new Content.From("data".getBytes(StandardCharsets.UTF_8)),
            new Digest.Sha256(digest)
        )
    ).toCompletableFuture().handle(
        (blob, throwable) -> {
            assertThat(throwable, not(nullValue()));
            assertThat(throwable, instanceOf(InvalidDigestException.class));
            final String message = Throwables.getRootCause(throwable).getMessage();
            assertThat(
                message,
                not(not(new StringContains("3a6eb0790f39ac87c94f3856b2dd2c5d110e6811602261a9a923d3bb23adc8b7")))
            );
            assertThat(message, new StringContains(digest));
            return CompletableFuture.allOf();
        }
    ).join();
}

class StringContains implements org.hamcrest.Matcher<String> {
    private final boolean contains;
    private final String substring;

    StringContains(boolean contains, String substring) {
        this.contains = contains;
        this.substring = substring;
    }

    @Override
    public boolean matches(final String s) {
        return contains
            ? s.contains(substring)
            : !s.contains(substring);
    }

    public void describeTo(org.hamcrest.Description description) {
        description.appendText("a string");
        description.appendText(contains ? " containing " : " not containing ");
        description.appendText(substring);
    }
}
```

The patch introduces a new `StringContains` matcher that accepts a boolean flag indicating whether the matcher should look for the presence or absence of the substring. This allows the original `StringContains` matcher to be used with a single argument.

The patch also uses static imports to simplify the code and avoids using the removed `com.artipie.docker.asto.IsNot` and `com.artipie.docker.asto.IsNull` matchers. Instead, the `not` matcher from Hamcrest is used.

Finally, the patch uses the `Content.From` constructor that accepts a byte array instead of a string, and uses `StandardCharsets.UTF_8` instead of assuming that the string is encoded in the platform default encoding. This ensures that the code is more portable and less likely to fail due to encoding issues.