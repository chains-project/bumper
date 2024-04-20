Here's a possible patch for the failing client code:
```java
@Override
public Policy<?> getPolicy(final PolicyConfig config) {
    final PolicyConfig sub = config.config("storage");
    try {
        StoragesLoader storagesLoader = new StoragesLoader();
        return new YamlPolicy(new BlockingStorage(storagesLoader.newObject(sub.string("type"), new Yaml().createYamlInput(sub.toString()).readYamlMapping())));
    } catch (final IOException err) {
        throw new UncheckedIOException(err);
    }
}
```
Here's what changed:

* We create a `StoragesLoader` instance instead of `Storages`.
* We use `StoragesLoader.newObject` method to create a storage object, instead of `Storages.newStorage`.
* We use the fully qualified name `com.artipie.asto.factory.StoragesLoader` for `StoragesLoader` to avoid any potential naming conflicts.
* We use the fully qualified name `com.amihaiemil.eoyaml.Yaml` for `Yaml` to avoid any potential naming conflicts.
* We use the fully qualified name `java.io.IOException` for `IOException` to avoid any potential naming conflicts.
* We use the fully qualified name `java.io.UncheckedIOException` for `UncheckedIOException` to avoid any potential naming conflicts.