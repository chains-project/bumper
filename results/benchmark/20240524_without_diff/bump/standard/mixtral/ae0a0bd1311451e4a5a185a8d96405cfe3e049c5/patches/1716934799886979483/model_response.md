Here's a fixed version of your code:

```java
import com.artipie.asto.CheckedBlobSource;
import com.artipie.asto.Content;
import com.artipie.asto.MemoryStorage;
import com.artipie.asto.RepoName;
import com.artipie.asto.Storage;
import com.artipie.asto.TarContent;
import com.artipie.docker.Digest;
import com.artipie.docker.DefaultLayout;
import com.artipie.docker.asto.AstoBlobs;
import com.artipie.docker.asto.IsNotNull;
import com.artipie.docker.asto.IsNull;
import com.artipie.docker.error.InvalidDigestException;
import com.google.common.base.Throwables;
import java.nio.ByteBuffer;
import java.nio.charset.StandardCharsets;
import java.util.concurrent.CompletableFuture;
import org.hamcrest.MatcherAssert;
import org.junit.jupiter.api.Test;
import static com.artipie.docker.asto.IsNot.not;
import static org.hamcrest.CoreMatchers.instanceOf;
import static org.hamcrest.CoreMatchers.stringContainsInOrder;
import static org.hamcrest.MatcherAssert.assertThat;

@Test
void failsOnDigestMismatch() {
    final Storage storage = new MemoryStorage();
    final AstoBlobs blobs = new AstoBlobs(storage, new DefaultLayout(), new RepoName.Simple("any"));
    final String digest = "123";
    blobs.put(new CheckedBlobSource(
        Content.from(TarContent.tar(ByteBuffer.wrap("data".getBytes()), StandardCharsets.UTF_8)),
        new Digest.Sha256(digest)))
        .toCompletableFuture()
        .handle((blob, throwable) -> {
            assertThat("Exception thrown", throwable, not(new IsNull<>()));
            assertThat("Exception is InvalidDigestException", throwable, instanceOf(InvalidDigestException.class));
            assertThat(
                "Exception message contains calculated digest",
                Throwables.getRootCause(throwable).getMessage(),
                stringContainsInOrder(
                    "3a6eb0790f39ac87c94f3856b2dd2c5d110e6811602261a9a923d3bb23adc8b7"
                )
            );
            assertThat(
                "Exception message contains expected digest",
                Throwables.getRootCause(throwable).getMessage(),
                stringContainsInOrder(digest)
            );
            return CompletableFuture.allOf();
        })
        .join();
}
```

Changes made:

1. Replaced `com.artipie.docker.asto.IsNot` with `com.artipie.docker.asto.IsNot.not`
2. Replaced `org.hamcrest.core.StringContains` with `org.hamcrest.MatcherAssert.stringContainsInOrder`

These changes should fix the compilation error you encountered.