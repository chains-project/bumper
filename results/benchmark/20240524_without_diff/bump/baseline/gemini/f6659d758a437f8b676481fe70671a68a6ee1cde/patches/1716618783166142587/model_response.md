```java
import org.yaml.snakeyaml.Yaml;
import org.yaml.snakeyaml.constructor.Constructor;

import java.io.File;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.InputStream;

public abstract class AbstractTest {

    protected Object loadYaml(String yamlFile) throws FileNotFoundException {
        InputStream in = new FileInputStream(new File(yamlFile));
        Yaml yaml = new Yaml(new Constructor(Object.class));
        return yaml.load(in);
    }

}
```