Here's a fixed version of the code that replaces the deprecated `Storages` class with the new `Storage` class:

```java
@Override
public Policy<?> getPolicy(final PolicyConfig config) {
    final PolicyConfig sub = config.config("storage");
    try {
        return new YamlPolicy(new BlockingStorage(new Storage.Single(
                sub.string("type"),
                Yaml.createYamlInput(sub.toString()).readYamlMapping()
        )));
    } catch (final IOException err) {
        throw new UncheckedIOException(err);
    }
}
```

In this updated version, we use the new `Storage.Single` class to create a single storage instance, passing in the type and the YAML mapping from the configuration. We also update the imports and exception handling to use the new classes and methods introduced in the updated library.