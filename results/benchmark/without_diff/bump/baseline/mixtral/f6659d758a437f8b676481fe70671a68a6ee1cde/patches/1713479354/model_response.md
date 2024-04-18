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

In this patch, we create a new `Yaml` instance and set the `TrustedTagInspector` manually. This way, we avoid the need to import `TrustedTagInspector` directly.

Note that this patch assumes that the `createYaml()` method is not overriding any method in the new version. If it is, you may need to modify the patch accordingly.