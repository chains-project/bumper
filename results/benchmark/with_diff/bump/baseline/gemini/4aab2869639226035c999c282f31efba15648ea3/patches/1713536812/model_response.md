```java
import com.artipie.asto.factory.StoragesLoader;

import java.util.Map;

public class YamlPolicyFactory {

    private final StoragesLoader storages;

    public YamlPolicyFactory(Map<String, Object> config) {
        this.storages = new StoragesLoader(config);
    }

    // ... rest of the class code
}
```