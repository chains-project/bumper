Here's a possible patch for the failing code:

```java
import org.yaml.snakeyaml.Yaml;

// ...

protected Yaml createYaml() {
    Yaml yaml = new Yaml();
    TrustedTagInspector trustedTagInspector = new TrustedTagInspector();
    yaml.setTag(trustedTagInspector);
    return yaml;
}
```

This patch creates a `Yaml` instance and sets a `TrustedTagInspector` to it, which should resolve the missing symbol error. Note that I'm assuming the `createYaml` method is the one causing the error. If it's not, please replace the method name accordingly.