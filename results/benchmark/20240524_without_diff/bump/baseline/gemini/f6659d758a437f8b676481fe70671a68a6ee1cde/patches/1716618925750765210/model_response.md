```java
import org.yaml.snakeyaml.Yaml;

import java.io.File;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.InputStream;

public class AbstractTest {

    protected Yaml yaml;

    public AbstractTest() {
        yaml = new Yaml(new TrustedTagInspector());
    }

    protected Object loadYaml(String path) throws FileNotFoundException {
        File file = new File(path);
        InputStream inputStream = new FileInputStream(file);
        return yaml.load(inputStream);
    }
}
```