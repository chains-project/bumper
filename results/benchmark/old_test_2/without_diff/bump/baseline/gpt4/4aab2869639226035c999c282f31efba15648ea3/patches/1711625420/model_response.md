```java
@Override
public Policy<?> getPolicy(final PolicyConfig config) {
    final PolicyConfig sub = config.config("storage");
    try {
        return new YamlPolicy(
            new BlockingStorage(
                new Storages().newStorage(
                    sub.string("type"), Yaml.createYamlInput(sub.rawData()).readYamlMapping()
                )
            )
        );
    } catch (final IOException err) {
        throw new UncheckedIOException(err);
    }
}
```