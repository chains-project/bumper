```java
import org.yaml.snakeyaml.DumperOptions;
import org.yaml.snakeyaml.Yaml;

import java.util.HashMap;
import java.util.Map;

public class AbstractTest {

    protected static final Yaml yaml = new Yaml(new DumperOptions()
            .setAllowReadOnlyProperties(true)
            .setAllowDuplicateKeys(false)
            .setDefaultFlowStyle(DumperOptions.FlowStyle.BLOCK));

    protected static final Map<String, Object> emptyMap = new HashMap<>();
}
```