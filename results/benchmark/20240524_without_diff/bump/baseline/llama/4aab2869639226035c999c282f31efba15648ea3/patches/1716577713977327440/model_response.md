```java
import java.util.ServiceLoader;

import com.artipie.asto.Artipie;
import com.artipie.asto.factory.StoragesFactory;

public class YamlPolicyFactory {
    public YamlPolicyFactory() {
        ServiceLoader<StoragesFactory> loader = ServiceLoader.load(StoragesFactory.class);
        StoragesFactory factory = loader.findFirst().get();
        factory.getStorages();
    }
}
```