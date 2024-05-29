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
import com.artipie.asto.MemoryStorage;
import com.artipie.asto.Storage;
import com.artipie.asto.ext.ExtendedCheckedBlobSource;
import com.artipie.asto.ext.ExtendedLayout;
import com.artipie.docker.Digest;
import com.artipie.docker.RepoName;
import com.artipie.docker.asto.AstoBlobs;
import com.artipie.docker.asto.CheckedBlobSource;
import com.google.common.base.Throwables;
import org.hamcrest.Matcher;

@Test
void failsOnDigestMismatch() {
    final Storage storage = new MemoryStorage();
    final ExtendedLayout layout = new ExtendedLayout();
    final RepoName repoName = new RepoName.Simple("any");
    final String digest = "123";
    final Content content = Content.From("data".getBytes(StandardCharsets.UTF_8));
    final Digest calculatedDigest = Digest.sha256("3a6eb0790f39ac87c94f3856b2dd2c5d110e6811602261a9a923d3bb23adc8b7");
    final CheckedBlobSource checkedBlobSource = new ExtendedCheckedBlobSource(content, calculatedDigest);
    final Matcher<Throwable> notNullMatcher = not(nullValue());
    final Matcher<Throwable> isInvalidDigestException = instanceOf(InvalidDigestException.class);
    final Matcher<Throwable> messageContainsCalculatedDigest = new MessageContains(calculatedDigest.toString());
    final Matcher<Throwable> messageContainsExpectedDigest = new MessageContains(digest);
    AstoBlobs.put(new AstoBlobs(storage, layout, repoName), checkedBlobSource)
        .toCompletableFuture()
        .handle((blob, throwable) -> {
            assertThat("Exception thrown", throwable, notNullMatcher);
            assertThat("Exception is InvalidDigestException", throwable, isInvalidDigestException);
            assertThat("Exception message contains calculated digest", throwable, messageContainsCalculatedDigest);
            assertThat("Exception message contains expected digest", throwable, messageContainsExpectedDigest);
            return CompletableFuture.allOf();
        })
        .join();
}

private static class MessageContains implements Matcher<Throwable> {
    private final String message;

    private MessageContains(String message) {
        this.message = message;
    }

    @Override
    public boolean matches(Object item) {
        return item instanceof Throwable && ((Throwable) item).getMessage().contains(message);
    }

    @Override
    public void describeTo(org.hamcrest.Description description) {
        description.appendText("message contains ").appendValue(message);
    }
}
```

The main changes are:

* Importing the necessary classes at the beginning of the file.
* Creating a new `Content` object using the `Content.From` method.
* Creating a new `Digest` object using the `Digest.sha256` method.
* Creating a new `ExtendedCheckedBlobSource` object using the `ExtendedCheckedBlobSource` constructor.
* Creating new `Matcher` objects for the `assertThat` statements.
* Creating a new `MessageContains` class that implements the `Matcher` interface.
* Replacing the `StringContains` matcher with the new `MessageContains` matcher.
* Adding a lambda expression to the `handle` method to simplify the code.
* Adding a `join` method call at the end of the `handle` method to wait for the completion of the `CompletableFuture`.

Note that these changes are just one possible solution to fix the error message. There might be other ways to solve the issue.