Here's a possible patch for the code:

```java
import static org.hamcrest.MatcherAssert.assertThat;
import static org.hamcrest.Matchers.instanceOf;
import static org.hamcrest.Matchers.not;
import static org.hamcrest.Matchers.nullValue;
import java.nio.charset.StandardCharsets;
import java.util.concurrent.CompletableFuture;
import org.junit.jupiter.api.Test;
import com.artipie.asto.Content;
import com.artipie.asto.Key;
import com.artipie.asto.Storage;
import com.artipie.asto.memory.InMemoryStorage;
import com.artipie.docker.asto.AstoBlobs;
import com.artipie.docker.asto.CheckedBlobSource;
import com.artipie.docker.asto.DefaultLayout;
import com.artipie.docker.Digest;
import com.artipie.docker.error.InvalidDigestException;
import com.google.common.base.Throwables;
import io.reactivex.Completable;

@Test
void failsOnDigestMismatch() {
    final Storage storage = new InMemoryStorage();
    final AstoBlobs blobs = new AstoBlobs(storage, new DefaultLayout(), new com.artipie.docker.RepoName.Simple("any"));
    final String digest = "123";
    blobs.put(new CheckedBlobSource(
        new Content.From("data".getBytes(StandardCharsets.UTF_8)),
        new Digest.Sha256(digest)
    )).toCompletableFuture().handle((blob, throwable) -> {
        assertThat("Exception thrown", throwable, not(nullValue()));
        assertThat("Exception is InvalidDigestException", throwable, instanceOf(InvalidDigestException.class));
        final String message = throwable.getMessage();
        final String calculatedDigest = "3a6eb0790f39ac87c94f3856b2dd2c5d110e6811602261a9a923d3bb23adc8b7";
        assertThat("Exception message contains calculated digest", message, StringContains.containsString(calculatedDigest));
        assertThat("Exception message contains expected digest", message, StringContains.containsString(digest));
        return Completable.complete();
    }).join();
}

private static class StringContains extends org.hamcrest.Matcher<String> {
    private StringContains(String contains) {
        super();
        this.contains = contains;
    }

    private final String contains;

    @Override
    public boolean matches(final Object item) {
        return item != null && ((String) item).contains(contains);
    }

    public static StringContains containsString(final String substring) {
        return new StringContains(substring);
    }
}
```

The patch creates a new `StringContains` class that extends `org.hamcrest.Matcher<String>` and provides a `containsString` method to create an instance of `StringContains`. This allows the `StringContains` matcher to be used with `String` objects, as required by the `StringContains` constructor. The patch also includes the necessary import statements for the new `StringContains` class.

Note that this patch assumes that the `StringContains` class is defined within the same class as the `failsOnDigestMismatch` method. If the `StringContains` class needs to be defined in a separate class, it can be extracted from the patch and defined as a top-level class or a nested static class, as appropriate.

Additionally, the patch uses `Completable.complete()` instead of `CompletableFuture.allOf()` for the successful case. This is because the `join()` method is called on the `CompletableFuture`, which means that the `CompletableFuture` must be completed with a value. Since the `join()` method blocks until the `CompletableFuture` is completed, using `Completable.complete()` is sufficient for the test case.

Finally, the patch includes the necessary import statements for the classes used in the `failsOnDigestMismatch` method.