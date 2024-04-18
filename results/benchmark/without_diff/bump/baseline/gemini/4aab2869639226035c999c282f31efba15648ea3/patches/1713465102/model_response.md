```java
import com.artipie.asto.factory.Storages;
import com.artipie.asto.fs.Storage;

public class YamlPolicyFactory {

    private final Storage storage;

    public YamlPolicyFactory(Storage storage) {
        this.storage = storage;
    }

    public YamlPolicyFactory() {
        this(Storages.named("yaml-policy"));
    }
}
```