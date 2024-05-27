Here's a possible patch for the given client code:

```java
import org.hamcrest.Matchers;
import org.junit.jupiter.api.Test;

import java.nio.charset.StandardCharsets;
import java.util.concurrent.CompletableFuture;

import static com.artipie.docker.asto.AstoBlobsITCase.content;
import static com.artipie.docker.asto.AstoBlobsITCase.repoName;
import static org.hamcrest.MatcherAssert.assertThat;
import static org.hamcrest.Matchers.instanceOf;

@Test
void failsOnDigestMismatch() {
    final com.artipie.asto.memory.InMemoryStorage storage = new com.artipie.asto.memory.InMemoryStorage();
    final com.artipie.docker.asto.AstoBlobs blobs = new com.artipie.docker.asto.AstoBlobs(
        storage, new com.artipie.docker.asto.DefaultLayout(), repoName("any")
    );
    final String digest = "123";
    blobs.put(
        new com.artipie.docker.asto.CheckedBlobSource(
            content("data".getBytes(StandardCharsets.UTF_8)),
            new com.artipie.docker.Digest.Sha256(digest)
        )
    ).toCompletableFuture().handle(
        (blob, throwable) -> {
            assertThat("Exception thrown", throwable, Matchers.notNullValue());
            assertThat(
                "Exception is InvalidDigestException",
                throwable,
                instanceOf(com.artipie.docker.error.InvalidDigestException.class)
            );
            assertThat(
                "Exception message contains calculated digest",
                throwable.getMessage(),
                Matchers.stringContains(
                    "3a6eb0790f39ac87c94f3856b2dd2c5d110e6811602261a9a923d3bb23adc8b7"
                )
            );
            assertThat(
                "Exception message contains expected digest",
                throwable.getMessage(),
                Matchers.stringContains(digest)
            );
            return CompletableFuture.allOf();
        }
    ).join();
}

static byte[] content(final String string) {
    return content(string.getBytes(StandardCharsets.UTF_8));
}

static byte[] content(final byte[] bytes) {
    return bytes;
}

static com.artipie.docker.RepoName.RepoName repoName(final String name) {
    return new com.artipie.docker.RepoName.Simple(name);
}
```

The changes I made are:

* I imported `Matchers` from `org.hamcrest` package to use it instead of `StringContains`.
* I changed the `StringContains` matcher to use `Matchers.stringContains` instead.
* I added two helper methods `content` and `repoName` to make the code more readable.
* I changed the `handle` method to use `Matchers.notNullValue()` instead of `new com.artipie.docker.asto.IsNot<>(new com.artipie.docker.asto.IsNull<>()`).

These changes should fix the error message and make the code more readable.