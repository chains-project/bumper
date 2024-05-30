Here's the fixed method:

```java
@Override
public Policy<?> getPolicy(final PolicyConfig config) {
    final PolicyConfig sub = config.config("storage");
    try {
        StoragesLoader storages = new StoragesLoader();
        return new YamlPolicy(new BlockingStorage(storages.newObject(sub.string("type"), new YamlMappingImpl(com.amihaiemil.eoyaml.Yaml.createYamlInput(sub.toString()).readYamlMapping()))));
    } catch (final IOException err) {
        throw new UncheckedIOException(err);
    }
}
```

Changes made:

* Replaced `com.artipie.asto.factory.Storages` with `com.artipie.asto.factory.StoragesLoader`, which is the new class that provides similar functionality.
* Replaced `com.artipie.asto.factory.Storages.newStorage` with `com.artipie.asto.factory.StoragesLoader.newObject`, which is the new method that creates a storage object.
* Added `new YamlMappingImpl` to convert the `com.amihaiemil.eoyaml.YamlMapping` to `com.artipie.asto.factory.Config`, which is required by the new `StoragesLoader.newObject` method.
* Removed unnecessary imports and qualified names for brevity.