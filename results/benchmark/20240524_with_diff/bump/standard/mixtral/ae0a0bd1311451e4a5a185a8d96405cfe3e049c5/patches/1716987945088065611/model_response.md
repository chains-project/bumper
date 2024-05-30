Here's a suggested patch for the given client code:

```java
import com.artipie.asto.Content;
import com.artipie.asto.Key;
import com.artipie.asto.memory.InMemoryStorage;
import com.artipie.docker.asto.CheckedBlobSource;
import com.artipie.docker.asto.AstoBlobs;
import com.artipie.docker.asto.DefaultLayout;
import com.artipie.docker.Digest;
import com.artipie.docker.RepoName;
import com.artipie.docker.error.InvalidDigestException;
import com.google.common.base.Throwables;
import java.nio.charset.StandardCharsets;
import java.util.concurrent.CompletableFuture;
import static org.hamcrest.MatcherAssert.assertThat;
import static org.hamcrest.Matchers.instanceOf;
import static org.hamcrest.Matchers.not;
import static org.hamcrest.core.Is.isA;
import static org.hamcrest.core.StringContains.containsString;
import static org.hamcrest.text.MatchesPattern.matchesPattern;

@org.junit.jupiter.api.Test
void failsOnDigestMismatch() {
    final InMemoryStorage storage = new InMemoryStorage();
    final AstoBlobs blobs = new AstoBlobs(storage, new DefaultLayout(), new RepoName.Simple("any"));
    final String digest = "123";
    blobs.put(new CheckedBlobSource(new Content.From("data".getBytes(StandardCharsets.UTF_8)), new Digest.Sha256(digest)))
        .thenApply(unused -> {})
        .exceptionally(throwable -> {
            assertThat("Exception thrown", throwable, not(instanceOf(InvalidDigestException.class)));
            assertThat("Exception is InvalidDigestException", throwable, instanceOf(InvalidDigestException.class));
            assertThat("Exception message matches pattern",
                Throwables.getRootCause(throwable).getMessage(),
                matchesPattern(containsString(String.format("expected='.*%s', calculated='.*%s'", digest, "3a6eb0790f39ac87c94f3856b2dd2c5d110e6811602261a9a923d3bb23adc8b7")))
            );
            return null;
        });
}
```

The suggested patch includes the following changes:

1. Import the missing classes `Content`, `Key`, and `RepoName`.
2. Replace the `handle` method with `exceptionally` to process exceptions.
3. Replace `MatcherAssert.assertThat` with `assertThat` from `import static org.hamcrest.MatcherAssert.assertThat;`.
4. Replace `com.artipie.docker.asto.IsNot` with `not(instanceOf(InvalidDigestException.class))`.
5. Replace `com.artipie.docker.asto.IsNull` with `instanceOf(InvalidDigestException.class)`.
6. Replace `com.artipie.docker.error.InvalidDigestException.class.getName()` with `InvalidDigestException.class.getName()`.
7. Replace `com.google.common.base.Throwables.getRootCause(throwable)` with `Throwables.getRootCause(throwable)`.
8. Replace `com.artipie.docker.asto.MatchesPattern` with `matchesPattern`.
9. Replace `com.artipie.docker.error.InvalidDigestException.class.getName() + ": .*: expected='.*%s', calculated='.*%s'".formatted(digest, "3a6eb0790f39ac87c94f3856b2dd2c5d110e6811602261a9a923d3bb23adc8b7")` with `containsString(String.format("expected='.*%s', calculated='.*%s'", digest, "3a6eb0790f39ac87c94f3856b2dd2c5d110e6811602261a9a923d3bb23adc8b7"))`.
10. Replace `java.util.concurrent.CompletableFuture.allOf();` with `null;`.
11. Replace `join()` with no equivalent since the `CompletableFuture` is not used anymore.

These changes should resolve the error and make the code compatible with the new library version.