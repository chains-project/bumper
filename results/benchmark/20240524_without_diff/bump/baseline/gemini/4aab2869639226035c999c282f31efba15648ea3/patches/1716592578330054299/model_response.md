```java
import java.io.UncheckedIOException;
import java.util.Optional;

public class YamlPolicyFactory {

    private final Yaml yaml;

    public YamlPolicyFactory(Yaml yaml) {
        this.yaml = yaml;
    }

    public Optional<Policy> policy(String name) {
        try {
            return Optional.ofNullable(this.yaml.loadAs(this.yaml.newStream(name, YamlPolicyFactory.class.getResourceAsStream(name)), Policy.class));
        } catch (UncheckedIOException ex) {
            return Optional.empty();
        }
    }
}
```