```java
  import org.yaml.snakeyaml.constructor.Constructor;
  import org.yaml.snakeyaml.DumperOptions;
  import org.yaml.snakeyaml.LoaderOptions;
  import org.yaml.snakeyaml.Yaml;
  import org.yaml.snakeyaml.nodes.Tag;
  import org.yaml.snakeyaml.representer.Representer;

  import java.util.Map;
  import java.util.Set;

  import static org.junit.Assert.assertEquals;

  public abstract class AbstractTest {
    protected void assertYamlEquals(String expected, String actual) {
      Yaml yaml = new Yaml();
      Map actualMap = (Map) yaml.load(actual);
      Map expectedMap = (Map) yaml.load(expected);
      assertEquals(expectedMap, actualMap);
    }

    protected void assertYamlEquals(String expected, Object actual) {
      Yaml yaml = new Yaml();
      Map actualMap = (Map) yaml.load(yaml.dump(actual));
      Map expectedMap = (Map) yaml.load(expected);
      assertEquals(expectedMap, actualMap);
    }

    protected void assertYamlEquals(Object expected, String actual) {
      Yaml yaml = new Yaml();
      Map expectedMap = (Map) yaml.load(yaml.dump(expected));
      Map actualMap = (Map) yaml.load(actual);
      assertEquals(expectedMap, actualMap);
    }

    protected void assertYamlEquals(Object expected, Object actual) {
      Yaml yaml = new Yaml();
      Map expectedMap = (Map) yaml.load(yaml.dump(expected));
      Map actualMap = (Map) yaml.load(yaml.dump(actual));
      assertEquals(expectedMap, actualMap);
    }

    protected void assertYamlEquals(String expected, String actual, Set<Tag> tags) {
      Yaml yaml = new Yaml(new Constructor(tags), new Representer(), new DumperOptions(), new LoaderOptions(),
          new TrustedTagInspector(tags));
      Map actualMap = (Map) yaml.load(actual);
      Map expectedMap = (Map) yaml.load(expected);
      assertEquals(expectedMap, actualMap);
    }

    protected void assertYamlEquals(String expected, Object actual, Set<Tag> tags) {
      Yaml yaml = new Yaml(new Constructor(tags), new Representer(), new DumperOptions(), new LoaderOptions(),
          new TrustedTagInspector(tags));
      Map actualMap = (Map) yaml.load(yaml.dump(actual));
      Map expectedMap = (Map) yaml.load(expected);
      assertEquals(expectedMap, actualMap);
    }

    protected void assertYamlEquals(Object expected, String actual, Set<Tag> tags) {
      Yaml yaml = new Yaml(new Constructor(tags), new Representer(), new DumperOptions(), new LoaderOptions(),
          new TrustedTagInspector(tags));
      Map expectedMap = (Map) yaml.load(yaml.dump(expected));
      Map actualMap = (Map) yaml.load(actual);
      assertEquals(expectedMap, actualMap);
    }

    protected void assertYamlEquals(Object expected, Object actual, Set<Tag> tags) {
      Yaml yaml = new Yaml(new Constructor(tags), new Representer(), new DumperOptions(), new LoaderOptions(),
          new TrustedTagInspector(tags));
      Map expectedMap = (Map) yaml.load(yaml.dump(expected));
      Map actualMap = (Map) yaml.load(yaml.dump(actual));
      assertEquals(expectedMap, actualMap);
    }
  }
```