Here is the proposed patch:
```java
import org.yaml.snakeyaml.Yaml;

// ...

Yaml yaml = new Yaml(new CustomTagInspector());
// ...

private static class CustomTagInspector extends org.yaml.snakeyaml.inspector.BaseInspector {
    @Override
    public boolean isGlobalTagAllowed(Tag tag) {
        // Implement the logic you need here
    }
}
```
Explanation:

The `TrustedTagInspector` class has been removed in the new version of the library. Instead, you can extend the `BaseInspector` class and override the `isGlobalTagAllowed()` method to implement the necessary logic. This method has not been removed in the new version, so it can still be used.

The `Yaml` constructor now takes an instance of `Inspector` as a parameter. You can pass an instance of your custom `CustomTagInspector` class to it.

Note: The `CustomTagInspector` class and the `isGlobalTagAllowed()` method implementation are just placeholders. You need to replace them with the necessary logic for your use case.