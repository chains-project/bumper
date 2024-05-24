```java
import com.artipie.asto.factory.StoragesLoader;

import java.util.Map;

public class YamlPolicyFactory {

    public YamlPolicyFactory(Map<String, Object> config) {
        StoragesLoader storagesLoader = new StoragesLoader(config);
    }
}
```