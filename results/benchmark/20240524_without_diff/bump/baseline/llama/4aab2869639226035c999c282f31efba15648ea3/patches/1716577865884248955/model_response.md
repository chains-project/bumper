```java
public Policy<?> getPolicy(final PolicyConfig config) {
    final PolicyConfig sub = config.config("storage");
    final Mapping yamlMapping;
    try {
        yamlMapping = Yaml.createYamlInput(sub.toString()).readYamlMapping();
    } catch (final IOException err) {
        throw new UncheckedIOException(err);
    }
    final Storage storage = new Storages().newStorage(sub.string("type"), yamlMapping);
    return new YamlPolicy(new BlockingStorage(storage));
}
```