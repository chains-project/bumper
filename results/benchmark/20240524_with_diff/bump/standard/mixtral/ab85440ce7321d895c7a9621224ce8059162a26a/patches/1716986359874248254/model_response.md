Here's a possible patch for the given client code:

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
import com.artipie.docker.asto.DefaultLayout;
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
            new Content.From("data".getBytes(StandardCharsets.UTF_8)),
            new Digest.Sha256(digest)
        )
    ).thenAcceptAsync(blob -> {
        assertThat(
            "Exception thrown",
            Throwables.getRootCause(blob),
            not(nullValue())
        );
        assertThat(
            "Exception is InvalidDigestException",
            Throwables.getRootCause(blob),
            instanceOf(InvalidDigestException.class)
        );
        assertThat(
            "Exception message contains calculated digest",
            Throwables.getRootCause(blob).getMessage(),
            String.containsIgnoringCase("3a6eb0790f39ac87c94f3856b2dd2c5d110e6811602261a9a923d3bb23adc8b7")
        );
        assertThat(
            "Exception message contains expected digest",
            Throwables.getRootCause(blob).getMessage(),
            String.containsIgnoringCase(digest)
        );
    }).toCompletableFuture().join();
}
```

The changes I made are:

1. Replace `handle` method with `thenAcceptAsync` to avoid the need for a `CompletableFuture.allOf()`.
2. Replace `MatcherAssert.assertThat` with `assertThat` for brevity.
3. Use `String.containsIgnoringCase` instead of `StringContains` to match the new library version.
4. Replace `MatcherAssert.assertThat` with `assertThat` for brevity.
5. Replace `new StringContains(true, ...)` with `String.containsIgnoringCase(...)` to match the new library version.
6. Replace `new IsNull<>()` with `nullValue()` for brevity.
7. Replace `new IsInstanceOf(...)` with `instanceOf(...)` for brevity.
8. Replace `new StringContains(true, ...)` with `String.containsIgnoringCase(...)` to match the new library version.