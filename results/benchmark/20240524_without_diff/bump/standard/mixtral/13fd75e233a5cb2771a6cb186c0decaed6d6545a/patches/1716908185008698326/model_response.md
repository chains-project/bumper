Here is a possible patch for the failing client code:
```java
import static org.hamcrest.MatcherAssert.assertThat;
import static org.hamcrest.Matchers.instanceOf;
import static org.hamcrest.Matchers.not;
import static org.hamcrest.core.IsEqual.equalTo;
import java.nio.charset.StandardCharsets;
import java.util.concurrent.CompletableFuture;
import org.junit.jupiter.api.Test;
import com.artipie.asto.Content;
import com.artipie.asto.Key;
import com.artipie.asto.Storage;
import com.artipie.asto.memory.InMemoryStorage;
import com.artipie.docker.asto.AstoBlobs;
import com.artipie.docker.asto.CheckedBlobSource;
import com.artipie.docker.digest.CanonicalBlob;
import com.artipie.docker.digest.DefaultDigest;
import com.artipie.docker.digest.Digest;
import com.artipie.docker.digest.Digger;
import com.artipie.docker.error.InvalidDigestException;
import com.google.common.base.Throwables;
import io.reactivex.Single;

@Test
void failsOnDigestMismatch() {
    final Storage storage = new InMemoryStorage();
    final AstoBlobs blobs = new AstoBlobs(
        storage,
        new DefaultLayout(),
        new RepoName.Simple("any")
    );
    final String digest = "123";
    final Key key = new Key.From("data".getBytes(StandardCharsets.UTF_8));
    final Content content = Content.From("data".getBytes(StandardCharsets.UTF_8));
    final CanonicalBlob canonicalBlob = new CanonicalBlob(content);
    final Digest calculatedDigest = new DefaultDigest(
        new Digger.Sha256().digest(Single.just(canonicalBlob))
    );
    blobs.put(
        new CheckedBlobSource(content, new Digest.Sha256(calculatedDigest.value()))
    ).toCompletableFuture().handle(
        (blob, throwable) -> {
            assertThat("Exception thrown", throwable, not(equalTo(null)));
            assertThat(
                "Exception is InvalidDigestException",
                throwable,
                instanceOf(InvalidDigestException.class)
            );
            assertThat(
                "Exception message contains calculated digest",
                Throwables.getRootCause(throwable).getMessage(),
                new StringContains(calculatedDigest.value())
            );
            assertThat(
                "Exception message contains expected digest",
                Throwables.getRootCause(throwable).getMessage(),
                new StringContains(digest)
            );
            return CompletableFuture.allOf();
        }
    ).join();
}

private static class StringContains implements org.hamcrest.Matcher<String> {
    private final String value;

    StringContains(String value) {
        this.value = value;
    }

    @Override
    public boolean matches(Object item) {
        return ((String) item).contains(value);
    }

    @Override
    public void describeTo(org.hamcrest.Description description) {
        description.appendText("string containing ").appendValue(value);
    }
}
```
The main changes are:

* The `StringContains` class is defined to fix the issue with the `StringContains` constructor.
* The `CanonicalBlob` and `DefaultDigest` classes are used to calculate the digest of the uploaded data.
* The `Key` and `Content` classes are used to create the `CheckedBlobSource` object.
* The `StringContains` class is used to check if the exception message contains the expected digest.
* The `instanceOf` and `not` matchers are used to check if the exception is an `InvalidDigestException` and if it is not null.
* The `StringContains` matcher is used to check if the exception message contains the calculated digest.
* The `StringContains` matcher is used to check if the exception message contains the expected digest.
* The `CompletableFuture.allOf()` method is used to wait for the completion of the `handle` method.
* The `Key.From` and `Content.From` methods are used to create the `Key` and `Content` objects.
* The `Digger.Sha256` class is used to calculate the digest of the uploaded data.
* The `InMemoryStorage` class is used to create the `Storage` object.
* The `defaultLayout` field is removed, as it is not used in the test method.
* The `RepoName.Simple` class is used to create the `RepoName` object.
* The `CheckedBlobSource` class is used to create the `CheckedBlobSource` object.
* The `put` method of the `AstoBlobs` class is used to upload the data.
* The `handle` method of the `CompletableFuture` class is used to handle the result of the `put` method.
* The `join` method of the `CompletableFuture` class is used to wait for the completion of the `handle` method.