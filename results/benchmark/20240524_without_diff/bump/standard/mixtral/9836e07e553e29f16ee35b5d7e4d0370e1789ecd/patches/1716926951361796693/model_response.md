Here's a fixed version of the code:

```java
import com.artipie.asto.Content;
import com.artipie.asto.CheckedBlobSource;
import com.artipie.asto.MemoryStorage;
import com.artipie.asto.ext.ExtLeaderFollower;
import com.artipie.asto.storage.Storage;
import com.artipie.docker.Digest;
import com.artipie.docker.RepoName;
import com.artipie.docker.asto.AstoBlobs;
import com.artipie.docker.asto.CheckedBlob;
import com.artipie.docker.asto.DefaultLayout;
import com.artipie.docker.error.InvalidDigestException;
import com.google.common.base.Throwables;
import java.nio.ByteBuffer;
import java.nio.charset.StandardCharsets;
import java.util.concurrent.CompletableFuture;
import org.hamcrest.MatcherAssert;
import org.junit.jupiter.api.Test;
import static com.artipie.docker.asto.IsNot.not;
import static com.artipie.docker.asto.IsNot.nullness;
import static org.hamcrest.Matchers.instanceOf;
import static org.hamcrest.Matchers.stringContainsInOrder;

@Test
void failsOnDigestMismatch() {
    final Storage storage = new MemoryStorage();
    final AstoBlobs blobs = new AstoBlobs(
        new ExtLeaderFollower(storage),
        new DefaultLayout(),
        new RepoName.Simple("any")
    );
    final Digest digest = Digest.sha256("123");
    blobs.put(
        new CheckedBlobSource(
            new Content.From(ByteBuffer.wrap("data".getBytes(StandardCharsets.UTF_8))),
            new Digest.Sha256(digest)
        )
    ).toCompletableFuture().handle(
        (CheckedBlob<ByteBuffer> blob, Throwable throwable) -> {
            MatcherAssert.assertThat(
                "Exception thrown",
                throwable,
                not(nullness())
            );
            MatcherAssert.assertThat(
                "Exception is InvalidDigestException",
                throwable,
                instanceOf(InvalidDigestException.class)
            );
            MatcherAssert.assertThat(
                "Exception message contains calculated digest",
                Throwables.getRootCause(throwable).getMessage(),
                stringContainsInOrder(
                    "3a6eb0790f39ac87c94f3856b2dd2c5d110e6811602261a9a923d3bb23adc8b7"
                )
            );
            MatcherAssert.assertThat(
                "Exception message contains expected digest",
                Throwables.getRootCause(throwable).getMessage(),
                stringContainsInOrder(digest.encoded())
            );
            return CompletableFuture.allOf();
        }
    ).join();
}
```

The main change is the usage of `stringContainsInOrder` instead of `StringContains`. The former takes a `java.lang.Iterable` as an argument, while the latter takes a single `java.lang.String`. This should fix the compilation error.