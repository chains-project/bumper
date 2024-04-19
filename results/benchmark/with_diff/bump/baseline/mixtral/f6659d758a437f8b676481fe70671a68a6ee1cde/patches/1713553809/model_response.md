Here's the proposed patch:
```java
import org.yaml.snakeyaml.Yaml;

// ...

protected Yaml createYaml() {
    Yaml yaml = new Yaml(new CustomTagInspector());
    // ...
    return yaml;
}

private static class CustomTagInspector extends org.yaml.snakeyaml.resolver.Resolver {
    @Override
    protected boolean isGlobalTagAllowed(Tag tag) {
        // Implement the desired logic here
        return true;
    }
}
```
Explanation:
Since the `TrustedTagInspector` class has been removed, we need to extend `org.yaml.snakeyaml.resolver.Resolver` instead and override the `isGlobalTagAllowed()` method to provide the desired behavior. The `Yaml` class now accepts a custom tag inspector, so we can pass an instance of our custom class.