```java
  import java.io.UncheckedIOException;
  import java.util.Optional;
  import com.artipie.http.Headers;
  import com.artipie.http.Response;
  import com.artipie.http.Slice;
  import com.artipie.http.rq.RequestLine;
  import com.artipie.http.rs.RsStatus;
  import com.artipie.http.rs.RsWithHeaders;
  import com.artipie.http.rs.RsWithStatus;
  import com.artipie.policy.Policy;
  import com.artipie.policy.PolicyFromYaml;
  import com.artipie.security.Authentication;
  import com.artipie.security.Policy;
  import com.artipie.security.PolicyFromYaml;
  import com.artipie.security.Session;
  import com.artipie.security.UserPrincipal;
  import java.io.IOException;
  import java.nio.charset.StandardCharsets;
  import java.util.concurrent.CompletionStage;

  public final class YamlPolicyFactory implements Slice {

    private final Policy policy;

    public YamlPolicyFactory(final Policy policy) {
      this.policy = policy;
    }

    @Override
    public CompletionStage<Response> response(
        final String line,
        final Iterable<String> headers,
        final Authentication auth,
        final Session session
    ) {
      final RequestLine request = RequestLine.valueOf(line);
      final Optional<UserPrincipal> principal = auth.principal();
      final Headers.From header = Headers.From.newFrom(headers);
      return CompletionStage.supplyAsync(
          () -> {
            try {
              return this.policy.evaluate(request, principal, header, session);
            } catch (final IOException ex) {
              throw new UncheckedIOException(ex);
            }
          }
      ).thenApply(
          res -> res.isPresent()
              ? new RsWithStatus(res.get())
              : new RsWithHeaders(
                new RsStatus(RsStatus.FORBIDDEN),
                Headers.newOne(
                    "WWW-Authenticate",
                    String.format(
                        "Basic realm=\"%s\"",
                        "Artipie"
                    )
                )
            )
      );
    }
  }
```