```java
@Override
public Policy<?> getPolicy(final PolicyConfig config) {
    final PolicyConfig sub = config.config("storage");
    try {
        Storage storage = new Storages().newStorage(
            sub.string("type"), 
            Yaml.createYamlInput(sub.toString()).readYamlMapping()
        );
        return new YamlPolicy(
            new BlockingStorage(storage)
        );
    } catch (final IOException err) {
        throw new UncheckedIOException(err);
    }
}
```