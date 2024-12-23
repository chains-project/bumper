```java
  import com.google.common.base.Preconditions;
  import com.google.common.io.ByteStreams;
  import com.google.common.io.Resources;
  import java.io.IOException;
  import java.io.InputStream;
  import java.net.URL;
  import java.util.Properties;

  /**
   * Yaml policy factory.
   *
   * @since 1.7
   */
  public class YamlPolicyFactory {

    private final URL url;

    /**
     * Ctor.
     *
     * @param url Policy URL
     */
    public YamlPolicyFactory(final URL url) {
      this.url = Preconditions.checkNotNull(url);
    }

    /**
     * Create policy.
     *
     * @return Policy
     * @throws IOException In case of IO errors
     */
    public Policy create() throws IOException {
      try (InputStream stream = Resources.asByteSource(this.url).openStream()) {
        final Properties props = new Properties();
        props.load(stream);
        return new YamlPolicy(props);
      }
    }
  }
```