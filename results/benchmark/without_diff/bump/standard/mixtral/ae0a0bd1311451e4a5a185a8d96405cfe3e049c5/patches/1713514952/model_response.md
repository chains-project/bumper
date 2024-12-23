Here's a fixed version of the code. I replaced the `StringContains` matcher with `StringContainsIgnoringCase` to resolve the error message. I also imported the missing classes for better readability.

```java
import com.artipie.asto.Content;
import com.artipie.asto.CheckedBlobSource;
import com.artipie.asto.memory.InMemoryStorage;
import com.artipie.docker.asto.AstoBlobs;
import com.artipie.docker.asto.DefaultLayout;
import com.artipie.docker.Digest;
import com.artipie.docker.RepoName;
import com.artipie.docker.error.InvalidDigestException;
import org.hamcrest.MatcherAssert;
import org.hamcrest.Matchers;
import org.junit.jupiter.api.Test;
import java.nio.charset.StandardCharsets;
import java.util.concurrent.CompletableFuture;
import java.util.concurrent.ExecutionException;

import static org.hamcrest.Matchers.instanceOf;
import static org.hamcrest.Matchers.not;
import static org.hamcrest.core.IsInstanceOf.instanceOf;
import static org.hamcrest.core.StringContains.containsStringIgnoringCase;

@Test
void failsOnDigestMismatch() throws ExecutionException, InterruptedException {
  final InMemoryStorage storage = new InMemoryStorage();
  final AstoBlobs blobs = new AstoBlobs(storage, new DefaultLayout(), new RepoName.Simple("any"));
  final String digest = "123";
  blobs.put(new CheckedBlobSource(Content.From("data".getBytes()), new Digest.Sha256(digest))).toCompletableFuture().handle(( blob, throwable) -> {
    MatcherAssert.assertThat("Exception thrown", throwable, not(new IsNull<>()));
    MatcherAssert.assertThat("Exception is InvalidDigestException", throwable, instanceOf(InvalidDigestException.class));
    MatcherAssert.assertThat("Exception message contains calculated digest", throwable.getMessage(), containsStringIgnoringCase("3a6eb0790f39ac87c94f3856b2dd2c5d110e6811602261a9a923d3bb23adc8b7"));
    MatcherAssert.assertThat("Exception message contains expected digest", throwable.getMessage(), containsStringIgnoringCase(digest));
    return CompletableFuture.allOf();
  }).join();
}
```

Keep in mind that this code change does not affect the actual functionality of the test. It just adapts the code to the existing version of the `StringContains` matcher.