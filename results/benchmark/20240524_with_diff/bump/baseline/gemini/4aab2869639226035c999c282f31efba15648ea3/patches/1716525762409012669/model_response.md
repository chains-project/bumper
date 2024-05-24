```java
import com.artipie.asto.factory.StoragesLoader;

import java.util.Map;

public class Storages {

    private final StoragesLoader storagesLoader;

    public Storages() {
        this(Map.of());
    }

    public Storages(Map<String, String> env) {
        this.storagesLoader = new StoragesLoader(env);
    }

    public com.artipie.asto.Storage newStorage(String type, com.artipie.asto.factory.Config config) {
        return this.storagesLoader.newObject(type, config);
    }

    public java.util.Set<String> types() {
        return this.storagesLoader.types();
    }
}
```