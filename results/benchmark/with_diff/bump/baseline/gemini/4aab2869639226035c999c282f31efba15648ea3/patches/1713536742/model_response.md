```java
import com.artipie.asto.factory.StoragesLoader;

import java.util.HashMap;
import java.util.Map;

public class Storages {

    private final StoragesLoader loader;

    public Storages() {
        this(new HashMap<>());
    }

    public Storages(Map<String, Object> env) {
        this.loader = new StoragesLoader(env);
    }

    public com.artipie.asto.Storage newStorage(String type, com.artipie.asto.factory.Config config) {
        return loader.newObject(type, config);
    }
}
```