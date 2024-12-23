Here's a possible patch for the failing client code:

```java
import static org.hamcrest.MatcherAssert.assertThat;
import static org.hamcrest.Matchers.instanceOf;
import static org.hamcrest.Matchers.not;
import static org.hamcrest.core.IsEqual.equalTo;
import java.nio.charset.StandardCharsets;
import java.util.concurrent.CompletableFuture;
import org.junit.jupiter.api.Test;
import com.artipie.asto.Content;
import com.artipie.asto.MemoryStorage;
import com.artipie.asto.ext.BlobLayout;
import com.artipie.asto.ext.Key;
import com.artipie.docker.Digest;
import com.artipie.docker.asto.CheckedBlobSource;
import com.artipie.docker.asto.AstoBlobs;
import com.artipie.docker.error.InvalidDigestException;
import com.google.common.base.Throwables;
import io.reactivex.Completable;

@Test
void failsOnDigestMismatch() {
    final MemoryStorage storage = new MemoryStorage();
    final AstoBlobs blobs = new AstoBlobs(storage, new BlobLayout(), new Key.Simple("any"));
    final String digest = "123";
    final Content content = Content.From("data".getBytes(StandardCharsets.UTF_8));
    blobs.put(new CheckedBlobSource(content, new Digest.Sha256(digest)))
        .toCompletableFuture()
        .handle(
            (blob, throwable) -> {
                assertThat("Exception thrown", throwable, not(equalTo(null)));
                assertThat("Exception is InvalidDigestException", throwable.getCause(), instanceOf(InvalidDigestException.class));
                final String message = throwable.getCause().getMessage();
                assertThat("Exception message contains calculated digest", message, not(not(new StringContains(message, "3a6eb0790f39ac87c94f3856b2dd2c5d110e6811602261a9a923d3bb23adc8b7"))));
                assertThat("Exception message contains expected digest", message, new StringContains(message, digest));
                return Completable.complete();
            }
        )
        .join();
}

class StringContains extends org.hamcrest.Matcher<String> {
    private final String substring;

    StringContains(String substring) {
        this.substring = substring;
    }

    @Override
    public boolean matches(Object item) {
        return ((String) item).contains(substring);
    }
}
```

This patch introduces a new `StringContains` class to work around the issue with the `StringContains` constructor in `org.hamcrest.core.StringContains`. It also simplifies the `handle` lambda expression by using `Completable.complete()` instead of `CompletableFuture.allOf()` and uses `throwable.getCause()` instead of `Throwables.getRootCause(throwable)`.