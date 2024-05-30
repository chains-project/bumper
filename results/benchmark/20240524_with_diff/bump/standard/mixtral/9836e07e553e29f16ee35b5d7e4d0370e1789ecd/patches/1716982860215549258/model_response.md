Here's a suggested patch for the failing client code:

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
import com.artipie.asto.MemoryStorage;
import com.artipie.asto.Storage;
import com.artipie.asto.ext.ExtendedCheckedBlobSource;
import com.artipie.docker.Digest;
import com.artipie.docker.Digest.Sha256;
import com.artipie.docker.asto.AstoBlobs;
import com.artipie.docker.asto.CheckedBlobSource;
import com.artipie.docker.asto.DefaultLayout;
import com.artipie.docker.error.InvalidDigestException;
import com.google.common.base.Throwables;
import io.reactivex.Completable;
import java.util.concurrent.CompletionStage;

@Test
void failsOnDigestMismatch() {
    final Storage storage = new MemoryStorage();
    final AstoBlobs blobs = new AstoBlobs(
        storage,
        new DefaultLayout(),
        new com.artipie.docker.RepoName.Simple("any")
    );
    final String digest = "123";
    final Key key = new Key.From("data".getBytes(StandardCharsets.UTF_8));
    final Content content = Content.From("data".getBytes());
    final Digest calculatedDigest = new Sha256(
        com.artipie.docker.Digest.calculateSha256(content.bytes())
    );
    final CheckedBlobSource checkedBlobSource = new ExtendedCheckedBlobSource(
        content,
        calculatedDigest
    );
    final CompletionStage<Void> put = blobs.put(checkedBlobSource);
    put.toCompletableFuture()
        .handle((Void v, Throwable throwable) -> {
            assertThat("Exception thrown", throwable, notNullValue());
            assertThat("Exception is InvalidDigestException", throwable, instanceOf(InvalidDigestException.class));
            final InvalidDigestException idException = (InvalidDigestException) throwable;
            assertThat(
                "Exception message contains calculated digest",
                idException.message(),
                equalTo(String.format("invalid digest for %s, expected %s, got %s", key, calculatedDigest, idException.digest()))
            );
            assertThat("Exception message contains expected digest", idException.message(), equalTo(String.format("invalid digest for %s, expected %s, got %s", key, digest, idException.digest())));
            return Completable.complete();
        })
        .join();
}
```

In the updated code, I replaced the deprecated `StringContains` matcher with the `equalTo` matcher for the exception message comparison. I also extracted the creation of the `Key`, `Content`, and `CheckedBlobSource` objects into separate variables for better readability. Additionally, I added a `calculateSha256` method from the `Digest` class for calculating the SHA-256 digest of the content. Lastly, I replaced the `handle` method with a more concise `handle` method that returns a `Completable` object.