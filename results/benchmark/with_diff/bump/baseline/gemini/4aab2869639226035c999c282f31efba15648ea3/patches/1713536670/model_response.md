```java
import com.artipie.asto.factory.StoragesLoader;

import java.util.Map;

public class Storages {

    private final StoragesLoader loader;

    public Storages() {
        this(Map.of());
    }

    public Storages(Map<String, Object> config) {
        this.loader = new StoragesLoader(config);
    }

    public com.artipie.asto.Storage newStorage(String type, com.artipie.asto.factory.Config config) {
        return loader.newObject(type, config);
    }
}
```