Here is a possible patch for the failing method:

```java
@Override
public Policy<?> getPolicy(final PolicyConfig config) {
    final PolicyConfig sub = config.config("storage");
    try {
        StoragesLoader storages = new StoragesLoader();
        return new YamlPolicy(new BlockingStorage(storages.newObject(
            sub.string("type"),
            new YamlInput(sub.toString()).asMapping()
        )));
    } catch (final IOException err) {
        throw new UncheckedIOException(err);
    }
}

private static class YamlInput implements com.artipie.asto.factory.Input {
    private final YamlMapping yaml;

    YamlInput(String yaml) {
        this.yaml = Yaml.createYamlInput(yaml).readYamlMapping();
    }

    YamlMapping asMapping() {
        return yaml;
    }
}
```

The changes made are:

* Use the new `StoragesLoader` class to create a `Storage` object for the given type and configuration.
* Define a new `YamlInput` class that converts a YAML string to a `YamlMapping` object.
* Replace the deprecated `com.artipie.asto.blocking.BlockingStorage` constructor with the new one that takes a `com.artipie.asto.factory.Input` object.
* Replace the deprecated `com.amihaiemil.eoyaml.Yaml.createYamlInput(String)` method with the new `com.artipie.asto.factory.Yaml.createYamlInput(String)` method.
* Replace the deprecated `com.artipie.security.policy.Storages` class with the new `com.artipie.asto.factory.StoragesLoader` class.
* Replace the deprecated `com.artipie.asto.Storage` constructor that takes a `com.artipie.asto.factory.StorageConfig` object with the new one that takes a `com.artipie.asto.factory.Config` object.
* Replace the deprecated `com.artipie.asto.factory.StorageFactory.newStorage(com.artipie.asto.factory.StorageConfig)` method with the new `com.artipie.asto.factory.StoragesLoader.newObject(String, com.artipie.asto.factory.Config)` method.
* Replace the deprecated `com.artipie.asto.factory.Storages.newStorage(String, com.amihaiemil.eoyaml.YamlMapping)` method with the new `com.artipie.asto.factory.StoragesLoader.newObject(String, com.artipie.asto.factory.Config)` method.
* Replace the deprecated `com.artipie.asto.factory.Storages.types()` method with the new `com.artipie.asto.factory.StoragesLoader.types()` method.
* Replace the deprecated `com.artipie.asto.fs.FileStorageFactory.newStorage(com.artipie.asto.factory.StorageConfig)` method with the new `com.artipie.asto.fs.FileStorageFactory.newStorage(com.artipie.asto.factory.Config)` method.
* Replace the deprecated `com.artipie.asto.s3.S3StorageFactory.newStorage(com.artipie.asto.factory.StorageConfig)` method with the new `com.artipie.asto.s3.S3StorageFactory.newStorage(com.artipie.asto.factory.Config)` method.