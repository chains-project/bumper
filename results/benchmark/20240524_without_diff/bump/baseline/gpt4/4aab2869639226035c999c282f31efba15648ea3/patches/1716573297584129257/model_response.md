```java
@Override
public Policy<?> getPolicy(final PolicyConfig config) {
    final PolicyConfig sub = config.config("storage");
    try {
        final Yaml yaml = new Yaml();
        final String storageType = sub.string("type");
        final YamlMapping yamlMapping = yaml.loadAs(sub.toString(), YamlMapping.class);
        return new YamlPolicy(
            new BlockingStorage(
                new Storages().newStorage(storageType, yamlMapping)
            )
        );
    } catch (final IOException err) {
        throw new UncheckedIOException(err);
    }
}
```