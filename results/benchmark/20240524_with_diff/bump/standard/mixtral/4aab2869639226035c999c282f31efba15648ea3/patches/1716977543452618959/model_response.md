Here is a possible patch for the code:
```java
import com.artipie.asto.factory.StoragesLoader;

@Override
public com.artipie.security.policy.Policy<?> getPolicy(final com.artipie.security.policy.PolicyConfig config) {
    final com.artipie.security.policy.PolicyConfig sub = config.config("storage");
    try {
        StoragesLoader storages = new StoragesLoader();
        return new com.artipie.security.policy.YamlPolicy(new com.artipie.asto.blocking.BlockingStorage(storages.newStorage(sub.string("type"), com.amihaiemil.eoyaml.Yaml.createYamlInput(sub.toString()).readYamlMapping())));
    } catch (final java.io.IOException err) {
        throw new java.io.UncheckedIOException(err);
    }
}
```
This patch uses the new `StoragesLoader` class to create a `Storage` object, instead of the old `Storages` class. The `StoragesLoader` class has a `newStorage` method that can be used to create a `Storage` object from a `Config` object, which can be obtained from the `sub` `PolicyConfig` object. The rest of the code remains unchanged.