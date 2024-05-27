Here's a suggested patch for the failing client code:

```java
import static org.hamcrest.MatcherAssert.assertThat;
import static org.hamcrest.Matchers.instanceOf;
import static org.hamcrest.Matchers.notNullValue;
import static org.hamcrest.core.IsEqual.equalTo;
import java.nio.ByteBuffer;
import java.util.concurrent.CompletableFuture;
import org.junit.jupiter.api.Test;
import com.artipie.asto.Content;
import com.artipie.asto.Key;
import com.artipie.asto.memory.InMemoryStorage;
import com.artipie.docker.asto.AstoBlobs;
import com.artipie.docker.asto.CheckedBlobSource;
import com.artipie.docker.Digest;
import com.artipie.docker.RepoName;
import com.artipie.docker.error.InvalidDigestException;

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
            Content.From(ByteBuffer.wrap("data".getBytes())),
            new Digest.Sha256(digest)
        )
    ).toCompletableFuture()
    .handle(
        (blob, throwable) -> {
            assertThat(throwable, notNullValue());
            assertThat(throwable, instanceOf(InvalidDigestException.class));
            InvalidDigestException exception = (InvalidDigestException) throwable;
            assertThat(
                exception.message(),
                equalTo(String.format("Content digest mismatch: expected '%s', calculated '%s'", digest, exception.calculatedDigest()))
            );
            return CompletableFuture.allOf();
        }
    ).join();
}
```

In this patch, I've replaced the `StringContains` matcher with `IsEqual` and used a custom message for the `InvalidDigestException`. This should resolve the compilation error.