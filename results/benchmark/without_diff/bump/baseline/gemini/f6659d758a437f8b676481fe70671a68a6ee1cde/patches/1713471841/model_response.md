```java
  import org.yaml.snakeyaml.Yaml;
  import org.yaml.snakeyaml.constructor.Constructor;
  import org.yaml.snakeyaml.representer.Representer;

  import java.util.Map;

  public class AbstractTest {

    protected <T> T loadYaml(String yaml, Class<T> clazz) {
      Yaml yamlParser = new Yaml(new Constructor(clazz), new Representer(), new TrustedTagInspector(), null, null);
      return yamlParser.load(yaml);
    }

    protected Map<String, Object> loadYaml(String yaml) {
      Yaml yamlParser = new Yaml(new Representer(), new TrustedTagInspector(), null, null);
      return (Map<String, Object>) yamlParser.load(yaml);
    }
  }
```