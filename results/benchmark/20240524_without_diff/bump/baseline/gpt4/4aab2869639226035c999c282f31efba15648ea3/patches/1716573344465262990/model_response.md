```java
@Override
public Policy<?> getPolicy(final PolicyConfig config) {
    final PolicyConfig sub = config.config("storage");
    try {
        YamlMapping yamlMapping = Yaml.createYamlInput(sub.value("type").toString()).readYamlMapping();
        return new YamlPolicy(
            new BlockingStorage(
                new Storages().newStorage(
                    sub.string("type"), yamlMapping
                )
            )
        );
    } catch (final IOException err) {
        throw new UncheckedIOException(err);
    }
}
```