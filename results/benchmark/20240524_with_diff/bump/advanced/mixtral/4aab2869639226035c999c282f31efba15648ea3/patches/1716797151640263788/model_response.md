Here's a proposed patch for the failing client code:

```java
import com.artipie.asto.factory.StoragesLoader;

@Override
public com.artipie.security.policy.Policy<?> getPolicy(final com.artipie.security.policy.PolicyConfig config) {
    final com.artipie.security.policy.PolicyConfig sub = config.config("storage");
    try {
        StoragesLoader storagesLoader = new StoragesLoader();
        return new com.artipie.security.policy.YamlPolicy(new com.artipie.asto.blocking.BlockingStorage(storagesLoader.newObject(sub.string("type"), com.amihaiemil.eoyaml.Yaml.createYamlInput(sub.toString()).readYamlMapping())));
    } catch (final java.io.IOException err) {
        throw new java.io.UncheckedIOException(err);
    }
}
```

In this patch, I created a `StoragesLoader` instance and used its `newObject` method to create a new `Storage` object with the provided configuration. This is possible because the new library version includes the `StoragesLoader` class, which provides a convenient way to create different types of `Storage` objects.

Note that I had to import the `com.artipie.asto.factory.StoragesLoader` class at the beginning of the code.