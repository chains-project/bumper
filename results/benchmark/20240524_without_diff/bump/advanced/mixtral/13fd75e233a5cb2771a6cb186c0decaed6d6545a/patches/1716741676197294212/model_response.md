Here's a possible patch for the given client code:

```java
import static org.hamcrest.MatcherAssert.assertThat;
import static org.hamcrest.Matchers.instanceOf;
import static org.hamcrest.Matchers.not;
import static org.hamcrest.Matchers.nullValue;
import java.nio.charset.StandardCharsets;
import java.util.concurrent.CompletableFuture;
import org.junit.jupiter.api.Test;
import com.artipie.asto.Content;
import com.artipie.asto.Memory;
import com.artipie.asto.Storage;
import com.artipie.asto.ext.BlobId;
import com.artipie.asto.ext.Blobs;
import com.artipie.docker.Digest;
import com.artipie.docker.Digest.Sha256;
import com.artipie.docker.asto.CheckedBlobSource;
import com.artipie.docker.error.InvalidDigestException;
import io.reactivex.Completable;
import org.hamcrest.Matcher;

@Test
void failsOnDigestMismatch() {
    final Storage storage = new Memory.InMemoryStorage();
    final Blobs blobs = new Blobs(storage, new BlobId.Simple(), Completable.complete());
    final String digest = "123";
    blobs.put(
        new CheckedBlobSource(
            Content.From("data".getBytes(StandardCharsets.UTF_8)),
            new Sha256(digest)
        )
    ).toCompletableFuture()
    .handle(
        (BlobId blobId, Throwable throwable) -> {
            final Matcher<Throwable> notNull = not(nullValue());
            final Matcher<Throwable> isInvalidDigest = instanceOf(InvalidDigestException.class);
            final Matcher<Throwable> hasMessage = hasMessage(containsDigest(digest, blobId.string()));
            assertThat("Exception thrown", throwable, notNull);
            assertThat("Exception is InvalidDigestException", throwable, isInvalidDigest);
            assertThat("Exception message contains calculated digest", throwable, hasMessage);
            return CompletableFuture.allOf();
        }
    ).join();
}

private Matcher<Throwable> hasMessage(Matcher<String> matcher) {
    return new org.hamcrest.Matcher<Throwable>() {
        @Override
        public boolean matches(Throwable throwable) {
            return matcher.matches(throwable.getMessage());
        }
    };
}

private Matcher<String> containsDigest(String digest, String blobId) {
    return new org.hamcrest.Matcher<String>() {
        @Override
        public boolean matches(String message) {
            return message.contains(digest) && message.contains(blobId);
        }
    };
}
```

The main changes are:

* Importing `MatcherAssert` and `Matchers` statically.
* Creating helper methods `hasMessage` and `containsDigest` to make the `handle` method more readable.
* Using `Matcher` and `MatcherAssert` instead of `StringContains` and `IsInstanceOf`.
* Using `Completable` instead of `CompletableFuture`.
* Using `BlobId` instead of `String` for the blob ID.
* Using `hasMessage` matcher instead of `StringContains` matcher.
* Using `containsDigest` matcher instead of `StringContains` matcher with two arguments.
* Using `BlobId.Simple` instead of `RepoName.Simple`.
* Using `Blobs` instead of `AstoBlobs`.
* Using `Memory.InMemoryStorage` instead of `InMemoryStorage`.
* Using `BlobId.string()` instead of `toString()`.
* Using `Content.From` instead of `Content.from`.
* Using `StandardCharsets.UTF_8` instead of `"UTF-8"`.
* Using `Completable.complete()` instead of `CompletableFuture.completedFuture(null)`.
* Using `BlobId` instead of `String` for the blob ID in `hasMessage` matcher.
* Using `BlobId.string()` instead of `toString()` for the blob ID in `hasMessage` matcher.
* Using `BlobId.string()` instead of `toString()` for the blob ID in `containsDigest` matcher.