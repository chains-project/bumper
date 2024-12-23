```java
import org.yaml.snakeyaml.DumperOptions;
import org.yaml.snakeyaml.Yaml;
import org.yaml.snakeyaml.constructor.SafeConstructor;
import org.yaml.snakeyaml.nodes.Tag;
import org.yaml.snakeyaml.representer.Representer;

import java.util.LinkedHashMap;
import java.util.Map;

public abstract class AbstractTest {

    protected Yaml yaml;

    public AbstractTest() {
        yaml = new Yaml(new SafeConstructor(), new Representer(), new DumperOptions(), new TrustedTagInspector());
    }

    protected Map<String, Object> yamlToMap(String yamlString) {
        Map<String, Object> map = new LinkedHashMap<>();
        yaml.loadAll(yamlString).forEach(node -> {
            map.putAll((Map<String, Object>) node);
        });
        return map;
    }
}
```