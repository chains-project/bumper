Here's the proposed patch for the failing client code:

```java
import org.yaml.snakeyaml.nodes.Tag;
import org.yaml.snakeyaml.inspector.TrustedPrefixesTagInspector;

public class CustomTrustedTagInspector extends TrustedPrefixesTagInspector {
    public CustomTrustedTagInspector() {
        super(null);
    }

    @Override
    public boolean isGlobalTagAllowed(Tag tag) {
        return true;
    }
}

import org.yaml.snakeyaml.Yaml;
import org.yaml.snakeyaml.constructor.Constructor;

// ...

Yaml yaml = new Yaml(new Constructor(YourClass.class), new CustomTrustedTagInspector());
```

This patch creates a custom `CustomTrustedTagInspector` class that extends `TrustedPrefixesTagInspector` and overrides the `isGlobalTagAllowed` method. This is done because the `TrustedTagInspector` class and its `isGlobalTagAllowed` method are removed in the new library version. The `CustomTrustedTagInspector` class can then be used as a replacement for `TrustedTagInspector` in the `Yaml` constructor.