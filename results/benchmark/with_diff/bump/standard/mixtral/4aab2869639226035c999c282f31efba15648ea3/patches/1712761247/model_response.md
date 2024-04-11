Here's a possible patch for the failing client code:

```java
@Override
public Policy<?> getPolicy(final PolicyConfig config) {
    final PolicyConfig sub = config.config("storage");
    try {
        StoragesLoader storagesLoader = new StoragesLoader();
        return new YamlPolicy(new BlockingStorage(storagesLoader.newStorage(sub.string("type"), com.amihaiemil.eoyaml.Yaml.createYamlInput(sub.toString()).readYamlMapping())));
    } catch (final IOException err) {
        throw new UncheckedIOException(err);
    }
}
```

The changes made include:

* Importing the new `StoragesLoader` class.
* Creating a new `StoragesLoader` object.
* Using the new `newStorage` method on `StoragesLoader` instead of the old `Storages` class.
* Importing the `UncheckedIOException` class from `java.io` instead of `java.io.UncheckedIOException`.
* Removing the unnecessary explicit import for `java.lang.Override`.

Note that this patch assumes that the new `StoragesLoader` class can be used in a similar way to the old `Storages` class, and that the `newStorage` method on `StoragesLoader` can take a `Config` object instead of a `StorageConfig` object. If these assumptions are incorrect, further modifications may be necessary.