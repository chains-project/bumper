```java
import org.yaml.snakeyaml.Yaml;

public abstract class AbstractTest {

    protected static final Yaml YAML = new Yaml(new TrustedTagInspector());

    // ...
}
```