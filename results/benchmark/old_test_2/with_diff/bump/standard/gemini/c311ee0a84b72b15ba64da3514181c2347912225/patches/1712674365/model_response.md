```java
import static org.hamcrest.MatcherAssert.assertThat;
import static org.hamcrest.core.IsInstanceOf.instanceOf;
import static org.hamcrest.core.StringContains.containsString;

import com.artipie.asto.Content.From;
import com.artipie.docker.asto.AstoBlobs;
import com.artipie.docker.asto.CheckedBlobSource;
import com.artipie.docker.asto.DefaultLayout;
import com.artipie.docker.asto.Digest.Sha256;
import com.artipie.docker.asto.IsNot;
import com.artipie.docker.asto.IsNull;
import com.artipie.docker.error.InvalidDigestException;
import com.artipie.docker.RepoName.Simple;
import com.artipie.asto.memory.InMemoryStorage;
import java.util.concurrent.CompletableFuture;
import org.junit.jupiter.api.Test;

class AstoBlobsITCase {

    @Test
    void failsOnDigestMismatch() {
        final InMemoryStorage storage = new InMemoryStorage();
        final AstoBlobs blobs = new AstoBlobs(storage, new DefaultLayout(), new Simple("any"));
        final String digest = "123";
        blobs.put(new CheckedBlobSource(new From("data".getBytes()), new Sha256(digest))).toCompletableFuture().handle(( blob, throwable) -> {
            assertThat("Exception thrown", throwable, new IsNot<>(new IsNull<>()));
            assertThat("Exception is InvalidDigestException", Throwable.getRootCause(throwable), instanceOf(InvalidDigestException.class));
            assertThat("Exception message contains calculated digest", Throwable.getRootCause(throwable).getMessage(), containsString("3a6eb0790f39ac87c94f3856b2dd2c5d110e6811602261a9a923d3bb23adc8b7"));
            assertThat("Exception message contains expected digest", Throwable.getRootCause(throwable).getMessage(), containsString(digest));
            return CompletableFuture.allOf();
        }).join();
    }
}
```