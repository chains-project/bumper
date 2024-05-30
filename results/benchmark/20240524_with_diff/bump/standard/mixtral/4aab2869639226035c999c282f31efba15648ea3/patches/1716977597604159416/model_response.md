Here's the fixed method with the changes needed to resolve the error:

```java
@Override
public Policy<?> getPolicy(final PolicyConfig config) {
    final PolicyConfig sub = config.config("storage");
    try {
        StoragesLoader storages = new StoragesLoader();
        return new YamlPolicy(new BlockingStorage(storages.newStorage(sub.string("type"), com.amihaiemil.eoyaml.Yaml.createYamlInput(sub.toString()).readYamlMapping())));
    } catch (final IOException err) {
        throw new UncheckedIOException(err);
    }
}
```

I changed the `com.artipie.asto.factory.Storages` class to `com.artipie.asto.factory.StoragesLoader` and its method `newStorage` to accommodate the new library version's changes.