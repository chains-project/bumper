```java
public Policy<?> getPolicy(final PolicyConfig config) {
    final PolicyConfig sub = config.config("storage");
    final Map<String, Object> yamlMap;
    try {
        yamlMap = Yaml.createYamlInput(sub.toString()).readYamlMapping();
    } catch (final IOException err) {
        throw new UncheckedIOException(err);
    }
    return new YamlPolicy(
        new BlockingStorage(
            new Storages().newStorage(
                sub.string("type"), yamlMap
            )
        )
    );
}
```