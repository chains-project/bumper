Here's the proposed patch for the failing client code:

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
import com.artipie.asto.ext.ExtendedMemory;
import com.artipie.asto.Key;
import com.artipie.asto.Storage;
import com.artipie.docker.Digest;
import com.artipie.docker.asto.AstoBlobs;
import com.artipie.docker.asto.CheckedBlobSource;
import com.artipie.docker.error.InvalidDigestException;
import com.google.common.base.Throwables;

@Test
void failsOnDigestMismatch() {
    final Storage storage = new ExtendedMemory(new Memory.InMem());
    final AstoBlobs blobs = new AstoBlobs(storage, new DefaultLayout(), new RepoName.Simple("any"));
    final String digest = "123";
    blobs.put(new CheckedBlobSource(
        new Content.From("data".getBytes(StandardCharsets.UTF_8)),
        new Digest.Sha256(digest)
    )).toCompletableFuture().handle((blob, throwable) -> {
        assertThat("Exception thrown", throwable, not(nullValue()));
        assertThat("Exception is InvalidDigestException", throwable, instanceOf(InvalidDigestException.class));
        String message = Throwables.getRootCause(throwable).getMessage();
        assertThat("Exception message contains calculated digest", message, new StringContains("3a6eb0790f39ac87c94f3856b2dd2c5d110e6811602261a9a923d3bb23adc8b7"));
        assertThat("Exception message contains expected digest", message, new StringContains(digest));
        return CompletableFuture.allOf();
    }).join();
}

interface StringContains extends org.hamcrest.Matcher<String> {
    StringContains contains(boolean ignoreCase, String substring);
}
```

The patch includes a new `StringContains` functional interface to resolve the error message. It also replaces the `com.google.common.base.Throwables.getRootCause` method with `Throwables.getRootCause` for brevity. Additionally, it imports some missing classes and interfaces.