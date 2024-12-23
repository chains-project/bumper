```java
  import java.io.UncheckedIOException;
  import com.artipie.http.Response;
  import com.artipie.http.Slice;
  import com.artipie.http.rq.RequestLine;
  import com.artipie.http.rs.RsStatus;
  import com.artipie.http.rs.StandardRs;
  import com.artipie.security.policy.Policy;
  import com.artipie.security.policy.YamlPolicy;
  import java.io.IOException;
  import java.nio.file.Files;
  import java.nio.file.Path;
  import java.nio.file.Paths;
  import java.util.concurrent.CompletableFuture;
  import java.util.concurrent.CompletionStage;

  public final class YamlPolicyFactory implements Slice {
    private final Path path;

    public YamlPolicyFactory(final Path path) {
      this.path = path;
    }

    @Override
    public CompletionStage<Response> response(final RequestLine request) {
      try {
        final Policy policy = new YamlPolicy(Files.newInputStream(this.path));
        return CompletableFuture.completedFuture(
          new StandardRs(
            RsStatus.OK,
            policy.serialize()
          )
        );
      } catch (final IOException e) {
        throw new UncheckedIOException(e);
      }
    }
  }
```