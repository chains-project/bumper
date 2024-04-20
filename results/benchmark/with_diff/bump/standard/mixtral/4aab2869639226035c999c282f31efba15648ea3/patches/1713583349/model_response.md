Here's the proposed patch for the failing client code:

```java
@Override
public Policy<?> getPolicy(final PolicyConfig config) {
    final PolicyConfig sub = config.config("storage");
    try {
        StoragesLoader storages = new StoragesLoader();
        return new YamlPolicy(new BlockingStorage(storages.newObject(sub.string("type"), new Yaml().createYamlInput(sub.toString()).readYamlMapping())));
    } catch (final IOException err) {
        throw new UncheckedIOException(err);
    }
}
```

Here are the changes I made:

* Replaced `com.artipie.asto.factory.Storages` with `com.artipie.asto.factory.StoragesLoader`
* Replaced `com.artipie.asto.factory.Storages.newStorage` with `com.artipie.asto.factory.StoragesLoader.newObject`
* Replaced `com.amihaiemil.eoyaml.Yaml.createYamlInput(sub.toString()).readYamlMapping()` with `new Yaml().createYamlInput(sub.toString()).readYamlMapping()`
* Replaced `java.io.UncheckedIOException` with `com.artipie.asto.factory.UncheckedIOException`

Note: I assumed that `Yaml` and `UncheckedIOException` are imported from `com.amihaiemil.eoyaml` and `com.artipie.asto.factory` packages respectively. If not, please import them as needed.