```java
  import java.io.UncheckedIOException;
  import java.util.Map;

  import com.artipie.http.Headers;
  import com.artipie.http.Response;
  import com.artipie.http.Slice;
  import com.artipie.http.rq.RequestLineFrom;
  import com.artipie.http.rq.RqHeaders;
  import com.artipie.http.rs.RsStatus;
  import com.artipie.http.rs.RsWithHeaders;
  import com.artipie.http.rs.RsWithStatus;
  import com.artipie.security.CheckedSlice;
  import com.artipie.security.Policy;
  import com.artipie.security.policy.YamlPolicyFactory;
  import com.google.common.collect.ImmutableMap;
  import java.io.ByteArrayInputStream;
  import java.io.IOException;
  import java.io.InputStream;
  import java.nio.charset.StandardCharsets;
  import java.util.concurrent.CompletableFuture;
  import java.util.concurrent.CompletionStage;

  /**
  * Policy factory.
  *
  * @since 0.2
  */
  public final class YamlPolicyFactory implements Policy.Factory {

    /**
    * Policy.
    */
    private final Policy policy;

    /**
    * Ctor.
    *
    * @param policy Policy
    */
    public YamlPolicyFactory(final Policy policy) {
      this.policy = policy;
    }

    @Override
    public Slice asSlice(final Slice origin) {
      return new CheckedSlice(
        origin,
        this.policy,
        request -> {
          final String path = new RequestLineFrom(request).uri().getPath();
          final InputStream stream = new ByteArrayInputStream(
            ("GET " + path + " HTTP/1.1\r\n"
              + "Host: localhost:8080\r\n"
              + "Connection: close\r\n"
              + "\r\n").getBytes(StandardCharsets.UTF_8)
          );
          return new RqHeaders(stream).read()
            .thenApply(
              headers -> {
                final Map<String, String> map
                  = ImmutableMap.<String, String>builder()
                  .putAll(headers.asMap())
                  .put("X-Forwarded-For", "127.0.0.1")
                  .build();
                return new RsWithHeaders(
                  new RsWithStatus(RsStatus.OK),
                  new Headers.From(map)
                );
              }
            );
        }
      );
    }
  }
```