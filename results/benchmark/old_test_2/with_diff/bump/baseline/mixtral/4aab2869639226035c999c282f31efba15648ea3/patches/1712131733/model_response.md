Here's the proposed patch:
```java
import com.artipie.asto.factory.StoragesLoader;
import com.artipie.asto.factory.Config;

@Override
public Policy<?> getPolicy(final PolicyConfig config) {
    final PolicyConfig sub = config.config("storage");
    try {
        StoragesLoader storages = new StoragesLoader();
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
Changes made:

* Imported `com.artipie.asto.factory.StoragesLoader` and `com.artipie.asto.factory.Config`.
* Created a new instance of `StoragesLoader` to use in place of the removed `Storages` class.
* Changed the argument of `storages.newStorage` from `StorageConfig` to `Config` to match the new method signature.