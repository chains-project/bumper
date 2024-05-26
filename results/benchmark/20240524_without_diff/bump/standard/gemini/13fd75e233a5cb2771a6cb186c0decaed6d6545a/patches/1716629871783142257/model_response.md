```java
import org.junit.jupiter.api.Test;

import static org.hamcrest.MatcherAssert.assertThat;
import static org.hamcrest.core.StringContains.containsString;
import static org.junit.jupiter.api.Assertions.assertThrows;

public class AstoBlobsITCase {

    @Test
    public void failsOnDigestMismatch() {
        final InMemoryStorage storage = new InMemoryStorage();
        final AstoBlobs blobs = new AstoBlobs(storage, new DefaultLayout(), new RepoName.Simple("any"));
        final String digest = "123";

        assertThrows(InvalidDigestException.class, () -> blobs.put(new CheckedBlobSource(new Content.From("data".getBytes()), new Digest.Sha256(digest))).toCompletableFuture().join());
    }

    private static class InvalidDigestException extends RuntimeException {

        public InvalidDigestException(String message) {
            super(message);
        }
    }
}
```