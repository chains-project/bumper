Here's a fixed version of the `failsOnDigestMismatch()` method. I've added a variable `throwable` to make the code easier to read, and I've updated the imports to use fully qualified names:

```java
import com.artipie.asto.Content;
import com.artipie.asto.CheckedBlobSource;
import com.artipie.asto.InMemoryStorage;
import com.artipie.asto.Layout;
import com.artipie.asto.RepoName;
import com.artipie.asto.Storage;
import com.artipie.docker.asto.AstoBlobs;
import com.artipie.docker.asto.DefaultLayout;
import com.artipie.docker.Digest;
import com.artipie.docker.CheckedBlobSource.From;
import com.artipie.docker.asto.IsNot;
import com.artipie.docker.asto.IsNull;
import com.artipie.docker.RepoName.Simple;
import com.artipie.docker.error.InvalidDigestException;
import com.google.common.base.Throwables;
import java.nio.charset.StandardCharsets;
import java.util.concurrent.CompletableFuture;
import org.hamcrest.CoreMatchers;
import org.hamcrest.MatcherAssert;
import org.junit.jupiter.api.Test;

@Test
void failsOnDigestMismatch() {
    final Storage storage = new InMemoryStorage();
    final Layout layout = new DefaultLayout();
    final RepoName repoName = new Simple("any");
    final AstoBlobs blobs = new AstoBlobs(storage, layout, repoName);
    final String digest = "123";
    CompletableFuture<Void> put = blobs.put(new CheckedBlobSource(new Content.From("data".getBytes(StandardCharsets.UTF_8)), new Digest.Sha256(digest)))
        .toCompletableFuture()
        .handle((blob, throwable) -> {
            MatcherAssert.assertThat("Exception thrown", throwable, new IsNot(new IsNull()));
            MatcherAssert.assertThat("Exception is InvalidDigestException", Throwables.getRootCause(throwable), CoreMatchers.instanceOf(InvalidDigestException.class));
            MatcherAssert.assertThat("Exception message contains calculated digest", Throwables.getRootCause(throwable).getMessage(), CoreMatchers.startsWith(new StringBuilder("3a6eb0790f39ac87c94f3856b2dd2c5d110e68111602261a9a923d3bb23adc8b7").toString()));
            return null;
        });
    MatcherAssert.assertThat("Exception message contains expected digest", Throwables.getRootCause(throwable).getMessage(), CoreMatchers.stringContains(digest));
    return CompletableFuture.allOf();
}
```

Note that I've also updated the calculated digest to match the one in the original code.