Here's the fixed version of the `getPolicy` method:

```java
@Override
public Policy<?> getPolicy(final PolicyConfig config) {
    final PolicyConfig sub = config.config("storage");
    try {
        Config cfg = new Config()
            .with(sub.string("type"), Yaml.createYamlInput(sub.toString()).readYamlMapping());
        return new YamlPolicy(new BlockingStorage(new StoragesLoader().newStorage("default", cfg)));
    } catch (final IOException err) {
        throw new UncheckedIOException(err);
    }
}
```

The main change is the usage of the new `StoragesLoader` class, which provides a `newStorage` method that can be used instead of the removed `Storages` class. The `Config` class is used instead of the removed `StorageConfig` class. A new `Config` instance is created using a `with` method that takes a `String` and a `YamlMapping`.