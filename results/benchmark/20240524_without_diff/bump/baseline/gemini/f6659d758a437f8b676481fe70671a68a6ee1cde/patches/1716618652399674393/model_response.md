```java
import org.yaml.snakeyaml.Yaml;

import java.io.InputStream;
import java.util.Map;

public class AbstractTest {

    public static Map<String, Object> loadYaml(String yamlPath) {
        try (InputStream inputStream = AbstractTest.class.getResourceAsStream(yamlPath)) {
            Yaml yaml = new Yaml();
            return yaml.load(inputStream);
        } catch (Exception e) {
            throw new RuntimeException(e);
        }
    }
}
```