```java
import com.artipie.asto.factory.StorageConfig;
import com.artipie.asto.factory.StoragesLoader;

public class FixedCode {
    public static void main(String[] args) {
        StoragesLoader storagesLoader = new StoragesLoader();
        StorageConfig storageConfig = new StorageConfig();
        storagesLoader.newObject("file", storageConfig);
    }
}
```