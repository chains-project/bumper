Here's the fixed version of the method:

```java
import com.artipie.asto.Content;
import com.artipie.asto.CheckedBlobSource;
import com.artipie.asto.Digest;
import com.artipie.asto.Layout;
import com.artipie.asto.memory.InMemoryStorage;
import com.artipie.docker.asto.AstoBlobs;
import com.artipie.docker.asto.DefaultLayout;
import com.artipie.docker.Digest.Sha256;
import com.artipie.docker.RepoName;
import com.artipie.docker.RepoName.Simple;
import com.artipie.docker.error.InvalidDigestException;
import com.google.common.base.Throwables;
import java.nio.charset.StandardCharsets;
import java.util.concurrent.CompletableFuture;
import org.hamcrest.MatcherAssert;
import org.hamcrest.Matchers;
import static org.hamcrest.Matchers.instanceOf;
import static org.hamcrest.Matchers.not;
import static org.hamcrest.core.IsInstanceOf.instanceOf;
import static org.hamcrest.core.StringContains.containsString;

@org.junit.jupiter.api.Test
void failsOnDigestMismatch() {
    final InMemoryStorage storage = new InMemoryStorage();
    final Layout layout = new DefaultLayout();
    final RepoName repoName = new Simple("any");
    final AstoBlobs blobs = new AstoBlobs(storage, layout, repoName);
    final String digest = "123";
    blobs.put(new CheckedBlobSource(new Content.From("data".getBytes(StandardCharsets.UTF_8)), new Sha256(digest)))
        .toCompletableFuture()
        .handle((blob, throwable) -> {
            MatcherAssert.assertThat("Exception thrown", throwable, not(instanceOf(InvalidDigestException.class)));
            MatcherAssert.assertThat("Exception is InvalidDigestException", throwable, instanceOf(InvalidDigestException.class));
            MatcherAssert.assertThat("Exception message contains calculated digest", Throwables.getRootCause(throwable).getMessage(), containsString("3a6eb0790f39ac87c94f3856b2dd2c5d110e6811602261a9a923d3bb23adc8b7"));
            MatcherAssert.assertThat("Exception message contains expected digest", Throwables.getRootCause(throwable).getMessage(), containsString(digest));
            return CompletableFuture.allOf();
        })
        .join();
}
```

The main change is the usage of `StringContains` matcher. I replaced it with `containsString` method from `Matchers` class. The `StringContains` constructor expects a single argument, but it received two arguments in the original code.