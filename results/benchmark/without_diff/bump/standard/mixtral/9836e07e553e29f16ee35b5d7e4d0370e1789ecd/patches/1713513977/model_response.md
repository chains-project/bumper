Here's a possible patch for the given client code:

```java
import static org.hamcrest.MatcherAssert.assertThat;
import static org.hamcrest.Matchers.instanceOf;
import static org.hamcrest.Matchers.not;
import static org.hamcrest.Matchers.nullValue;
import java.nio.charset.StandardCharsets;
import java.util.concurrent.CompletableFuture;
import org.hamcrest.Matcher;
import org.junit.jupiter.api.Test;
import com.artipie.asto.Content;
import com.artipie.asto.CheckedBlobSource;
import com.artipie.asto.Memory;
import com.artipie.asto.Storage;
import com.artipie.asto.ext.ExtStorage;
import com.artipie.docker.asto.AstoBlobs;
import com.artipie.docker.asto.CheckedBlob;
import com.artipie.docker.asto.DefaultLayout;
import com.artipie.docker.Digest;
import com.artipie.docker.RepoName;
import com.artipie.docker.error.InvalidDigestException;
import com.google.common.base.Throwables;
import io.reactivex.Single;
import java.util.concurrent.CompletionStage;

@Test
void failsOnDigestMismatch() {
    final Storage storage = new ExtStorage(new Memory());
    final AstoBlobs blobs = new AstoBlobs(storage, new DefaultLayout(), new RepoName.Simple("any"));
    final String digest = "123";
    final Matcher<CheckedBlob> isNull = not(nullValue());
    final Matcher<Throwable> isNot = not(isNull);
    final Matcher<Throwable> isInvalidDigest = instanceOf(InvalidDigestException.class);
    final Matcher<String> stringContains = new StringContains(digest);
    final CheckedBlobSource checkedBlobSource = new CheckedBlobSource(
        new Content.From("data".getBytes(StandardCharsets.UTF_8)),
        new Digest.Sha256(digest)
    );
    final CompletionStage<CheckedBlob> put = blobs.put(checkedBlobSource);
    put.toCompletableFuture()
        .handle((checkedBlob, throwable) -> {
            assertThat("Exception thrown", throwable, isNot);
            assertThat("Exception is InvalidDigestException", throwable, isInvalidDigest);
            final Throwable rootCause = Throwables.getRootCause(throwable);
            assertThat("Exception message contains calculated digest", rootCause.getMessage(), stringContains);
            assertThat("Exception message contains expected digest", rootCause.getMessage(), stringContains);
            return CompletableFuture.allOf();
        })
        .join();
}

private static class StringContains implements Matcher<String> {
    private final String expected;

    private StringContains(String expected) {
        this.expected = expected;
    }

    @Override
    public boolean matches(Object actual) {
        return actual instanceof String && ((String) actual).contains(expected);
    }

    @Override
    public void describeTo(org.hamcrest.Description description) {
        description.appendText("a string containing ").appendValue(expected);
    }
}
```

This patch defines a new `StringContains` class that implements the `Matcher<String>` interface, which is used to check if a string contains a substring. It also defines a new `failsOnDigestMismatch()` method that creates a new `Storage` object using the `ExtStorage` class, which provides some additional functionality compared to the `InMemoryStorage` class used in the original code. Finally, it defines a new `put` variable using the `CompletionStage` interface instead of the `CompletableFuture` interface used in the original code.

Note that this patch assumes that the `CheckedBlobSource`, `Content`, `ExtStorage`, `Memory`, `RepoName`, and `StringContains` classes are available in the project's classpath. If these classes are not available, the patch may need to be modified accordingly.