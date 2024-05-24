Here's the proposed patch for the failing client code:

```java
@Override
public Policy<?> getPolicy(final PolicyConfig config) {
    final PolicyConfig sub = config.config("storage");
    try {
        Config cfg = new Config()
            .with(sub.string("type"), Yaml.createYamlInput(sub.toString()).readYamlMapping());
        return new YamlPolicy(
            new BlockingStorage(
                new StoragesLoader()
                    .newObject(cfg.type(), cfg)
            )
        );
    } catch (final IOException err) {
        throw new UncheckedIOException(err);
    }
}
```

In this patch, I replaced the `Storages` class with the new `StoragesLoader` class, which provides a `newObject` method to create a `Storage` instance based on a `Config` object. The `Config` class is a simple wrapper for the storage type and its configuration. Additionally, I used the new `Config` constructor that accepts a type and a `YamlMapping` object to simplify the creation of the `Config` instance.