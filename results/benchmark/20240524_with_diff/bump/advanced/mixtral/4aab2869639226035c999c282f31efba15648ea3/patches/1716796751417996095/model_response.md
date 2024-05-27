Here's a possible patch for the failing client code:

```java
import com.artipie.asto.factory.StoragesLoader;
import java.util.Map;
import java.util.Collections;

@Override
public com.artipie.security.policy.Policy<?> getPolicy(final com.artipie.security.policy.PolicyConfig config) {
    final com.artipie.security.policy.PolicyConfig sub = config.config("storage");
    try {
        StoragesLoader loader = new StoragesLoader(Collections.emptyMap());
        return new com.artipie.security.policy.YamlPolicy(new com.artipie.asto.blocking.BlockingStorage(loader.newObject(sub.string("type"), new com.amihaiemil.eoyaml.YamlInput(sub.toString()).asInput())));
    } catch (final java.io.IOException err) {
        throw new java.io.UncheckedIOException(err);
    }
}
```

This patch creates a `StoragesLoader` instance and uses it to create a new storage object based on the `type` field of the `sub` configuration. It also uses a new `YamlInput` class from the `eoyaml` library to read the YAML input.