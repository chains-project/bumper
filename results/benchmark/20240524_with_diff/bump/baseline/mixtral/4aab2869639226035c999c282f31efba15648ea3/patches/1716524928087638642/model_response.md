Here is the proposed patch:

```java
@Override
public Policy<?> getPolicy(final PolicyConfig config) {
    final PolicyConfig sub = config.config("storage");
    try {
        Config cfg = new Config()
            .with(sub.string("type"), Yaml.createYamlInput(sub.toString()).readYamlMapping());
        return new YamlPolicy(
            new BlockingStorage(
                new StorageFactory()
                    .newStorage(cfg)
            )
        );
    } catch (final IOException err) {
        throw new UncheckedIOException(err);
    }
}
```