Here's the fixed `failsOnDigestMismatch` method with the required changes:

```java
import com.artipie.asto.Content;
import com.artipie.asto.CheckedBlobSource;
import com.artipie.asto.MemoryStorage;
import com.artipie.asto.RepoName;
import com.artipie.asto.Storage;
import com.artipie.asto.layer.DefaultLayout;
import com.artipie.docker.asto.AstoBlobs;
import com.artipie.docker.Digest;
import com.artipie.docker.CheckedBlobSource.From;
import com.artipie.docker.asto.IsNot;
import com.artipie.docker.asto.IsNull;
import com.artipie.docker.error.InvalidDigestException;
import com.google.common.base.Throwables;
import java.nio.charset.StandardCharsets;
import java.util.concurrent.CompletableFuture;
import org.hamcrest.MatcherAssert;
import org.hamcrest.core.IsInstanceOf;
import static org.hamcrest.core.StringContains.containsString;
import static org.hamcrest.MatcherAssert.assertThat;
import static org.junit.jupiter.api.Assertions.fail;

@org.junit.jupiter.api.Test
void failsOnDigestMismatch() {
    final Storage storage = new MemoryStorage();
    final AstoBlobs blobs = new AstoBlobs(storage, new DefaultLayout(), new RepoName.Simple("any"));
    final String digest = "123";
    try {
        blobs.put(new CheckedBlobSource(new Content.From("data".getBytes(StandardCharsets.UTF_8)), new Digest.Sha256(digest))).toCompletableFuture().join();
        fail("Exception not thrown");
    } catch (Exception e) {
        final Throwable rootCause = Throwables.getRootCause(e);
        assertThat("Exception thrown", rootCause instanceof InvalidDigestException);
        assertThat("Exception message contains calculated digest", rootCause.getMessage(), containsString("3a6eb0790f39ac87c94f3856b2dd2c5d110e6811602261a9a923d3bb23adc8b7"));
        assertThat("Exception message contains expected digest", rootCause.getMessage(), containsString(digest));
    }
}
```

The following changes have been made:

- Imported `java.nio.charset.StandardCharsets` for the `getBytes` method.
- Changed the `handle` method to `join` in the `CompletableFuture`.
- Wrapped the `CompletableFuture` in a `try-catch` block and used JUnit's `fail` method to ensure an exception is thrown.
- Updated the `StringContains` matcher to the new `containsString` method.
- Removed the `MatcherAssert.assertThat` calls that check for the `IsNot` and `IsNull` matchers.
- Updated the `StringContains` constructor to only accept a single `String` argument.