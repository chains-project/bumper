```java
import java.util.ServiceLoader;

import com.artipie.asto.factory.StoragesFactory;

public class YamlPolicyFactory {
    public YamlPolicyFactory() {
        ServiceLoader<StoragesFactory> loader = ServiceLoader.load(StoragesFactory.class);
        StoragesFactory storagesFactory = loader.findFirst().get();
        // Use storagesFactory instead of Storages
    }
}
```