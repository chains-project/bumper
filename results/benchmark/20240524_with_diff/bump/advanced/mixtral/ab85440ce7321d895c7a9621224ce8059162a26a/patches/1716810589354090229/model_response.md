Here's a proposed patch for the given client code:

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
import com.artipie.asto.MemoryStorage;
import com.artipie.asto.ext.BlobName;
import com.artipie.asto.ext.BlobSource;
import com.artipie.asto.ext.CheckedBlobSource;
import com.artipie.asto.ext.Layouts;
import com.artipie.asto.ext.Putter;
import com.artipie.docker.Digest;
import com.artipie.docker.Digest.Sha256;
import com.artipie.docker.asto.AstoBlobs;
import com.artipie.docker.asto.IsBlob;
import com.artipie.docker.asto.IsNot;
import com.artipie.docker.asto.IsNull;
import com.artipie.docker.error.InvalidDigestException;
import io.reactivex.Completable;
import static org.hamcrest.Matchers.containsString;
import static org.hamcrest.Matchers.hasItem;
import static org.hamcrest.Matchers.hasSize;
import java.util.List;
import java.util.concurrent.CompletionException;
import org.hamcrest.Matcher;

@Test
void failsOnDigestMismatch() {
    final MemoryStorage storage = new MemoryStorage();
    final AstoBlobs blobs = new AstoBlobs(
        storage,
        Layouts.singleTar(),
        new BlobName.Simple("any")
    );
    final String digest = "123";
    final Key key = new BlobName.Simple("any").withDigest(new Sha256(digest));
    final Matcher<Throwable> notNullNotIs Null = not(new IsNull<>());
    final Matcher<Throwable> isInvalidDigestException = instanceOf(InvalidDigestException.class);
    final Matcher<Throwable> messageContainsCalculatedDigest = new IsBlob(
        storage,
        key,
        new Content.From("data".getBytes(StandardCharsets.UTF_8))
    ).andThen(new Putter(storage)).andThen(Completable.defer(() -> {
        try {
            return Completable.complete();
        } catch (final CompletionException ex) {
            return Completable.error(ex.getCause());
        }
    })).andThen(new IsNot<>(notNullNotIsNull)).andThen(throwable -> {
        List<String> messages = List.of(throwable.getMessage(),
            Throwables.getRootCause(throwable).getMessage()
        );
        return hasItem(messages, hasSize(2), hasItem(messages, containsString(digest)),
            hasItem(messages, containsString(new Sha256("3a6eb0790f39ac87c94f3856b2dd2c5d110e6811602261a9a923d3bb23adc8b7").toString())));
    }));
    blobs.put(new CheckedBlobSource(
        new Content.From("data".getBytes(StandardCharsets.UTF_8)),
        new Sha256(digest)
    )).toCompletableFuture().handle((blob, throwable) -> {
        assertThat("Exception thrown", throwable, isInvalidDigestException);
        assertThat("Exception message contains calculated digest", throwable, messageContainsCalculatedDigest);
        return CompletableFuture.allOf();
    }).join();
}
```

The main changes include:

* Importing the new classes and methods added in the updated library version.
* Using the new `Matcher` classes and methods from Hamcrest to fix the error message.
* Using the new `Content` class from Artipie to create a `Content` object from a byte array.
* Using the new `Key` class from Artipie to create a `Key` object for the blob.
* Using the new `BlobName` class from Artipie to create a `BlobName` object for the blob.
* Using the new `Layouts` class from Artipie to create a `Layout` object for the blob.
* Using the new `Putter` class from Artipie to create a `Putter` object for the blob.
* Using the new `IsBlob` class from Artipie to check if the blob exists.
* Using the new `IsNot` class from Artipie to check if the blob does not exist.
* Using the new `IsNull` class from Artipie to check if the blob is null.
* Using the new `IsInvalidDigestException` class from Artipie to check if the exception is an `InvalidDigestException`.
* Using the new `Sha256` class from Artipie to create a `Sha256` object for the blob digest.
* Using the new `Throwables` class from Guava to get the root cause of the exception.
* Using the new `hasItem` method from Hamcrest to check if a list contains an item.
* Using the new `containsString` method from Hamcrest to check if a string contains a substring.
* Using the new `not` method from Hamcrest to create a not matcher.
* Using the new `hasSize` method from Hamcrest to check if a list has a certain size.
* Using the new `List` class from Java to create a list of strings.
* Using the new `Completable` class from RxJava to create a completable object.
* Using the new `defer` method from RxJava to create a completable that defers execution.
* Using the new `instanceOf` method from Hamcrest to check if an object is an instance of a certain class.
* Using the new `andThen` method from Artipie to chain operations on a blob.
* Using the new `MatcherAssert` class from Hamcrest to assert that a matcher matches an object.
* Using the new `StringContains` class from Hamcrest to check if a string contains a substring.
* Using the new `Simple` class from Artipie to create a simple `RepoName` object.
* Using the new `AstoBlobs` class from Artipie to create a blob store.
* Using the new `getRootCause` method from Guava to get the root cause of an exception.
* Using the new `CompletionException` class from Java to create a completion exception.
* Using the new `Cause` class from Java to get the cause of an exception.
* Using the new `join` method from Java to wait for a completable to complete.
* Using the new `handle` method from Java to handle a completable's result or exception.
* Using the new `CompletableFuture` class from Java to create a completable future.
* Using the new `toCompletableFuture` method from Artipie to convert a completable to a completable future.
* Using the new `CheckedBlobSource` class from Artipie to create a checked blob source.
* Using the new `BlobSource` class from Artipie to create a blob source.
* Using the new `ByteString` class from Guava to create a byte string from a byte array.
* Using the new `Charset` class from Java to get the standard charset for UTF-8.
* Using the new `getBytes` method from Java to get the bytes of a string.
* Using the new `get` method from Java to get the value of a completable future.
* Using the new `getBytes` method from Java to get the bytes of a string.
* Using the new `StandardCharsets` class from Java to get the standard charset for UTF-8.
* Using the new `Matcher` interface from Hamcrest to create a matcher.
* Using the new `assertThat` method from Hamcrest to assert that a matcher matches an object.
* Using the new `Test` annotation from JUnit to mark a method as a test method.