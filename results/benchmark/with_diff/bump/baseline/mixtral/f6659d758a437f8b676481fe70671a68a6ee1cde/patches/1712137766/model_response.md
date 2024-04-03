Here's the proposed patch:
```java
import org.yaml.snakeyaml.Yaml;

// create a TrustedTagInspector instance
TrustedTagInspector trustedTagInspector = new Yaml().getInspector().getTrustedTagInspector();

// use the TrustedTagInspector instance as needed
boolean isTagAllowed = trustedTagInspector.isGlobalTagAllowed(new Tag("!foo"));
```
Note that the `TrustedTagInspector` constructor is no longer public in the updated library version. However, we can still obtain an instance of `TrustedTagInspector` by creating a `Yaml` instance and calling `getInspector().getTrustedTagInspector()`. We can then use this instance as needed.