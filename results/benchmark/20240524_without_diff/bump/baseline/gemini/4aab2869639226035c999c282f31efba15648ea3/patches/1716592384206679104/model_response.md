```java
import java.io.IOException;
import java.io.UncheckedIOException;

public class YamlPolicyFactory {
    public static Policy policy(String yaml) {
        try {
            return Policy.from(new Yaml(yaml).loadAs(Map.class));
        } catch (IOException e) {
            throw new UncheckedIOException(e);
        }
    }
}
```