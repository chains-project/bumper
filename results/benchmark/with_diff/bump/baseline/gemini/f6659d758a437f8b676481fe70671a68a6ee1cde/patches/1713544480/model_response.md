```java
import org.yaml.snakeyaml.Yaml;

import java.io.InputStream;
import java.util.Properties;

public class AbstractTest {

    protected Properties loadProperties(String filename) throws Exception {
        Properties properties = new Properties();
        InputStream inputStream = getClass().getResourceAsStream(filename);
        properties.load(inputStream);
        return properties;
    }

    protected Yaml createYaml() {
        return new Yaml();
    }
}
```