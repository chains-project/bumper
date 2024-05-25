Here's a possible patch that you can apply to the code:

```java
import org.yaml.snakeyaml.Yaml;

TrustedTagInspector trustInspector = new TrustedTagInspector();
Yaml yaml = new Yaml(trustInspector);
```

This code creates an instance of `TrustedTagInspector` and passes it to the `Yaml` constructor. This allows you to use the `Yaml` class while still specifying a custom `TagInspector`.

Note that this code assumes that you have access to the `TrustedTagInspector` class, which is part of the `snakeyaml-engine` library. If you don't have access to this library, you may need to find a different way to customize the `Yaml` constructor.

Also, note that the `override` decorator has been removed from the method, as it was not overriding any method in the new version.