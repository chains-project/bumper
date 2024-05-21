Here's the proposed patch for the failing client code:

```java
import com.artipie.asto.factory.StoragesLoader;
import com.artipie.asto.fs.FileStorageFactory;
import java.util.Map;
import java.util.function.Function;

@Override
public com.artipie.security.policy.Policy<?> getPolicy(final com.artipie.security.policy.PolicyConfig config) {
    final com.artipie.security.policy.PolicyConfig sub = config.config("storage");
    try {
        StoragesLoader storagesLoader = new StoragesLoader();
        Function<String, Storage> newObject = storagesLoader.newObject(storagesLoader.defPackage(), Map::of);
        return new com.artipie.security.policy.YamlPolicy(new com.artipie.asto.blocking.BlockingStorage(newObject.apply(sub.string("type")), com.amihaiemil.eoyaml.Yaml.createYamlInput(sub.toString()).readYamlMapping())));
    } catch (final java.io.IOException err) {
        throw new java.io.UncheckedIOException(err);
    }
}
```

This patch creates a new `StoragesLoader` object and uses its `newObject` method to create a new `Storage` object. The `newObject` method takes a package name and a map of configuration properties, and returns a function that creates a new `Storage` object based on the given configuration. In this case, the package name is obtained from the `StoragesLoader` object itself using the `defPackage` method, and the configuration properties are obtained from an empty map using the `Map::of` method. The `Storage` object created by `newObject` is then used to create a `BlockingStorage` object, which is passed to the `YamlPolicy` constructor along with the parsed YAML configuration.