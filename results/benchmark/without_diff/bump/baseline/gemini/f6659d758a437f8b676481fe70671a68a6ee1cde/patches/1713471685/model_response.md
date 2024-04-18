```java
import org.yaml.snakeyaml.Yaml;

public class AbstractTest {

    protected static final Yaml YAML = new Yaml(new TrustedTagInspector());

}
```