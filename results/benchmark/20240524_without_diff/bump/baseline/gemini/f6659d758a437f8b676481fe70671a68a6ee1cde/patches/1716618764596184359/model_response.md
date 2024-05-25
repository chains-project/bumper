```java
  import org.yaml.snakeyaml.Yaml;

  import java.io.IOException;
  import java.io.InputStream;
  import java.util.Map;

  public abstract class AbstractTest {

    protected Map<?, ?> loadYaml(String filename) throws IOException {
      try (InputStream in = getClass().getResourceAsStream(filename)) {
        Yaml yaml = new Yaml();
        return yaml.load(in);
      }
    }
  }
```