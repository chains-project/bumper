```java
import com.artipie.asto.factory.StoragesLoader;

public class Storages {
    public static StoragesLoader loader() {
        return new StoragesLoader();
    }
}
```