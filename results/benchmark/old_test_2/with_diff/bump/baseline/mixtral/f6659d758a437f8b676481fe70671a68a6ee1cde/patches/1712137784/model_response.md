Here's a possible patch for the failing client code:
```java
import org.yaml.snakeyaml.Yaml;
import org.yaml.snakeyaml.nodes.Tag;

// ...

public void someMethod() {
    Yaml yaml = new Yaml(new MyTagInspector());
    // ...
}

private static class MyTagInspector extends org.yaml.snakeyaml.resolver.Resolver {
    @Override
    protected boolean isGlobalTagAllowed(Tag tag) {
        // your custom logic here
    }
}
```
In this patch, we create a new private static inner class `MyTagInspector` that extends `org.yaml.snakeyaml.resolver.Resolver`. We override the `isGlobalTagAllowed` method to implement the same functionality as the removed `TrustedTagInspector.isGlobalTagAllowed` method.

We then create a new `Yaml` instance using `MyTagInspector` instead of `TrustedTagInspector`.

Note that this patch assumes that the custom logic for `isGlobalTagAllowed` method is the same as before. If not, you may need to modify the implementation accordingly.