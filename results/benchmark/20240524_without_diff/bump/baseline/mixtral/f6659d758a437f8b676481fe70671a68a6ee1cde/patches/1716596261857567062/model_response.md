Here's the proposed patch to fix the error:

```java
import org.yaml.snakeyaml.Yaml;

// ...

protected Yaml createYaml() {
    Yaml yaml = new Yaml(new TrustedTagInspector());
    // ...
    return yaml;
}
```

This patch creates a `Yaml` instance with a `TrustedTagInspector` and returns it. It should work as a replacement for the failing method.