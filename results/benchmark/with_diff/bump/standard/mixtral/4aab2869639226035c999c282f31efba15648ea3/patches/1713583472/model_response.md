Here's a fixed version of the `getPolicy` method:
```java
@Override
public Policy<?> getPolicy(final PolicyConfig config) {
    final PolicyConfig sub = config.config("storage");
    try {
        return new YamlPolicy(new BlockingStorage(new StoragesLoader().newStorage(sub.string("type"), com.amihaiemil.eoyaml.Yaml.createYamlInput(sub.toString()).readYamlMapping())));
    } catch (final IOException err) {
        throw new UncheckedIOException(err);
    }
}
```
The main change is replacing the deprecated `Storages` class with the new `StoragesLoader` class.