Here's the proposed patch for the failing client code:

```java
import com.artipie.asto.factory.StoragesLoader;
import java.util.Map;
import java.util.HashMap;

@Override
public com.artipie.security.policy.Policy<?> getPolicy(final com.artipie.security.policy.PolicyConfig config) {
    final com.artipie.security.policy.PolicyConfig sub = config.config("storage");
    try {
        StoragesLoader loader = new StoragesLoader(new HashMap<>());
        return new com.artipie.security.policy.YamlPolicy(new com.artipie.asto.blocking.BlockingStorage(loader.newObject(sub.string("type"), com.amihaiemil.eoyaml.Yaml.createYamlInput(sub.toString()).readYamlMapping())));
    } catch (final java.io.IOException err) {
        throw new java.io.UncheckedIOException(err);
    }
}
```

The patch creates a `StoragesLoader` instance and uses it to create a `Storage` object. The `StoragesLoader` constructor takes a `Map` parameter, which is initialized as an empty `HashMap`. The `newObject` method of `StoragesLoader` is used to create a `Storage` object with the necessary configuration.