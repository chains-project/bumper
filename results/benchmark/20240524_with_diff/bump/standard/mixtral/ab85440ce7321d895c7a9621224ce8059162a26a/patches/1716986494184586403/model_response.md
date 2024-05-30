Here's a suggested patch for the given client code:

```java
import static org.hamcrest.MatcherAssert.assertThat;
import static org.hamcrest.Matchers.instanceOf;
import static org.hamcrest.Matchers.notNullValue;
import static org.hamcrest.core.IsEqual.equalTo;
import java.nio.charset.StandardCharsets;
import java.util.concurrent.CompletableFuture;
import org.junit.jupiter.api.Test;
import com.artipie.asto.Content;
import com.artipie.asto.Key;
import com.artipie.asto.memory.InMemoryStorage;
import com.artipie.docker.Digest;
import com.artipie.docker.asto.AstoBlobs;
import com.artipie.docker.asto.CheckedBlobSource;
import com.artipie.docker.error.InvalidDigestException;
import com.google.common.base.Throwables;
import static com.google.common.io.MoreFiles.encodeUTF8;

@Test
void failsOnDigestMismatch() {
    final InMemoryStorage storage = new InMemoryStorage();
    final AstoBlobs blobs = new AstoBlobs(storage, new DefaultLayout(), new RepoName.Simple("any"));
    final String digest = "123";
    blobs.put(new CheckedBlobSource(
        Content.From(encodeUTF8("data", StandardCharsets.UTF_8)),
        new Digest.Sha256(digest)
    )).toCompletableFuture().handle((blob, throwable) -> {
        assertThat("Exception thrown", throwable, notNullValue());
        assertThat("Exception is InvalidDigestException", throwable, instanceOf(InvalidDigestException.class));
        InvalidDigestException exception = (InvalidDigestException) throwable;
        assertThat("Exception message contains calculated digest", exception.message(), equalTo(
            "3a6eb0790f39ac87c94f3856b2dd2c5d110e6811602261a9a923d3bb23adc8b7"
        ));
        assertThat("Exception message contains expected digest", exception.message(), equalTo(
            String.format("Expected digest %s, got %s", digest, "3a6eb0790f39ac87c94f3856b2dd2c5d110e6811602261a9a923d3bb23adc8b7")
        ));
        return CompletableFuture.allOf();
    }).join();
}
```

The main changes are:

1. Importing static methods from `org.hamcrest.Matchers` and `com.google.common.base.Throwables` to simplify the code.
2. Replacing the `StringContains` matcher with `equalTo` for the expected and calculated digest.
3. Using `String.format` to include the expected digest in the exception message.
4. Changing the `IsNot` and `IsNull` matchers to `notNullValue` for the thrown exception.
5. Encoding the string "data" to bytes using `encodeUTF8` from `com.google.common.io.MoreFiles`.

These changes should resolve the compilation error and provide the desired behavior.