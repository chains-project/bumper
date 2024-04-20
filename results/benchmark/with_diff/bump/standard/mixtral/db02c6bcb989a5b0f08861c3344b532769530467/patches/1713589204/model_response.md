Here's a suggested patch for the given client code:

```java
import com.artipie.asto.CheckedBlobSource;
import com.artipie.asto.Content;
import com.artipie.asto.Key;
import com.artipie.asto.Memory;
import com.artipie.asto.Storage;
import com.artipie.asto.TmpFolder;
import com.artipie.docker.Digest;
import com.artipie.docker.RepoName;
import com.artipie.docker.asto.CheckedBlob;
import com.artipie.docker.asto.AstoBlobs;
import com.artipie.docker.asto.DefaultLayout;
import com.google.common.base.Throwables;
import io.reactivex.Completable;
import java.nio.file.Files;
import java.nio.file.Path;
import org.hamcrest.MatcherAssert;
import org.hamcrest.Matchers;
import org.junit.jupiter.api.Test;

@Test
void fixesDigestMismatch() {
    final Storage storage = new TmpFolder();
    final AstoBlobs blobs = new AstoBlobs(
        storage,
        new DefaultLayout(),
        new RepoName.Simple("any")
    );
    final Digest digest = Digest.sha256("123");
    final Path data = Files.createTempFile("data", null);
    try {
        final Content content = Content.from(Files.readAllBytes(data));
        final Key key = new Key.From("data", digest);
        final CheckedBlob checkedBlob = new CheckedBlob(content, key);
        final CompletableFuture<CheckedBlob> future = blobs.put(new CheckedBlobSource(checkedBlob));
        future.handle((blob, throwable) -> {
            MatcherAssert.assertThat(
                "Exception thrown",
                throwable,
                Matchers.not(Matchers.instanceOf(IllegalArgumentException.class))
            );
            MatcherAssert.assertThat(
                "Exception is InvalidDigestException",
                Throwables.getRootCause(throwable),
                Matchers.instanceOf(com.artipie.docker.error.InvalidDigestException.class)
            );
            MatcherAssert.assertThat(
                "Exception message contains calculated digest",
                Throwables.getRootCause(throwable).getMessage(),
                Matchers.stringContains("3a6eb0790f39ac87c94f3856b2dd2c5d110e6811602261a9a923d3bb23adc8b7")
            );
        });
    } finally {
        Files.deleteIfExists(data);
    }
    MatcherAssert.assertThat(
        "Exception message contains expected digest",
        Throwables.getRootCause(throwable).getMessage(),
        Matchers.stringContains(digest.toString())
    );
    return Completable.complete();
}
```

In the updated code, I've replaced the `InMemoryStorage` with `TmpFolder` which is a new addition to the library. Also, I've added a `Path` variable `data` to store the temporary file for the content. The `CheckedBlob` is now created using the `Content` obtained from the `data` file. The rest of the code remains mostly the same.

Please note that you need to replace the `import` statements according to the new library version.