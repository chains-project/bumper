```java
@Override
public Policy<?> getPolicy(final PolicyConfig config) {
    final PolicyConfig sub = config.config("storage");
    try {
        Yaml yaml = new Yaml();
        String yamlString = sub.toString();
        YamlMapping yamlMapping = yaml.createYamlInput(yamlString).readYamlMapping();
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