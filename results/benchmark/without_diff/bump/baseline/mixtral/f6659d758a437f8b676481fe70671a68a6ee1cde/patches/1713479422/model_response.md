Here's a possible patch that you can apply to the code:

```java
import org.yaml.snakeyaml.Yaml;

// ...

protected void setUp() throws Exception {
    Yaml yaml = new Yaml(new TrustedTagInspector());
    // ...
}
```

In this patch, we create a new `Yaml` instance and pass a new `TrustedTagInspector` instance to its constructor. This way, we can still use the `TrustedTagInspector` class, even if it's no longer available as a top-level class.

Note that this patch assumes that the rest of the `setUp()` method remains unchanged. If there are any other changes needed in the method, you may need to modify the patch accordingly.