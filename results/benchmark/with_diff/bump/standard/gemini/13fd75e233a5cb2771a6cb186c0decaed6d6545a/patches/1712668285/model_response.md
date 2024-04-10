```java
import com.artipie.asto.Content;
import com.artipie.docker.Digest;
import com.artipie.docker.asto.CheckedBlobSource;
import com.artipie.docker.asto.IsNot;
import com.artipie.docker.asto.IsNull;
import com.artipie.docker.error.InvalidDigestException;
import com.artipie.docker.RepoName;
import com.artipie.asto.memory.InMemoryStorage;
import com.artipie.docker.asto.AstoBlobs;
import com.artipie.docker.asto.DefaultLayout;
import org.hamcrest.MatcherAssert;
import org.hamcrest.core.IsInstanceOf;
import org.hamcrest.core.StringContains;
import org.junit.jupiter.api.Test;
import java.lang.String;
import java.util.concurrent.CompletableFuture;
import java.util.concurrent.ExecutionException;
import java.util.concurrent.TimeUnit;
import java.util.concurrent.TimeoutException;

import static org.hamcrest.MatcherAssert.assertThat;
import static org.junit.jupiter.api.Assertions.assertThrows;

public class AstoBlobsITCase {

    @Test
    void failsOnDigestMismatch() {
        final InMemoryStorage storage = new InMemoryStorage();
        final AstoBlobs blobs = new AstoBlobs(storage, new DefaultLayout(), new RepoName.Simple("any"));
        final String digest = "123";
        assertThrows(InvalidDigestException.class, () -> {
            blobs.put(new CheckedBlobSource(new Content.From("data".getBytes()), new Digest.Sha256(digest))).get(1, TimeUnit.SECONDS);
        });
    }
}
```