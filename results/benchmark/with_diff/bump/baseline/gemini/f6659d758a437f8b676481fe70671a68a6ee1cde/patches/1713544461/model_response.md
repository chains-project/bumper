```java
  import org.yaml.snakeyaml.DumperOptions;
  import org.yaml.snakeyaml.Yaml;
  import org.yaml.snakeyaml.constructor.SafeConstructor;
  import org.yaml.snakeyaml.nodes.Tag;

  public class TrustedTagInspector {

    private final DumperOptions options;

    public TrustedTagInspector() {
      this.options = new DumperOptions();
      this.options.setAllowUnicode(true);
      this.options.setDefaultFlowStyle(DumperOptions.FlowStyle.BLOCK);
    }

    public boolean isGlobalTagAllowed(Tag tag) {
      return this.options.getAllowUnicode() && tag.startsWith("!");
    }
  }
```