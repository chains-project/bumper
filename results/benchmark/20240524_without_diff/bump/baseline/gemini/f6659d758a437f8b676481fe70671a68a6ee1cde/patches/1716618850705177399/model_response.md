```java
  import org.yaml.snakeyaml.Yaml;
  import org.yaml.snakeyaml.constructor.Constructor;

  import java.io.InputStream;
  import java.util.Map;

  public abstract class AbstractTest {

      protected Map<String, Object> loadYaml(String resourceName) {
          InputStream in = getClass().getResourceAsStream(resourceName);
          Yaml yaml = new Yaml(new Constructor(Map.class));
          return yaml.load(in);
      }
  }
```