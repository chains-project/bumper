Here's the updated code to fix the error:

```java
import com.artipie.asto.Content;
import com.artipie.asto.CheckedBlobSource;
import com.artipie.asto.MemoryStorage;
import com.artipie.asto.ansion.Layout;
import com.artipie.asto.ext.Ext;
import com.artipie.docker.asto.AstoBlobs;
import com.artipie.docker.asto.CheckedBlob;
import com.artipie.docker.Digest;
import com.artipie.docker.RepoName;
import com.artipie.docker.error.InvalidDigestException;
import com.google.common.base.Throwables;
import io.reactivex.Completable;
import java.nio.ByteBuffer;
import java.nio.charset.StandardCharsets;
import java.util.concurrent.CompletableFuture;
import org.hamcrest.MatcherAssert;
import org.junit.jupiter.api.Test;
import static com.artipie.docker.asto.CheckedBlob.checksum;
import static org.hamcrest.Matchers.*;
import static org.hamcrest.core.IsInstanceOf.instanceOf;

@Test
void failsOnDigestMismatch() {
    final MemoryStorage storage = new MemoryStorage();
    final Layout layout = new Layout.Base();
    final RepoName repoName = new RepoName.Simple("any");
    final AstoBlobs blobs = new AstoBlobs(storage, layout, repoName);
    final String digest = "123";
    final Content content = Content.From("data".getBytes(StandardCharsets.UTF_8));
    final ByteBuffer buffer = content.buffer();
    final CheckedBlob checkedBlob = CheckedBlob.create(
        buffer,
        checksum(buffer),
        Digest.Sha256.name()
    );
    blobs.put(new CheckedBlobSource(checkedBlob)).toCompletableFuture().handle(( blob, throwable) -> {
        MatcherAssert.assertThat("Exception thrown", throwable, notNullValue());
        MatcherAssert.assertThat("Exception is InvalidDigestException", throwable, instanceOf(InvalidDigestException.class));
        MatcherAssert.assertThat("Exception message contains calculated digest", Throwables.getRootCause(throwable).getMessage(), stringContainsInOrder(
            checkedBlob.content().content(),
            checkedBlob.checksum(),
            checkedBlob.digest().name()
        ));
        MatcherAssert.assertThat("Exception message contains expected digest", Throwables.getRootCause(throwable).getMessage(), stringContainsIgnoringCase(digest));
        return Completable.complete();
    }).join();
}
```

The changes include:

- Replacing the `IsNot` and `IsNull` matchers with `notNullValue()`.
- Replacing the `StringContains` matcher with `stringContainsInOrder()` and `stringContainsIgnoringCase()`.
- Creating a `ByteBuffer` for the content and using it to create a `CheckedBlob`.
- Replacing the `CompletableFuture` with RxJava's `Completable`.