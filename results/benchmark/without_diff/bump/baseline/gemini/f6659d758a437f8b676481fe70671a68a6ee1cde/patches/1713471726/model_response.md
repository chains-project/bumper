```java
import org.yaml.snakeyaml.Yaml;

public class AbstractTest {

    protected Yaml yaml = new Yaml(new TrustedTagInspector());

    // ... rest of the class code
}
```