```java
import java.io.UncheckedIOException;
import org.yaml.snakeyaml.Yaml;

class YamlPolicyFactory {
    private final Yaml yaml;

    public YamlPolicyFactory() {
        this.yaml = new Yaml();
    }

    public Policy read(String policy) {
        try {
            return this.yaml.loadAs(policy, Policy.class);
        } catch (Exception ex) {
            throw new UncheckedIOException(ex);
        }
    }
}
```