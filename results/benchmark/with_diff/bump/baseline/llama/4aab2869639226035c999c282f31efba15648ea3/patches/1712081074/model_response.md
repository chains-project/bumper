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
The patch removes the usage of `Storages` class, which is removed in the new library version, and instead uses the `StoragesLoader` class, which is added in the new version, to create a `Storage` instance.

The `StoragesLoader` class provides a way to load storage objects from the configuration, and the `newStorage` method is used to create a new storage object from a configuration map.

The rest of the code remains the same, as it does not depend on the removed `Storages` class.