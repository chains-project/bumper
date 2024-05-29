Here's a fixed version of your code:

```java
import com.artipie.asto.Content;
import com.artipie.asto.CheckedBlobSource;
import com.artipie.asto.MemoryStorage;
import com.artipie.asto.Storage;
import com.artipie.asto.asto.AstoBlobs;
import com.artipie.docker.Digest;
import com.artipie.docker.DefaultLayout;
import com.artipie.docker.RepoName;
import com.artipie.docker.error.InvalidDigestException;
import java.nio.charset.StandardCharsets;
import java.util.concurrent.CompletableFuture;
import org.hamcrest.MatcherAssert;
import org.hamcrest.Matchers;
import org.junit.jupiter.api.Test;

@Test
void failsOnDigestMismatch() {
    final Storage storage = new MemoryStorage();
    final AstoBlobs blobs = new AstoBlobs(storage, new DefaultLayout(), new RepoName.Simple("any"));
    final String digest = "123";
    blobs.put(new CheckedBlobSource(Content.From("data".getBytes()), new Digest.Sha256(digest)))
        .toCompletableFuture()
        .handle((blob, throwable) -> {
            MatcherAssert.assertThat("Exception thrown", throwable, Matchers.notNullValue());
            MatcherAssert.assertThat("Exception is InvalidDigestException", throwable, Matchers.instanceOf(InvalidDigestException.class));
            MatcherAssert.assertThat("Exception message contains calculated digest",
                throwable.getMessage(), Matchers.stringContainsInOrder(
                    "3a6eb0790f39ac87c94f3856b2dd2c5d110e6811602261a9a923d3bb23adc8b7",
                    digest
                ));
            return CompletableFuture.allOf();
        })
        .join();
}
```

The main change is in the `MatcherAssert.assertThat` calls. The `StringContains` matcher should take a single argument, the expected substring. Instead, you were passing two arguments: a boolean and a string. I replaced the boolean argument with `Matchers.stringContainsInOrder`, which checks if the given string contains the provided substrings in the specified order.