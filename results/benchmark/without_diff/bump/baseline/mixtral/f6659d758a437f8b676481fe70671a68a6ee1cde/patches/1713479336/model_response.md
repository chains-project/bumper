Here's a patch that you can apply to the code to fix the error:

```java
import org.yaml.snakeyaml.Yaml;

// ...

protected void setUp() throws Exception {
    Yaml yaml = new Yaml(new TrustedTagInspector());
    // ...
}
```

In this patch, we are creating a new instance of `Yaml` and passing it a new instance of `TrustedTagInspector`. This way, we can still use the `TrustedTagInspector` class even if it's not directly importable.