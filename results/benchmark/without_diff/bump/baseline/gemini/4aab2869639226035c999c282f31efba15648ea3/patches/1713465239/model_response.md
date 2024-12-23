```java
  import java.io.UncheckedIOException;
  import java.nio.file.Path;
  import java.util.Map;
  import com.artipie.asto.Content;
  import com.artipie.asto.Key;
  import com.artipie.asto.Storage;
  import com.artipie.asto.ext.ContentFrom;
  import com.artipie.asto.ext.KeyFrom;
  import com.artipie.http.Headers;
  import com.artipie.http.Response;
  import com.artipie.http.Slice;
  import com.artipie.http.async.AsyncResponse;
  import com.artipie.http.rs.RsWithBody;
  import com.artipie.http.rs.RsWithHeaders;
  import com.artipie.http.rs.StandardRs;
  import com.artipie.security.Authentication;
  import com.artipie.security.Policy;
  import com.artipie.security.policy.YamlPolicyFactory;
  import com.artipie.security.session.AuthenticationKey;
  import com.artipie.security.session.AuthenticationSession;
  import com.artipie.security.session.Session;
  import com.artipie.security.session.SessionCookie;
  import com.artipie.security.session.SessionManager;
  import com.artipie.security.session.SimpleAuthentication;
  import com.artipie.security.session.Token;
  import com.google.common.collect.ImmutableList;
  import com.google.common.collect.ImmutableMap;
  import com.google.common.collect.ImmutableSet;

  public final class YamlPolicyFactoryTest implements Slice {

    private final Storage storage;
    private final Policy policy;
    private final SessionManager sessionManager;

    public YamlPolicyFactoryTest(final Storage storage, final Policy policy, final SessionManager sessionManager) {
      this.storage = storage;
      this.policy = policy;
      this.sessionManager = sessionManager;
    }

    @Override
    public Response response(
        final String line,
        final Headers headers,
        final Authentication authentication
    ) {
      final Token token = new Token(authentication.name());
      final Session session = new AuthenticationSession(token, new SimpleAuthentication(token));
      final SessionCookie cookie = new SessionCookie(this.sessionManager, session);
      final Path path = new KeyFrom(line).asPath();
      final Content content = new ContentFrom(this.storage, new Key(path));
      return new AsyncResponse(
          new RsWithHeaders(
              new RsWithBody(
                  new StandardRs(
                      Response.StatusCode.OK,
                      ImmutableMap.of("Content-Type", "text/plain"),
                      content
                  ),
                  headers.with(cookie)
              ),
              new Headers.From(
                  ImmutableMap.of(
                      "Content-Disposition",
                      String.format("attachment; filename=\"%s\"", path.getFileName())
                  )
              )
          )
      ).activate();
    }

    public static void main(final String[] args) throws Exception {
      final Storage storage = new Storage.Mem();
      final Policy policy = new YamlPolicyFactory(
          new ContentFrom(storage, new Key("policy.yaml"))
      ).create();
      final SessionManager sessionManager = new SessionManager(
          storage,
          "session",
          new AuthenticationKey(),
          new Token.Generator()
      );
      final YamlPolicyFactoryTest policyFactoryTest = new YamlPolicyFactoryTest(
          storage,
          policy,
          sessionManager
      );
      final Slice slice = new Slice.Wrap(policyFactoryTest, policy);
      final Slice auth = new Slice.Wrap(slice, new Authentication.Noop());
      auth.response("GET /", new Headers.From(ImmutableMap.of()), new Authentication.None()).send(System.out);
    }
  }
```