Here's a possible patch for the code you provided. I added a helper method `stringContains` to handle the `StringContains` matcher with a boolean flag:

```java
import org.hamcrest.CoreMatchers;
import org.hamcrest.MatcherAssert;
import org.junit.jupiter.api.Test;

import java.nio.charset.StandardCharsets;
import java.util.concurrent.CompletableFuture;
import java.util.concurrent.ExecutionException;

import static com.artipie.docker.asto.AstoBlobsITCase.stringContains;

public class AstoBlobsITCase {
    @Test
    void failsOnDigestMismatch() throws ExecutionException, InterruptedException {
        final com.artipie.asto.memory.InMemoryStorage storage = new com.artipie.asto.memory.InMemoryStorage();
        final com.artipie.docker.asto.AstoBlobs blobs = new com.artipie.docker.asto.AstoBlobs(storage, new com.artipie.docker.asto.DefaultLayout(), new com.artipie.docker.RepoName.Simple("any"));
        final java.lang.String digest = "123";
        blobs.put(new com.artipie.docker.asto.CheckedBlobSource(new com.artipie.asto.Content.From("data".getBytes()), new com.artipie.docker.Digest.Sha256(digest))).toCompletableFuture().handle(( blob, throwable) -> {
            MatcherAssert.assertThat("Exception thrown", throwable, CoreMatchers.notNullValue());
            MatcherAssert.assertThat("Exception is InvalidDigestException", throwable, CoreMatchers.instanceOf(com.artipie.docker.error.InvalidDigestException.class));
            MatcherAssert.assertThat("Exception message contains calculated digest", stringContains(throwable.getMessage(), "3a6eb0790f39ac87c94f3856b2dd2c5d110e6811602261a9a923d3bb23adc8b7"), CoreMatchers.is(true));
            MatcherAssert.assertThat("Exception message contains expected digest", stringContains(throwable.getMessage(), digest), CoreMatchers.is(true));
            return CompletableFuture.allOf();
        }).join();
    }

    static boolean stringContains(String haystack, String needle) {
        return haystack.contains(needle);
    }
}
```

The issue with the original code was that the `StringContains` constructor was being called with an incorrect number of arguments. Instead, I created a helper method `stringContains` that accepts a `String` and a `String` and returns a `boolean`. This method checks if the first `String` contains the second `String`. I then used this helper method in the `handle` method of the `CompletableFuture`.