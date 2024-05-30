Here's a suggested patch for the given client code:

```java
import static org.hamcrest.MatcherAssert.assertThat;
import static org.hamcrest.Matchers.instanceOf;
import static org.hamcrest.Matchers.not;
import static org.hamcrest.Matchers.nullValue;
import java.nio.charset.StandardCharsets;
import java.util.concurrent.CompletableFuture;
import org.junit.jupiter.api.Test;
import com.artipie.asto.Content;
import com.artipie.asto.memory.InMemoryStorage;
import com.artipie.docker.asto.AstoBlobs;
import com.artipie.docker.asto.CheckedBlobSource;
import com.artipie.docker.asto.DefaultLayout;
import com.artipie.docker.Digest;
import com.artipie.docker.RepoName;
import com.artipie.docker.error.InvalidDigestException;
import com.google.common.base.Throwables;

@Test
void failsOnDigestMismatch() {
    final InMemoryStorage storage = new InMemoryStorage();
    final AstoBlobs blobs = new AstoBlobs(
        storage,
        new DefaultLayout(),
        new RepoName.Simple("any")
    );
    final String digest = "123";
    blobs.put(
        new CheckedBlobSource(
            Content.From("data".getBytes(StandardCharsets.UTF_8)),
            new Digest.Sha256(digest)
        )
    ).toCompletableFuture()
        .handle(
            (blob, throwable) -> {
                assertThat("Exception thrown", throwable, not(nullValue()));
                assertThat("Exception is InvalidDigestException", throwable, instanceOf(InvalidDigestException.class));
                InvalidDigestException exception = (InvalidDigestException) throwable;
                assertThat(
                    "Exception message contains calculated digest",
                    exception.message(),
                    new org.hamcrest.core.StringContains(exception.calculatedDigest())
                );
                assertThat("Exception message contains expected digest", exception.message(), new org.hamcrest.core.StringContains(digest));
                return CompletableFuture.allOf();
            }
        )
        .join();
}
```

The main change is the way the `StringContains` matcher is used. Instead of using `new StringContains(true, "expected value")`, the `StringContains` matcher is now used with the `message()` method of the `InvalidDigestException` instance, and a new `StringContains` instance is created with the `calculatedDigest()` method of the exception instance as the argument. Additionally, the `getRootCause()` method is no longer required since the thrown exception is already an `InvalidDigestException`.