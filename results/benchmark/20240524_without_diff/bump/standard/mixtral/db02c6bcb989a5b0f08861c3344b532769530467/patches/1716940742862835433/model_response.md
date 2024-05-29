Here's a possible patch for the code you provided. I added a `containsString` method to check if the exception message contains the expected digest.

```java
import java.nio.charset.StandardCharsets;
import java.util.concurrent.CompletableFuture;
import org.hamcrest.MatcherAssert;
import org.hamcrest.Matchers;
import org.junit.jupiter.api.Test;
import com.artipie.asto.Content;
import com.artipie.asto.MemoryStorage;
import com.artipie.asto.ext.Key;
import com.artipie.docker.asto.AstoBlobs;
import com.artipie.docker.asto.CheckedBlobSource;
import com.artipie.docker.Digest;
import com.artipie.docker.error.InvalidDigestException;

@Test
void failsOnDigestMismatch() {
    final MemoryStorage storage = new MemoryStorage();
    final AstoBlobs blobs = new AstoBlobs(storage, new DefaultLayout(), new RepoName.Simple("any"));
    final String digest = "123";
    blobs.put(new CheckedBlobSource(new Content.From("data".getBytes()), new Digest.Sha256(digest)))
        .toCompletableFuture()
        .handle((blob, throwable) -> {
            MatcherAssert.assertThat("Exception thrown", throwable, Matchers.notNullValue());
            MatcherAssert.assertThat("Exception is InvalidDigestException", throwable, Matchers.instanceOf(InvalidDigestException.class));
            MatcherAssert.assertThat("Exception message contains calculated digest", containsString(throwable.getMessage(), "3a6eb0790f39ac87c94f3856b2dd2c5d110e6811602261a9a923d3bb23adc8b7"));
            MatcherAssert.assertThat("Exception message contains expected digest", containsString(throwable.getMessage(), digest));
            return CompletableFuture.allOf();
        })
        .join();
}

private boolean containsString(String haystack, String needle) {
    return haystack.contains(needle);
}
```

Note that I changed the `MatcherAssert.assertThat` calls that were causing the error, and added a `containsString` method to check if the exception message contains the expected digest. I also imported the missing classes and interfaces.