```java
  import java.io.IOException;

  import com.google.common.base.Preconditions;
  import com.google.common.io.Resources;
  import com.google.common.net.HostAndPort;
  import com.google.common.net.HttpHeaders;
  import com.google.common.net.MediaType;
  import com.google.common.net.UrlEscapers;
  import java.io.UncheckedIOException;
  import java.net.HttpURLConnection;
  import java.net.URL;
  import java.nio.charset.StandardCharsets;
  import java.util.HashMap;
  import java.util.List;
  import java.util.Map;
  import java.util.Optional;
  import java.util.concurrent.CompletionStage;
  import java.util.concurrent.ExecutionException;
  import java.util.concurrent.TimeUnit;
  import java.util.concurrent.TimeoutException;
  import java.util.concurrent.atomic.AtomicBoolean;
  import java.util.function.Function;
  import org.apache.commons.lang3.StringUtils;
  import org.eclipse.jetty.http.HttpStatus;

  public class RemotePolicyLoader implements PolicyLoader {

    private final String url;

    private final String token;

    private final int timeout;

    private final AtomicBoolean loaded = new AtomicBoolean(false);

    public RemotePolicyLoader(final String url, final String token, final int timeout) {
      this.url = url;
      this.token = token;
      this.timeout = timeout;
    }

    @Override
    public CompletionStage<Policy> load() {
      return CompletableFuture.supplyAsync(() -> {
        Preconditions.checkState(!this.loaded.get(), "Policy already loaded");
        this.loaded.set(true);
        try {
          return this.loadPolicy();
        } catch (final Exception e) {
          throw new UncheckedIOException(e);
        }
      });
    }

    private Policy loadPolicy() throws Exception {
      final HttpURLConnection connection = this.openUrlConnection();
      try {
        final int status = connection.getResponseCode();
        if (status == HttpStatus.OK_200) {
          final String policy = StringUtils.toEncodedString(
              Resources.toByteArray(connection.getInputStream()),
              StandardCharsets.UTF_8
          );
          return YamlPolicyFactory.create(policy);
        } else {
          throw new RuntimeException(
              String.format(
                  "Failed to load policy from %s: %s",
                  this.url,
                  connection.getResponseMessage()
              )
          );
        }
      } finally {
        connection.disconnect();
      }
    }

    private HttpURLConnection openUrlConnection() throws Exception {
      final URL url = new URL(this.url);
      final HttpURLConnection connection = (HttpURLConnection) url.openConnection();
      connection.setConnectTimeout(this.timeout);
      connection.setReadTimeout(this.timeout);
      connection.setRequestMethod("GET");
      connection.setRequestProperty(
          HttpHeaders.AUTHORIZATION,
          String.format("Bearer %s", this.token)
      );
      return connection;
    }
  }
```