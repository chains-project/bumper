Here's the proposed patch:

```java
import com.artipie.asto.factory.StoragesLoader;
import com.artipie.asto.factory.Config;

@Override
public Policy<?> getPolicy(final PolicyConfig config) {
    final PolicyConfig sub = config.config("storage");
    StoragesLoader storages = new StoragesLoader();
    try {
        return new YamlPolicy(
            new BlockingStorage(
                storages.newStorage(
                    sub.string("type"), Yaml.createYamlInput(sub.toString()).readYamlMapping()
                )
            )
        );
    } catch (final IOException err) {
        throw new UncheckedIOException(err);
    }
}
```

This patch replaces the `Storages` class with the new `StoragesLoader` class and updates the method call accordingly. The `StoragesLoader` class provides a `newStorage` method, which can be used to create a new `Storage` object. The `Storages` class and its associated methods have been removed in the new library version.