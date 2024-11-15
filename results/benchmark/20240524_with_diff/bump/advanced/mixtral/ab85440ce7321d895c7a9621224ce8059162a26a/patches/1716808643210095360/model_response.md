Here's the fixed `failsOnDigestMismatch` method with the necessary changes to resolve the error:

```java
import com.artipie.asto.Content;
import com.artipie.asto.CheckedBlobSource;
import com.artipie.asto.memory.InMemoryStorage;
import com.artipie.docker.asto.AstoBlobs;
import com.artipie.docker.asto.DefaultLayout;
import com.artipie.docker.Digest;
import com.artipie.docker.RepoName;
import com.artipie.docker.asto.CheckedBlob;
import com.artipie.docker.error.InvalidDigestException;
import java.nio.charset.StandardCharsets;
import java.util.concurrent.CompletableFuture;
import static com.artipie.docker.asto.IsNot.not;
import static com.artipie.docker.asto.IsNot.isNull;
import static org.hamcrest.MatcherAssert.assertThat;
import static org.hamcrest.Matchers.instanceOf;
import static org.hamcrest.core.IsInstanceOf.instanceOf;
import static org.hamcrest.core.StringContains.containsString;
import static org.hamcrest.core.StringStartsWith.startsWith;

@org.junit.jupiter.api.Test
void failsOnDigestMismatch() {
    final InMemoryStorage storage = new InMemoryStorage();
    final AstoBlobs blobs = new AstoBlobs(storage, new DefaultLayout(), new RepoName.Simple("any"));
    final String digest = "123";
    blobs.put(new CheckedBlobSource(new Content.From("data".getBytes(StandardCharsets.UTF_8)), new Digest.Sha256(digest)))
        .toCompletableFuture()
        .handle((CheckedBlob blob, Throwable throwable) -> {
            assertThat("Exception thrown", throwable, not(isNull()));
            assertThat("Exception is InvalidDigestException", throwable, instanceOf(InvalidDigestException.class));
            String message = throwable.getMessage();
            assertThat("Exception message contains calculated digest", message, containsString("3a6eb0790f39ac87c94f3856b2dd2c5d110e6811602261a9a923d3bb23adc8b7"));
            assertThat("Exception message contains expected digest", message, startsWith(String.format("invalid digest for %s", digest)));
            return CompletableFuture.allOf();
        })
        .join();
}
```

The changes include:

1. Importing missing classes `IsNot`, `not`, `isNull`, `StringContains`, and `StringStartsWith`.
2. Replacing the `StringContains` constructor with `containsString` for the first assertion.
3. Using `startsWith` instead of `StringContains` for the second assertion to match the updated library method signature.
4. Updating the imports for `Content`, `CheckedBlobSource`, `InMemoryStorage`, `RepoName`, `Digest`, `InvalidDigestException`, and `CheckedBlob`.
5. Changing the way the content is encoded from `"data".getBytes()` to `"data".getBytes(StandardCharsets.UTF_8)`.
6. Reformatting the code for better readability.