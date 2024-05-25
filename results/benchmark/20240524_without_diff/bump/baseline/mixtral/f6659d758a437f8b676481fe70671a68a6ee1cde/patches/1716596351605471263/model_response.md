Here's a possible patch for the failing code:

```java
import org.yaml.snakeyaml.Yaml;

// ...

protected void setupYaml() {
    Yaml yaml = new Yaml(new TrustedTagInspector());
    // ...
}
```

This patch creates a `Yaml` instance with a `TrustedTagInspector` instance. This way, you can still use the `TrustedTagInspector` class, even if it's not directly imported.