```java
import com.artipie.asto.Artipie;
import com.artipie.asto.factory.StoragesFactory;

public class YamlPolicyFactory {
    public YamlPolicyFactory() {
        StoragesFactory storagesFactory = Artipie.newAsto();
    }
}
```