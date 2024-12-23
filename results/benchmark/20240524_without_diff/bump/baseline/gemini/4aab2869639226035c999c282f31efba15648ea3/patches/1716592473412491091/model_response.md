```java
  import java.io.UncheckedIOException;
  import java.io.IOException;

  import com.artipie.asto.Content;
  import com.artipie.asto.Key;
  import com.artipie.asto.Storage;
  import com.artipie.http.Headers;
  import com.artipie.http.Response;
  import com.artipie.http.Slice;
  import com.artipie.http.async.AsyncResponse;
  import com.artipie.http.rs.RsStatus;
  import com.artipie.http.rs.StandardRs;
  import com.artipie.policy.Policy;
  import com.artipie.policy.PolicyList;
  import com.artipie.policy.RepoPolicy;
  import com.artipie.security.PolicyFactory;
  import com.artipie.security.Session;
  import com.artipie.security.auth.Authentication;
  import com.artipie.security.auth.DefaultSession;
  import com.artipie.security.auth.UserPrincipal;
  import com.artipie.settings.AuthSettings;
  import com.artipie.settings.RepoSettings;
  import com.artipie.settings.StorageSettings;
  import com.artipie.vertx.VertxSliceServer;
  import com.google.common.collect.ImmutableList;
  import io.vertx.core.Handler;
  import io.vertx.core.http.HttpServerResponse;
  import java.nio.charset.StandardCharsets;
  import java.util.Optional;
  import java.util.concurrent.CompletableFuture;
  import java.util.concurrent.CompletionStage;
  import java.util.concurrent.Executor;
  import java.util.concurrent.Executors;
  import java.util.function.Function;

  import static com.artipie.http.Headers.COOKIE;
  import static com.artipie.http.headers.Header.Authorization;
  import static com.artipie.http.headers.Header.WWW_AUTHENTICATE;
  import static com.artipie.http.headers.WWWAuthenticate.Type.BASIC;
  import static com.artipie.http.rs.RsStatus.UNAUTHORIZED;
  import static java.util.concurrent.CompletableFuture.completedFuture;

  public class YamlPolicyFactory implements PolicyFactory {

    private static final String POLICY_PATH = "/policy.yaml";

    private final StorageSettings storageSettings;

    private final AuthSettings authSettings;

    private final RepoSettings repoSettings;

    private final Executor executor;

    public YamlPolicyFactory(
        final StorageSettings storageSettings,
        final AuthSettings authSettings,
        final RepoSettings repoSettings
    ) {
      this(storageSettings, authSettings, repoSettings, Executors.newCachedThreadPool());
    }

    public YamlPolicyFactory(
        final StorageSettings storageSettings,
        final AuthSettings authSettings,
        final RepoSettings repoSettings,
        final Executor executor
    ) {
      this.storageSettings = storageSettings;
      this.authSettings = authSettings;
      this.repoSettings = repoSettings;
      this.executor = executor;
    }

    @Override
    public Slice asSlice(final Slice origin) {
      return new YamlPolicyFactory.AuthSlice(
          this.storageSettings.storage(),
          this.authSettings.slice(),
          origin,
          this.executor
      );
    }

    private static class AuthSlice implements Slice {

      private final Storage storage;

      private final Slice origin;

      private final Slice auth;

      private final Executor executor;

      AuthSlice(
          final Storage storage,
          final Slice auth,
          final Slice origin,
          final Executor executor
      ) {
        this.storage = storage;
        this.auth = auth;
        this.origin = origin;
        this.executor = executor;
      }

      @Override
      public Response response(
          final String line,
          final Headers headers,
          final Function<Slice, CompletionStage<Response>> next
      ) {
        final Optional<UserPrincipal> principal = this.principal(headers);
        return principal.isPresent()
            ? next.apply(this.origin)
            : this.auth.response(line, headers, next);
      }

      private Optional<UserPrincipal> principal(final Headers headers) {
        return headers.value(WWW_AUTHENTICATE)
            .filter(BASIC::equals)
            .flatMap(auth -> headers.value(Authorization))
            .map(auth -> auth.substring(BASIC.toString().length()).trim())
            .map(UserPrincipal::new);
      }

      private CompletionStage<Policy> policy(final UserPrincipal principal) {
        return this.storage.value(new Key.From(YamlPolicyFactory.POLICY_PATH))
            .thenApply(Content::as(String.class, StandardCharsets.UTF_8))
            .thenApply(YamlPolicyFactory::parse)
            .thenApply(policies -> policies.find(principal));
      }
    }

    private static PolicyList parse(final String content) {
      return new PolicyList(
          ImmutableList.copyOf(
              YamlPolicyFactory.PoliciesParser.parse(content)
          )
      );
    }

    private static class PoliciesParser {

      private static final String REPO_PREFIX = "repo:";

      static Iterable<Policy> parse(final String content) {
        return YamlParser.parse(content)
            .stream()
            .map(PoliciesParser::parse)
            .flatMap(Optional::stream)
            .collect(ImmutableList.toImmutableList());
      }

      static Optional<Policy> parse(final Map.Entry<String, Object> entry) {
        if (entry.getKey().startsWith(PoliciesParser.REPO_PREFIX)) {
          final String repo = entry.getKey().substring(PoliciesParser.REPO_PREFIX.length());
          return Optional.of(new RepoPolicy(repo, PoliciesParser.parse(entry.getValue())));
        }
        return Optional.empty();
      }

      private static Policy parse(final Object value) {
        if (value instanceof String) {
          return new Policy.Simple(value.toString());
        } else if (value instanceof List) {
          return new PolicyList(
              ImmutableList.copyOf(
                  ((List<?>) value).stream()
                      .map(PoliciesParser::parse)
                      .flatMap(Optional::stream)
                      .iterator()
              )
          );
        }
        throw new IllegalArgumentException(
            String.format(
                "Unsupported policy value `%s` of type `%s`",
                value,
                value.getClass().getSimpleName()
            )
        );
      }
    }
  }
```