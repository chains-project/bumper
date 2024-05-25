Here is the patched code:
```
public Policy<?> getPolicy(final PolicyConfig config) {
    final PolicyConfig sub = config.config("storage");
    final Map<String, Object> yamlMapping;
    try {
        yamlMapping = Yaml.createYamlInput(sub.toString()).readYamlMapping();
    } catch (final IOException err) {
        throw new UncheckedIOException(err);
    }
    return new YamlPolicy(
        new BlockingStorage(
            new Storages().newStorage(sub.string("type"), yamlMapping)
        )
    );
}
```