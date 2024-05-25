Here is a patch that you can apply to the code in order to fix the error:

```java
import org.yaml.snakeyaml.Yaml;

// ...

protected void setUp() throws Exception {
    Yaml yaml = new Yaml(new TrustedTagInspector());
    // ...
}
```

This patch imports the `Yaml` class from the `snakeyaml` library and creates a new `Yaml` instance with a `TrustedTagInspector` in the `setUp` method. This should fix the "cannot find symbol" error.

Note: I am assuming that the `TrustedTagInspector` class is still available in the version of the `snakeyaml` library that you are using. If it has been removed, you may need to find an alternative solution.