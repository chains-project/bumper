```java
import com.artipie.asto.factory.StoragesLoader;

import java.util.Map;

public class MyStorages extends StoragesLoader {

    private final Map<String, Config> configs;

    public MyStorages(Map<String, Config> configs) {
        this.configs = configs;
    }

    @Override
    public com.artipie.asto.Storage newObject(String name, Config config) {
        return switch (name) {
            case "file" -> new com.artipie.asto.fs.FileStorageFactory().newStorage(config);
            case "etcd" -> new com.artipie.asto.etcd.EtcdStorageFactory().newStorage(config);
            case "s3" -> new com.artipie.asto.s3.S3StorageFactory().newStorage(config);
            default -> throw new IllegalArgumentException("Unknown storage type: " + name);
        };
    }
}
```