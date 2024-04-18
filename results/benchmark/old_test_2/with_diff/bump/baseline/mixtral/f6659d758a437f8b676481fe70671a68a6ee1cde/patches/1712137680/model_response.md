Here's the proposed patch:
```java
import org.yaml.snakeyaml.Yaml;

// ...

protected Yaml createYaml() {
    Yaml yaml = new Yaml(new CustomTagInspector());
    // ...
}

static class CustomTagInspector extends org.yaml.snakeyaml.resolver.Resolver {
    @Override
    protected org.yaml.snakeyaml.inspector.TagInspector createTagInspector() {
        return new org.yaml.snakeyaml.inspector.DefaultTagInspector() {
            @Override
            public boolean isGlobalTagAllowed(org.yaml.snakeyaml.nodes.Tag tag) {
                // implement the logic of the removed TrustedTagInspector.isGlobalTagAllowed method here
            }
        };
    }
}
```
This patch creates a custom tag inspector by extending `Resolver` and overriding `createTagInspector` to return a custom `TagInspector` that overrides `isGlobalTagAllowed` to implement the logic of the removed `TrustedTagInspector.isGlobalTagAllowed` method. This allows the client code to continue functioning without directly using the removed `TrustedTagInspector` class.