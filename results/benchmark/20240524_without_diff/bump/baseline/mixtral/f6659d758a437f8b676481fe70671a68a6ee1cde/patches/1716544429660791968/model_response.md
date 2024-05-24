Here's a patch that you can apply to the client code to fix the error:

```java
import org.yaml.snakeyaml.inspector.TrustedPrefixesTagInspector;

// ...

@Override
protected TrustedTagInspector createTagInspector() {
    return new TrustedPrefixesTagInspector(Collections.emptyList());
}
```

This code creates a new `TrustedPrefixesTagInspector` object with an empty list of trusted prefixes. The `createTagInspector` method is overridden to return this new object. This should fix the error caused by the missing `TrustedTagInspector` class.