Here's the updated code that should fix the error:

```java
import com.artipie.asto.Content;
import com.artipie.asto.CheckedBlobSource;
import com.artipie.asto.memory.InMemoryStorage;
import com.artipie.docker.asto.AstoBlobs;
import com.artipie.docker.asto.DefaultLayout;
import com.artipie.docker.Digest;
import com.artipie.docker.CheckedBlobWriter;
import com.artipie.docker.asto.IsNot;
import com.artipie.docker.asto.IsNull;
import com.artipie.docker.RepoName;
import com.artipie.docker.error.InvalidDigestException;
import com.google.common.base.Throwables;
import java.nio.charset.StandardCharsets;
import java.util.concurrent.CompletableFuture;
import java.util.concurrent.ExecutionException;
import org.hamcrest.MatcherAssert;
import static org.hamcrest.CoreMatchers.instanceOf;
import static org.hamcrest.CoreMatchers.startsWith;
import static org.hamcrest.MatcherAssert.assertThat;
import static org.junit.jupiter.api.Assertions.assertThrows;

@org.junit.jupiter.api.Test
void failsOnDigestMismatch() {
    final InMemoryStorage storage = new InMemoryStorage();
    final AstoBlobs blobs = new AstoBlobs(storage, new DefaultLayout(), new RepoName.Simple("any"));
    final String digest = "123";
    assertThrows(InvalidDigestException.class, () -> {
        blobs.put(new CheckedBlobSource(Content.From("data".getBytes()), new Digest.Sha256(digest)), new CheckedBlobWriter())
            .toCompletableFuture()
            .join();
    });
    final ExecutionException exception = assertThrows(ExecutionException.class, () -> {
        blobs.put(new CheckedBlobSource(Content.From("data".getBytes()), new Digest.Sha256(digest)))
            .toCompletableFuture()
            .get();
    });
    final Throwable rootCause = Throwables.getRootCause(exception);
    MatcherAssert.assertThat("Exception thrown", rootCause, new IsNot<>(new IsNull<>()));
    MatcherAssert.assertThat("Exception is InvalidDigestException", rootCause, new instanceOf(InvalidDigestException.class));
    MatcherAssert.assertThat("Exception message contains calculated digest", rootCause.getMessage(), new startsWith(true, "3a6eb0790f39ac87c94f3856b2dd2c5d110e6811602261a9a923d3bb23adc8b7"));
    MatcherAssert.assertThat("Exception message contains expected digest", rootCause.getMessage(), new startsWith(true, digest));
}
```

In the updated code, I have replaced `StringContains` with `startsWith` and changed the way exceptions are handled to avoid the error. I have also changed the order of imports to avoid conflicts.