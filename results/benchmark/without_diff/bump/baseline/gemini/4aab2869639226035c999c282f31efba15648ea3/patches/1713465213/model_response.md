```java
  import java.io.UncheckedIOException;
import com.artipie.http.Headers;
import com.artipie.http.Response;
import com.artipie.http.Slice;
import com.artipie.http.async.AsyncResponse;
import com.artipie.http.rs.RsStatus;
import com.artipie.http.rs.RsWithHeaders;
import com.artipie.http.rs.RsWithStatus;
import com.artipie.security.Policy;
import com.artipie.security.policy.JdkPolicy;
import com.artipie.security.policy.YamlPolicyFactory;
import java.io.IOException;
import java.io.UncheckedIOException;
import java.nio.ByteBuffer;
import java.security.Principal;
import java.util.concurrent.CompletionStage;
import java.util.concurrent.atomic.AtomicInteger;
import java.util.function.Function;

public final class YamlPolicyFactory implements Function<Headers, Slice> {

  private final String path;

  public YamlPolicyFactory(final String path) {
    this.path = path;
  }

  @Override
  public Slice apply(final Headers headers) {
    return new Slice() {
      @Override
      public Response response(final String line, final Iterable<String> lines,
          final Principal principal) {
        return new RsWithHeaders(
            new RsWithStatus(
                new AsyncResponse(
                    (response, ex) -> {
                      if (ex != null) {
                        response.send(new RsStatus(RsStatus.BAD_REQUEST));
                      } else {
                        try {
                          final Policy policy;
                          if (this.path.endsWith(".yaml")) {
                            policy = new YamlPolicyFactory(this.path).create();
                          } else {
                            policy = new YamlPolicyFactory(this.path + ".yaml").create();
                          }
                          response.send(new RsWithStatus(policy.response(headers)));
                        } catch (final IOException e) {
                          throw new UncheckedIOException(e);
                        }
                      }
                    }
                ),
                RsStatus.OK
            ),
            new Headers.From(
                "Content-Type", "application/json"
            )
        );
      }

      private Policy create() throws IOException {
        return new JdkPolicy(this.path);
      }
    };
  }
}
```