Here's the proposed patch:
```java
import org.yaml.snakeyaml.nodes.Tag;
import org.yaml.snakeyaml.inspector.TrustedPrefixesTagInspector;

// ...

@Override
protected TrustedTagInspector getTrustedTagInspector() {
    return new TrustedPrefixesTagInspector(null);
}

@Override
protected boolean isGlobalTagAllowed(Tag tag) {
    TrustedPrefixesTagInspector inspector = getTrustedTagInspector();
    return inspector.isGlobalTagAllowed(tag);
}
```
This patch creates a `TrustedPrefixesTagInspector` instance and uses the new method `isGlobalTagAllowed` to check if a tag is allowed. Note that the `TrustedTagInspector` constructor is no longer available, so we use the `TrustedPrefixesTagInspector` constructor instead.