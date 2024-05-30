Here's a proposed patch for the client code:

```java
import java.util.concurrent.CompletableFuture;
import org.hamcrest.MatcherAssert;
import org.hamcrest.Matchers;
import com.artipie.asto.Content;
import com.artipie.asto.CheckedBlobSource;
import com.artipie.asto.memory.InMemoryStorage;
import com.artipie.docker.asto.AstoBlobs;
import com.artipie.docker.asto.DefaultLayout;
import com.artipie.docker.Digest;
import com.artipie.docker.RepoName;
import com.artipie.docker.error.InvalidDigestException;

@org.junit.jupiter.api.Test
void failsOnDigestMismatch() {
    final InMemoryStorage storage = new InMemoryStorage();
    final AstoBlobs blobs = new AstoBlobs(storage, new DefaultLayout(), new RepoName.Simple("any"));
    final String digest = "123";
    blobs.put(new CheckedBlobSource(new Content.From("data".getBytes()), new Digest.Sha256(digest))).toCompletableFuture()
        .handle((blob, throwable) -> {
            MatcherAssert.assertThat("Exception thrown", throwable, Matchers.notNullValue());
            MatcherAssert.assertThat("Exception is InvalidDigestException", throwable, Matchers.instanceOf(InvalidDigestException.class));
            MatcherAssert.assertThat("Exception message contains calculated digest", throwable.getMessage(), Matchers.stringContains("3a6eb0790f39ac87c94f3856b2dd2c5d110e6811602261a9a923d3bb23adc8b7"));
            MatcherAssert.assertThat("Exception message contains expected digest", throwable.getMessage(), Matchers.stringContains(digest));
            return CompletableFuture.allOf();
        }).join();
}
```

The changes made include:

* Replacing the deprecated `StringContains` constructor with the `stringContains` method.
* Replacing the `IsNot` and `IsNull` matchers with the `notNullValue` matcher.
* Replacing the `IsInstanceOf` matcher with the `instanceOf` method.
* Removing the unnecessary type declarations for `MatcherAssert`, `Matchers`, and `CompletableFuture`.
* Adding import statements for the `Content` and `RepoName` classes.
* Renaming the `CheckedBlobSource` constructor argument from `source` to `blob`.
* Removing the unnecessary `true` argument from the `stringContains` matcher.
* Adding a missing semicolon at the end of the `handle` method call.