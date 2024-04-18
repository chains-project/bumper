Here is a possible patch for the failing code:
```java
import org.yaml.snakeyaml.Yaml;

TrustedTagInspector trustInspector = new TrustedTagInspector();
Yaml yaml = new Yaml(trustInspector);
```
This code creates a new `TrustedTagInspector` object and passes it to the `Yaml` constructor. This should fix the "cannot find symbol" error.

Note: This patch assumes that the `TrustedTagInspector` class is still available in the new version of the library, but may have been moved or renamed. If this is not the case, you may need to modify the import statement or use a different approach to create a `TrustedTagInspector` object.