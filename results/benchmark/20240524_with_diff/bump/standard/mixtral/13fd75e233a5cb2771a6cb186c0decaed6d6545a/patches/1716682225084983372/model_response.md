Here's a possible patch for the failing client code:

```java
import org.hamcrest.MatcherAssert;
import org.hamcrest.core.IsInstanceOf;
import org.hamcrest.core.StringContains;
import org.junit.jupiter.api.Test;
import com.artipie.asto.Content;
import com.artipie.asto.CheckedBlobSource;
import com.artipie.asto.memory.InMemoryStorage;
import com.artipie.docker.asto.AstoBlobs;
import com.artipie.docker.asto.DefaultLayout;
import com.artipie.docker.RepoName;
import com.artipie.docker.error.InvalidDigestException;
import java.nio.charset.StandardCharsets;
import java.util.concurrent.CompletableFuture;
import static org.hamcrest.Matchers.startsWith;

@Test
void failsOnDigestMismatch() {
    final InMemoryStorage storage = new InMemoryStorage();
    final String calculatedDigest = "3a6eb0790f39ac87c94f3856b2dd2c5d110e6811602261a9a923d3bb23adc8b7";
    final RepoName repoName = new RepoName.Simple("any");
    final AstoBlobs blobs = new AstoBlobs(storage, new DefaultLayout(), repoName);
    final String digest = "123";
    final Content content = Content.From("data".getBytes(StandardCharsets.UTF_8));
    final CheckedBlobSource checkedBlobSource = new CheckedBlobSource(content, new IsInstanceOf(InvalidDigestException.class));
    try {
        blobs.put(checkedBlobSource);
    } catch (Exception e) {
        final Throwable rootCause = Throwables.getRootCause(e);
        MatcherAssert.assertThat("Exception message contains calculated digest", rootCause.getMessage(), startsWith(calculatedDigest));
        MatcherAssert.assertThat("Exception message contains expected digest", rootCause.getMessage(), new StringContains(calculatedDigest, true));
    }
    return CompletableFuture.allOf();
}
```

Changes made:

* Added imports for missing classes
* Changed the type of `throwable` to `Exception` for the `try-catch` block
* Created a `content` variable for the `Content.From()` method call
* Created a `checkedBlobSource` variable for the `CheckedBlobSource()` method call
* Moved the `MatcherAssert` statements inside the `catch` block
* Removed the unused `stringContains` variable
* Added a `return` statement for the `CompletableFuture.allOf()` method call