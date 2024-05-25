```java
import org.yaml.snakeyaml.Yaml;

import java.io.InputStream;

public class AbstractTest {

    private static final Yaml YAML = new Yaml(new TrustedTagInspector());

    public Object loadYaml(String resourceName) {
        try (InputStream in = getClass().getResourceAsStream(resourceName)) {
            return YAML.load(in);
        } catch (Exception e) {
            throw new RuntimeException(e);
        }
    }
}
```