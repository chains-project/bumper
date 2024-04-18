```java
import org.yaml.snakeyaml.Yaml;

import java.io.InputStream;
import java.util.Map;

public abstract class AbstractTest {

    protected Map<String, Object> loadYaml(String path) throws Exception {
        InputStream is = getClass().getResourceAsStream(path);
        Yaml yaml = new Yaml(new TrustedTagInspector());
        return (Map<String, Object>) yaml.load(is);
    }
}
```