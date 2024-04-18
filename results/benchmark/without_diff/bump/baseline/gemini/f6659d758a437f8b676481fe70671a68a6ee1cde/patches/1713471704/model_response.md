```java
import org.yaml.snakeyaml.Yaml;
import org.yaml.snakeyaml.constructor.Constructor;

import java.io.InputStream;

public abstract class AbstractTest {

    protected <T> T loadYaml(String yamlPath, Class<T> clazz) {
        InputStream inputStream = this.getClass().getResourceAsStream(yamlPath);
        Yaml yaml = new Yaml(new Constructor(clazz));
        return yaml.load(inputStream);
    }
}
```