```java
import com.artipie.asto.factory.StoragesLoader;

import java.util.Map;

public class YamlPolicyFactory {

    public YamlPolicyFactory(StoragesLoader storagesLoader) {
    }

    public YamlPolicyFactory(Map<String, Object> config) {
        this(new StoragesLoader(config));
    }
}
```