```java
import org.yaml.snakeyaml.Yaml;
import org.yaml.snakeyaml.constructor.Constructor;

public class AbstractTest {
    protected Yaml yaml = new Yaml(new Constructor(Object.class), new TrustedTagInspector());
}
```