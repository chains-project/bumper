Here's a fixed version of the method using the added `StoragesLoader` class:

```java
@Override
public Policy<?> getPolicy(final PolicyConfig config) {
    final PolicyConfig sub = config.config("storage");
    try {
        StoragesLoader loader = new StoragesLoader();
        return new YamlPolicy(
            new BlockingStorage(
                loader.newStorage(
                    sub.string("type"), Yaml.createYamlInput(sub.toString()).readYamlMapping()
                )
            )
        );
    } catch (final IOException err) {
        throw new UncheckedIOException(err);
    }
}
```

The `Storages` class has been removed in the new library version, so we use the new `StoragesLoader` class to create a `Storage` object instead.