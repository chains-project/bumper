Here's the proposed patch:

```java
import com.artipie.asto.factory.StorageFactory;
import com.artipie.asto.factory.Config;

@Override
public Policy<?> getPolicy(final PolicyConfig config) {
    final PolicyConfig sub = config.config("storage");
    try {
        return new YamlPolicy(
            new BlockingStorage(
                StorageFactory.newStorage(
                    new Config.From(
                        sub.string("type"),
                        Yaml.createYamlInput(sub.toString()).readYamlMapping()
                    )
                )
            )
        );
    } catch (final IOException err) {
        throw new UncheckedIOException(err);
    }
}
```

This patch replaces the removed `Storages` class with the new `StorageFactory` class, and updates the method signature of the `newStorage` method accordingly. The `Config.From` class is used to construct a `Config` object from the provided type and YAML mapping.