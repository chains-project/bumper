Here's a suggested patch for the given client code:

```java
import com.artipie.asto.Content;
import com.artipie.asto.Key;
import com.artipie.asto.Storage;
import com.artipie.asto.ext.ExtAsto;
import com.artipie.docker.Digest;
import com.artipie.docker.CheckedBlobSource;
import com.artipie.docker.asto.AstoBlobs;
import com.artipie.docker.asto.DefaultLayout;
import com.artipie.docker.RepoName;
import com.artipie.docker.error.InvalidDigestException;
import org.hamcrest.MatcherAssert;
import org.hamcrest.core.IsInstanceOf;
import org.hamcrest.core.StringContains;
import org.hamcrest.core.StringStartsWith;
import org.junit.jupiter.api.Test;
import java.nio.ByteBuffer;
import java.nio.charset.StandardCharsets;
import java.util.concurrent.CompletableFuture;

import static com.artipie.asto.ext.ExtAsto.content;
import static org.hamcrest.core.IsNot.not;
import static org.mockito.Mockito.mock;
import static org.mockito.Mockito.when;

@Test
void failsOnDigestMismatch() {
    final Storage storage = mock(Storage.class);
    final AstoBlobs blobs = new AstoBlobs(storage, new DefaultLayout(), new RepoName.Simple("any"));
    final String digest = "123";
    final Key key = new Key.From("any", Digest.Sha256.name(), digest);
    final Content content = content(ByteBuffer.wrap("data".getBytes(StandardCharsets.UTF_8)));
    when(storage.save(key, content)).thenAnswer(invocation -> {
        throw new InvalidDigestException("Invalid digest: " + digest);
    });
    blobs.put(new CheckedBlobSource(content, new Digest.Sha256(digest))).toCompletableFuture().handle((blob, throwable) -> {
        MatcherAssert.assertThat("Exception thrown", throwable, not(new IsInstanceOf(IllegalStateException.class)));
        MatcherAssert.assertThat("Exception is InvalidDigestException", throwable, new IsInstanceOf(InvalidDigestException.class));
        MatcherAssert.assertThat("Exception message contains calculated digest", throwable.getMessage(), new StringStartsWith(new StringValue(new StringBuilder("3a6eb0790f39ac87c94f3856b2dd2c5d110e6811602261a9a923d3bb23adc8b7").toString())));
    });
    MatcherAssert.assertThat("Exception message contains expected digest", throwable.getMessage(), new StringContains(digest));
    return CompletableFuture.allOf();
}
```

This patch includes a mock of the `Storage` class, which throws an `InvalidDigestException` when the `save` method is called. This allows the test to check for the expected exception and message. Additionally, the `IsNot` class is replaced with `not`, which is a static import from `org.hamcrest.core`. The `content` method is imported from `com.artipie.asto.ext.ExtAsto` to simplify the creation of the `Content` object.