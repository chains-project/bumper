```java
  import com.jcabi.aspects.Tv;
  import com.jcabi.log.Logger;
  import org.kohsuke.github.GitHub;

  public class MkGithub extends GitHub {
    public MkGithub(String user, String password) {
      super(user, password);
      Logger.debug(this, "Mock GitHub created with user '%s'", user);
    }

    public MkGithub(String user, String password, String host) {
      super(user, password, host);
      Logger.debug(this, "Mock GitHub created with user '%s' at '%s'", user, host);
    }

    public MkGithub(String user, String password, String host, String oauthToken) {
      super(user, password, host, oauthToken);
      Logger.debug(this, "Mock GitHub created with user '%s' at '%s'", user, host);
    }

    public MkGithub(String user, String password, String host, String oauthToken, String requestMethod) {
      super(user, password, host, oauthToken, requestMethod);
      Logger.debug(this, "Mock GitHub created with user '%s' at '%s'", user, host);
    }

    public MkGithub(String user, String password, String host, String oauthToken, String requestMethod, String proxyHost, int proxyPort) {
      super(user, password, host, oauthToken, requestMethod, proxyHost, proxyPort);
      Logger.debug(this, "Mock GitHub created with user '%s' at '%s'", user, host);
    }

    public MkGithub(String user, String password, String host, String oauthToken, String requestMethod, String proxyHost, int proxyPort, String proxyUser, String proxyPassword) {
      super(user, password, host, oauthToken, requestMethod, proxyHost, proxyPort, proxyUser, proxyPassword);
      Logger.debug(this, "Mock GitHub created with user '%s' at '%s'", user, host);
    }

    public MkGithub(String oauthToken) {
      super(oauthToken);
      Logger.debug(this, "Mock GitHub created with oauth token");
    }

    public MkGithub(String oauthToken, String requestMethod) {
      super(oauthToken, requestMethod);
      Logger.debug(this, "Mock GitHub created with oauth token");
    }

    public MkGithub(String oauthToken, String requestMethod, String proxyHost, int proxyPort) {
      super(oauthToken, requestMethod, proxyHost, proxyPort);
      Logger.debug(this, "Mock GitHub created with oauth token");
    }

    public MkGithub(String oauthToken, String requestMethod, String proxyHost, int proxyPort, String proxyUser, String proxyPassword) {
      super(oauthToken, requestMethod, proxyHost, proxyPort, proxyUser, proxyPassword);
      Logger.debug(this, "Mock GitHub created with oauth token");
    }

    public MkGithub(String oauthToken, String host, String requestMethod) {
      super(oauthToken, host, requestMethod);
      Logger.debug(this, "Mock GitHub created with oauth token at '%s'", host);
    }

    public MkGithub(String oauthToken, String host, String requestMethod, String proxyHost, int proxyPort) {
      super(oauthToken, host, requestMethod, proxyHost, proxyPort);
      Logger.debug(this, "Mock GitHub created with oauth token at '%s'", host);
    }

    public MkGithub(String oauthToken, String host, String requestMethod, String proxyHost, int proxyPort, String proxyUser, String proxyPassword) {
      super(oauthToken, host, requestMethod, proxyHost, proxyPort, proxyUser, proxyPassword);
      Logger.debug(this, "Mock GitHub created with oauth token at '%s'", host);
    }

    public MkGithub(GitHubBuilder builder) {
      super(builder);
      Logger.debug(this, "Mock GitHub created with builder");
    }

    public MkGithub(GitHubBuilder builder, String oauthToken) {
      super(builder, oauthToken);
      Logger.debug(this, "Mock GitHub created with builder and oauth token");
    }

    public MkGithub(GitHubBuilder builder, String oauthToken, String requestMethod) {
      super(builder, oauthToken, requestMethod);
      Logger.debug(this, "Mock GitHub created with builder and oauth token");
    }

    public MkGithub(GitHubBuilder builder, String oauthToken, String requestMethod, String proxyHost, int proxyPort) {
      super(builder, oauthToken, requestMethod, proxyHost, proxyPort);
      Logger.debug(this, "Mock GitHub created with builder and oauth token");
    }

    public MkGithub(GitHubBuilder builder, String oauthToken, String requestMethod, String proxyHost, int proxyPort, String proxyUser, String proxyPassword) {
      super(builder, oauthToken, requestMethod, proxyHost, proxyPort, proxyUser, proxyPassword);
      Logger.debug(this, "Mock GitHub created with builder and oauth token");
    }

    public MkGithub(GitHubBuilder builder, String oauthToken, String host, String requestMethod) {
      super(builder, oauthToken, host, requestMethod);
      Logger.debug(this, "Mock GitHub created with builder and oauth token at '%s'", host);
    }

    public MkGithub(GitHubBuilder builder, String oauthToken, String host, String requestMethod, String proxyHost, int proxyPort) {
      super(builder, oauthToken, host, requestMethod, proxyHost, proxyPort);
      Logger.debug(this, "Mock GitHub created with builder and oauth token at '%s'", host);
    }

    public MkGithub(GitHubBuilder builder, String oauthToken, String host, String requestMethod, String proxyHost, int proxyPort, String proxyUser, String proxyPassword) {
      super(builder, oauthToken, host, requestMethod, proxyHost, proxyPort, proxyUser, proxyPassword);
      Logger.debug(this, "Mock GitHub created with builder and oauth token at '%s'", host);
    }

    public Tv tv() {
      return this.createMock(Tv.class);
    }
  }
```