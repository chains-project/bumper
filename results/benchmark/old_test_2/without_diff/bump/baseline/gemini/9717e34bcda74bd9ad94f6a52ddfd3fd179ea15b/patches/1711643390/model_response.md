```java
  import com.google.common.cache.CacheBuilder;
  import com.google.common.cache.CacheLoader;
  import com.google.common.cache.LoadingCache;
  import com.google.common.collect.ImmutableMap;
  import com.jcabi.aspects.Loggable;
  import com.jcabi.aspects.Tv;
  import com.jcabi.cache.Cache;
  import com.jcabi.cache.CacheException;
  import com.jcabi.cache.GuavaCache;
  import com.jcabi.github.Commit;
  import com.jcabi.github.Issue;
  import com.jcabi.github.Releases;
  import com.jcabi.github.Repo;
  import com.jcabi.github.User;
  import com.jcabi.github.mock.MkRepo;
  import com.jcabi.github.mock.MkUser;
  import com.jcabi.http.Request;
  import com.jcabi.http.Response;
  import com.jcabi.http.response.JsonResponse;
  import com.jcabi.http.wire.Wire;
  import com.jcabi.log.Logger;
  import com.jcabi.mock.MockRequest;
  import com.jcabi.mock.StubResponse;
  import com.jcabi.xml.XML;
  import com.jcabi.xml.XMLDocument;
  import java.io.IOException;
  import java.net.URI;
  import java.net.URISyntaxException;
  import java.util.Map;
  import java.util.concurrent.ExecutionException;
  import org.hamcrest.MatcherAssert;
  import org.hamcrest.Matchers;
  import org.junit.Before;
  import org.junit.Test;
  import org.mockito.Mockito;

  @Loggable(Loggable.DEBUG)
  public class MkGithubTest {

    private final Cache cache = new GuavaCache(CacheBuilder.newBuilder().build());
    private final Wire wire = new Wire();
    private final User user = new MkUser("hub");
    private final Repo repo = new MkRepo(this.user, "jcabi-github");
    private final Map<String, String> tags = ImmutableMap.of(
        "v1.0.0", "1234567890abcdef1234567890abcdef12345678",
        "v1.0.1", "abcdef12345678901234567890abcdef12345678"
    );

    @Before
    @Tv
    public void setUp() throws CacheException, IOException, URISyntaxException {
      this.cache.put(
          "https://api.github.com/repos/hub/jcabi-github/releases",
          new StubResponse(
              200,
              new JsonResponse(
                  new XMLDocument(
                      new XML().parse(
                          "<releases>"
                              + "<release>"
                              + "<tag_name>v1.0.0</tag_name>"
                              + "<zipball_url>http://example.com/v1.0.0.zip</zipball_url>"
                              + "</release>"
                              + "<release>"
                              + "<tag_name>v1.0.1</tag_name>"
                              + "<zipball_url>http://example.com/v1.0.1.zip</zipball_url>"
                              + "</release>"
                              + "</releases>"
                      )
                  )
              )
          )
      );
      this.cache.put(
          "https://api.github.com/repos/hub/jcabi-github/commits/"
              + "1234567890abcdef1234567890abcdef12345678",
          new StubResponse(
              200,
              new JsonResponse(
                  new XMLDocument(
                      new XML().parse(
                          "<commit>"
                              + "<sha>1234567890abcdef1234567890abcdef12345678</sha>"
                              + "<message>Fix: Release info.</message>"
                              + "<author>"
                              + "<name>hub</name>"
                              + "<email>hub@example.com</email>"
                              + "</author>"
                              + "</commit>"
                      )
                  )
              )
          )
      );
      this.cache.put(
          "https://api.github.com/repos/hub/jcabi-github/commits/"
              + "abcdef12345678901234567890abcdef12345678",
          new StubResponse(
              200,
              new JsonResponse(
                  new XMLDocument(
                      new XML().parse(
                          "<commit>"
                              + "<sha>abcdef12345678901234567890abcdef12345678</sha>"
                              + "<message>Fix: Release info.</message>"
                              + "<author>"
                              + "<name>hub</name>"
                              + "<email>hub@example.com</email>"
                              + "</author>"
                              + "</commit>"
                      )
                  )
              )
          )
      );
    }

    @Test
    @Tv
    public void testReleases() throws IOException {
      final Releases releases = this.repo.releases();
      MatcherAssert.assertThat(releases.size(), Matchers.is(2));
      for (final Releases.Release release : releases) {
        MatcherAssert.assertThat(
            this.tags.get(release.name()),
            Matchers.is(release.sha())
        );
      }
    }

    @Test
    @Tv
    public void testRelease() throws IOException {
      final Releases.Release release = this.repo.releases().get(0);
      MatcherAssert.assertThat(
          release.name(),
          Matchers.is("v1.0.0")
      );
      MatcherAssert.assertThat(
          release.sha(),
          Matchers.is("1234567890abcdef1234567890abcdef12345678")
      );
      MatcherAssert.assertThat(
          release.zipball(),
          Matchers.is("http://example.com/v1.0.0.zip")
      );
      MatcherAssert.assertThat(
          release.author().login(),
          Matchers.is("hub")
      );
      MatcherAssert.assertThat(
          release.author().email(),
          Matchers.is("hub@example.com")
      );
    }

    @Test
    @Tv
    public void testReleaseCommit() throws IOException {
      final Commit commit = this.repo.releases().get(0).commit();
      MatcherAssert.assertThat(
          commit.sha(),
          Matchers.is("1234567890abcdef1234567890abcdef12345678")
      );
      MatcherAssert.assertThat(
          commit.message(),
          Matchers.is("Fix: Release info.")
      );
      MatcherAssert.assertThat(
          commit.author().login(),
          Matchers.is("hub")
      );
      MatcherAssert.assertThat(
          commit.author().email(),
          Matchers.is("hub@example.com")
      );
    }

    @Test
    @Tv
    public void testRepo() throws IOException {
      MatcherAssert.assertThat(this.repo.name(), Matchers.is("jcabi-github"));
      MatcherAssert.assertThat(this.repo.owner(), Matchers.is(this.user));
    }

    @Test
    @Tv
    public void testUser() throws IOException {
      MatcherAssert.assertThat(this.user.login(), Matchers.is("hub"));
    }

    @Test
    @Tv
    public void testIssues() throws IOException {
      final Issues issues = this.repo.issues();
      MatcherAssert.assertThat(issues.size(), Matchers.is(0));
    }

    @Test
    @Tv
    public void testIssue() throws IOException {
      final Issue issue = Mockito.mock(Issue.class);
      Mockito.when(issue.number()).thenReturn(0);
      Mockito.when(issue.title()).thenReturn("title");
      Mockito.when(issue.body()).thenReturn("body");
      Mockito.when(issue.state()).thenReturn("open");
      Mockito.when(issue.author()).thenReturn(this.user);
      Mockito.when(issue.repo()).thenReturn(this.repo);
      Mockito.when(issue.createdAt()).thenReturn(1234567890000L);
      Mockito.when(issue.updatedAt()).thenReturn(1234567890000L);
      Mockito.when(issue.closedAt()).thenReturn(null);
      Mockito.when(issue.labels()).thenReturn(null);
      Mockito.when(issue.assignees()).thenReturn(null);
      Mockito.when(issue.milestone()).thenReturn(null);
      MatcherAssert.assertThat(issue.number(), Matchers.is(0));
      MatcherAssert.assertThat(issue.title(), Matchers.is("title"));
      MatcherAssert.assertThat(issue.body(), Matchers.is("body"));
      MatcherAssert.assertThat(issue.state(), Matchers.is("open"));
      MatcherAssert.assertThat(issue.author(), Matchers.is(this.user));
      MatcherAssert.assertThat(issue.repo(), Matchers.is(this.repo));
      MatcherAssert.assertThat(issue.createdAt(), Matchers.is(1234567890000L));
      MatcherAssert.assertThat(issue.updatedAt(), Matchers.is(1234567890000L));
      MatcherAssert.assertThat(issue.closedAt(), Matchers.is(nullValue()));
      MatcherAssert.assertThat(issue.labels(), Matchers.is(nullValue()));
      MatcherAssert.assertThat(issue.assignees(), Matchers.is(nullValue()));
      MatcherAssert.assertThat(issue.milestone(), Matchers.is(nullValue()));
    }

    @Test
    @Tv
    public void testRequest() throws IOException, URISyntaxException {
      final Request request = this.wire.request(
          new URI("http://example.com/"),
          new MockRequest(
              "GET",
              new URI("http://example.com/"),
              "application/xml",
              new byte[0]
          )
      );
      MatcherAssert.assertThat(request.method(), Matchers.is("GET"));
      MatcherAssert.assertThat(request.uri(), Matchers.is(new URI("http://example.com/")));
      MatcherAssert.assertThat(request.accept(), Matchers.is("application/xml"));
      MatcherAssert.assertThat(request.body(), Matchers.is(new byte[0]));
      MatcherAssert.assertThat(
          request.header("Content-Type"),
          Matchers.is("application/xml")
      );
    }

    @Test
    @Tv
    public void testResponse() throws IOException {
      final Response response = this.wire.response(
          new StubResponse(
              200,
              new JsonResponse(
                  new XMLDocument(
                      new XML().parse(
                          "<response>OK</response>"
                      )
                  )
              )
          )
      );
      MatcherAssert.assertThat(response.status(), Matchers.is(200));
      MatcherAssert.assertThat(
          response.body(),
          Matchers.is(
              "<response>OK</response>"
          )
      );
      MatcherAssert.assertThat(
          response.header("Content-Type"),
          Matchers.is("application/json")
      );
    }

    @Test
    @Tv
    public void testCache() throws CacheException, ExecutionException {
      final LoadingCache<String, Response> cache = new GuavaCache(
          CacheBuilder.newBuilder().build(),
          new CacheLoader<String, Response>() {
            @Override
            public Response load(String key) throws Exception {
              return new StubResponse(200, new JsonResponse(new XMLDocument(new XML().parse("<response>OK</response>"))));
            }
          }
      );
      MatcherAssert.assertThat(
          cache.get("http://example.com/"),
          Matchers.is(
              new StubResponse(200, new JsonResponse(new XMLDocument(new XML().parse("<response>OK</response>"))))
          )
      );
    }

    @Test
    @Tv
    public void testXml() throws IOException {
      final XMLDocument doc = new XML().parse("<response>OK</response>");
      MatcherAssert.assertThat(
          doc.text(),
          Matchers.is("OK")
      );
    }

  }
```