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
The patch replaces `Storages()` with `StoragesLoader()` and removes the type parameter `com.artipie.asto.factory.StorageConfig` from the constructor call, as the `StoragesLoader` class does not have such a constructor. Instead, it has a `newStorage` method that takes a `String` and a `YamlMapping` object, which can be used to create a `Storage` object.

Additionally, the `StoragesLoader` class has a `types` method that returns a set of package names, which can be used to register the storage types.

This patch should fix the error and allow the code to compile and run successfully.