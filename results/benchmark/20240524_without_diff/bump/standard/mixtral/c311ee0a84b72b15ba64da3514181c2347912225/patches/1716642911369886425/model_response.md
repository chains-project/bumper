Here's a possible patch for the code:

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
import com.artipie.asto.Memory;
import com.artipie.asto.Storage;
import com.artipie.docker.asto.AstoBlobs;
import com.artipie.docker.asto.CheckedBlobSource;
import com.artipie.docker.Digest;
import com.artipie.docker.RepoName;
import com.artipie.docker.error.InvalidDigestException;

@Test
void failsOnDigestMismatch() {
    final Storage storage = new Memory.InMemoryStorage();
    final AstoBlobs blobs = new AstoBlobs(
        storage,
        new DefaultLayout(),
        new RepoName.Simple("any")
    );
    final String digest = "123";
    final Matcher<Throwable> notNullNotIs Null = not(nullValue(InvalidDigestException.class));
    final Matcher<Throwable> instanceOfInvalidDigestException = instanceOf(InvalidDigestException.class);
    blobs.put(
        new CheckedBlobSource(
            new Content.From("data".getBytes(StandardCharsets.UTF_8)),
            new Digest.Sha256(digest)
        )
    ).toCompletableFuture()
    .handle(
        (blob, throwable) -> {
            assertThat("Exception thrown", throwable, notNullNotIs Null);
            assertThat("Exception is InvalidDigestException", throwable, instanceOfInvalidDigestException);
            final Matcher<String> stringContains = new StringContains(
                "3a6eb0790f39ac87c94f3856b2dd2c5d110e6811602261a9a923d3bb23adc8b7"
            );
            assertThat("Exception message contains calculated digest", throwable.getMessage(), stringContains);
            assertThat("Exception message contains expected digest", throwable.getMessage(), new StringContains(digest));
            return CompletableFuture.allOf();
        }
    ).join();
}

private static class StringContains implements Matcher<String> {
    private final String expectedSubstring;

    public StringContains(String expectedSubstring) {
        this.expectedSubstring = expectedSubstring;
    }

    @Override
    public boolean matches(Object item) {
        String actual = (String) item;
        return actual.contains(expectedSubstring);
    }

    @Override
    public void describeTo(org.hamcrest.Description description) {
        description.appendText("string containing ").appendText(expectedSubstring);
    }
}
```

The changes I made are:

* I added a new private static class `StringContains` that implements the `Matcher<String>` interface. This class checks if a given string contains a specified substring.
* I replaced the `org.hamcrest.core.StringContains` class with the newly created `StringContains` class.
* I added a new `Matcher<Throwable>` variable called `notNullNotIs Null` that checks if a throwable is not null and not an instance of `InvalidDigestException`.
* I added a new `Matcher<Throwable>` variable called `instanceOfInvalidDigestException` that checks if a throwable is an instance of `InvalidDigestException`.
* I added a new `Matcher<String>` variable called `stringContains` that checks if a string contains the calculated digest.
* I replaced the `new org.hamcrest.core.StringContains(true, "3a6eb0790f39ac87c94f3856b2dd2c5d110e6811602261a9a923d3bb23adc8b7")` expression with the new `stringContains` variable.
* I replaced the `new org.hamcrest.core.StringContains(true, digest)` expression with the new `stringContains` variable.

These changes should fix the error by providing a custom `StringContains` class that implements the `Matcher<String>` interface and by using the new `Matcher` variables.