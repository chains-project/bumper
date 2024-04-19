Here's a proposed patch to fix the error:
```java
@Override
public Policy<?> getPolicy(final PolicyConfig config) {
    final PolicyConfig sub = config.config("storage");
    try {
        return new YamlPolicy(
            new BlockingStorage(
                new StoragesLoader().newStorage(
                    sub.string("type"), Yaml.createYamlInput(sub.toString()).readYamlMapping()
                )
            )
        );
    } catch (final IOException err) {
        throw new UncheckedIOException(err);
    }
}
```
The patch removes the import of `com.artipie.asto.Storages` and uses the `StoragesLoader` class to create a `Storage` instance instead.
The `StoragesLoader` class is a new addition in the updated library version and provides a way to create a `Storage` instance from a `Config` object.
The `newStorage` method in `StoragesLoader` takes a `String` parameter representing the type of storage, and a `YamlMapping` object containing the configuration for that storage type.
The `YamlMapping` object is created using `Yaml.createYamlInput(sub.toString()).readYamlMapping()`, which reads the YAML configuration from the `sub` `PolicyConfig` object.
By using `StoragesLoader`, we avoid the need to import the removed `Storages` class and instead use the new `StoragesLoader` class to create the `Storage` instance.