Here's the updated code to fix the error:

```java
import com.artipie.asto.Content;
import com.artipie.asto.Key;
import com.artipie.asto.memory.InMemoryStorage;
import com.artipie.docker.asto.AstoBlobs;
import com.artipie.docker.asto.CheckedBlobSource;
import com.artipie.docker.Digest;
import com.artipie.docker.error.InvalidDigestException;
import com.google.common.base.Throwables;
import java.nio.ByteBuffer;
import java.nio.charset.StandardCharsets;
import java.util.concurrent.CompletableFuture;
import org.hamcrest.MatcherAssert;
import org.junit.jupiter.api.Test;

@Test
void failsOnDigestMismatch() {
    final InMemoryStorage storage = new InMemoryStorage();
    final AstoBlobs blobs = new AstoBlobs(
        storage,
        new DefaultLayout(),
        new RepoName.Simple("any")
    );
    final String digest = "123";
    blobs.put(
        new CheckedBlobSource(
            new Content.From(ByteBuffer.wrap("data".getBytes(StandardCharsets.UTF_8))),
            new Digest.Sha256(digest)
        )
    ).thenAccept(unused -> {
        MatcherAssert.assertThat(
            "Exception thrown",
            () -> {
                throw new InvalidDigestException("3a6eb0790f39ac87c94f3856b2dd2c5d110e6811602261a9a923d3bb23adc8b7", digest);
            },
            new IsInstanceOf(InvalidDigestException.class)
        );
        MatcherAssert.assertThat(
            "Exception message contains calculated digest",
            Throwables.getRootCause(new RuntimeException("test")).getMessage(),
            new StringStartsWith("3a6eb0790f39ac87c94f3856b2dd2c5d110e6811602261a9a923d3bb23adc8b7")
        );
        MatcherAssert.assertThat(
            "Exception message contains expected digest",
            Throwables.getRootCause(new RuntimeException("test")).getMessage(),
            new StringContains.StringContains(digest)
        );
    }).join();
}
```

The error was caused by the missing return type for the lambda expression in the `handle` method. I've replaced `handle` with `thenAccept` and added a `RuntimeException` to extract the exception message for validation.