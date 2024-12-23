```java
import static org.hamcrest.MatcherAssert.assertThat;
import static org.hamcrest.core.IsInstanceOf.instanceOf;
import static org.hamcrest.core.StringContains.containsString;
import static org.hamcrest.core.IsNot.not;
import static org.hamcrest.core.IsNull.nullValue;
import static java.util.concurrent.CompletableFuture.allOf;

import com.artipie.docker.asto.AstoBlobs;
import com.artipie.docker.asto.CheckedBlobSource;
import com.artipie.docker.asto.DefaultLayout;
import com.artipie.docker.asto.IsNull;
import com.artipie.docker.asto.IsNot;
import com.artipie.docker.error.InvalidDigestException;
import com.artipie.docker.RepoName;
import com.artipie.asto.Content;
import com.artipie.asto.memory.InMemoryStorage;

import org.junit.jupiter.api.Test;

import java.util.concurrent.CompletableFuture;

public class AstoBlobsITCase {

    @Test
    void failsOnDigestMismatch() {
        InMemoryStorage storage = new InMemoryStorage();
        AstoBlobs blobs = new AstoBlobs(storage, new DefaultLayout(), new RepoName.Simple("any"));
        String digest = "123";
        allOf(blobs.put(new CheckedBlobSource(new Content.From("data".getBytes()), new com.artipie.docker.Digest.Sha256(digest)))
                .toCompletableFuture()
                .handle((blob, throwable) -> {
                    assertThat("Exception thrown", throwable, not(new IsNull<>()));
                    assertThat("Exception is InvalidDigestException", com.google.common.base.Throwables.getRootCause(throwable), instanceOf(InvalidDigestException.class));
                    assertThat("Exception message contains calculated digest", com.google.common.base.Throwables.getRootCause(throwable).getMessage(), containsString("3a6eb0790f39ac87c94f3856b2dd2c5d110e6811602261a9a923d3bb23adc8b7"));
                    assertThat("Exception message contains expected digest", com.google.common.base.Throwables.getRootCause(throwable).getMessage(), containsString(digest));
                    return CompletableFuture.allOf();
                }))
                .join();
    }
}
```