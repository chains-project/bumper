```java
import org.yaml.snakeyaml.Yaml;

import java.io.File;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.util.Map;

public class AbstractTest {
    protected Map<String, Object> loadYaml(String path) throws FileNotFoundException {
        Yaml yaml = new Yaml(new TrustedTagInspector());
        File file = new File(path);
        try (FileInputStream fis = new FileInputStream(file)) {
            return yaml.load(fis);
        } catch (IOException e) {
            throw new RuntimeException(e);
        }
    }
}
```