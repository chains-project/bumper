```java
import com.artipie.docker.asto.CheckedBlobSource;
import com.artipie.docker.asto.DefaultLayout;
import com.artipie.docker.asto.Digest;
import com.artipie.docker.asto.IsNot;
import com.artipie.docker.asto.IsNull;
import com.artipie.docker.asto.AstoBlobs;
import com.artipie.asto.Content;
import com.artipie.asto.memory.InMemoryStorage;
import com.artipie.docker.RepoName;
import com.artipie.docker.error.InvalidDigestException;
import java.util.concurrent.CompletableFuture;
import org.hamcrest.MatcherAssert;
import org.hamcrest.core.IsInstanceOf;
import org.hamcrest.core.StringContains;
import org.junit.jupiter.api.Test;

class AstoBlobsITCase {

    @Test
    void failsOnDigestMismatch() {
        final InMemoryStorage storage = new InMemoryStorage();
        final AstoBlobs blobs = new AstoBlobs(storage, new DefaultLayout(), new RepoName.Simple("any"));
        final String digest = "123";
        blobs.put(new CheckedBlobSource(Content.From("data".getBytes()), new Digest.Sha256(digest))).toCompletableFuture().handle((blob, throwable) -> {
            MatcherAssert.assertThat("Exception thrown", throwable, new IsNot<>(new IsNull<>()));
            MatcherAssert.assertThat("Exception is InvalidDigestException", com.google.common.base.Throwables.getRootCause(throwable), new IsInstanceOf(InvalidDigestException.class));
            MatcherAssert.assertThat("Exception message contains calculated digest", com.google.common.base.Throwables.getRootCause(throwable).getMessage(), new StringContains(true, "3a6eb0790f39ac87c94f3856b2dd2c5d110e6811602261a9a923d3bb23adc8b7"));
            MatcherAssert.assertThat("Exception message contains expected digest", com.google.common.base.Throwables.getRootCause(throwable).getMessage(), new StringContains(true, digest));
            return null;
        }).join();
    }
}
```