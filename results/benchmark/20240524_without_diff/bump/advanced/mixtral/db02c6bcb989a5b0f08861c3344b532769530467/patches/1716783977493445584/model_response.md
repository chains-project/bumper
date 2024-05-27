Here's a possible patch for the failing client code:

```java
import static org.hamcrest.MatcherAssert.assertThat;
import static org.hamcrest.Matchers.instanceOf;
import static org.hamcrest.Matchers.not;
import static org.hamcrest.Matchers.nullValue;
import java.nio.charset.StandardCharsets;
import java.util.concurrent.CompletableFuture;
import org.junit.jupiter.api.Test;
import com.artipie.asto.Content;
import com.artipie.asto.Memory;
import com.artipie.asto.Storage;
import com.artipie.docker.asto.AstoBlobs;
import com.artipie.docker.asto.CheckedBlobSource;
import com.artipie.docker.Digest;
import com.artipie.docker.RepoName;
import com.artipie.docker.error.InvalidDigestException;
import com.google.common.base.Throwables;

@Test
void failsOnDigestMismatch() {
    final Storage storage = new Memory.InMemoryStorage();
    final AstoBlobs blobs = new AstoBlobs(
        storage,
        new DefaultLayout(),
        new RepoName.Simple("any")
    );
    final String digest = "123";
    blobs.put(
        new CheckedBlobSource(
            Content.From("data".getBytes(StandardCharsets.UTF_8)),
            new Digest.Sha256(digest)
        )
    ).toCompletableFuture()
        .handle(
            (blob, throwable) -> {
                assertThat("Exception thrown", throwable, not(nullValue()));
                assertThat("Exception is InvalidDigestException", throwable, instanceOf(InvalidDigestException.class));
                final String message = Throwables.getRootCause(throwable).getMessage();
                assertThat(
                    "Exception message contains calculated digest",
                    message,
                    new StringContains("3a6eb0790f39ac87c94f3856b2dd2c5d110e6811602261a9a923d3bb23adc8b7")
                );
                assertThat(
                    "Exception message contains expected digest",
                    message,
                    new StringContains(digest)
                );
                return CompletableFuture.allOf();
            }
        )
        .join();
}

static class StringContains extends org.hamcrest.core.StringContains {
    StringContains(boolean sensitive, String substring) {
        super(substring);
        this.sensitive = sensitive;
    }

    @Override
    protected boolean matchSubstring(String substring) {
        return sensitive ? super.matchSubstring(substring) : substring.contains(this.substring);
    }

    private final boolean sensitive;
}
```

The patch includes a new implementation of the `StringContains` matcher that accepts a boolean flag indicating whether the substring comparison should be case-sensitive. This allows the original test to pass without modifying the external dependency that introduced the compilation error.