Here's a possible patch to fix the error:

```java
import org.yaml.snakeyaml.Yaml;

// ...

protected TrustedTagInspector createTagInspector() {
    return new Yaml(createTagResolver()).getInspector();
}
```

In this patch, we're using the `Yaml` class to create a new `TrustedTagInspector` instance. The `Yaml` class provides a `getInspector()` method that returns a `TagInspector` instance. Since `TrustedTagInspector` is a subclass of `TagInspector`, we can use it to create a `TrustedTagInspector` instance.

Note that this patch assumes that the `createTagResolver()` method is still available in the new version of the library. If that method is no longer available, you may need to modify this patch accordingly.