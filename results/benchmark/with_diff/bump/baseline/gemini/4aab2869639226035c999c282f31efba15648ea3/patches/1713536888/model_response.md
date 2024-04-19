```java
@Override
public Policy<?> getPolicy(final PolicyConfig config) {
    final PolicyConfig sub = config.config("storage");
    final String type = sub.string("type");
    final Config storageConfig = new Config.Builder()
        .add(sub)
        .build();
    try {
        return new YamlPolicy(
            new BlockingStorage(
                new StoragesLoader().newObject(type, storageConfig)
            )
        );
    } catch (final IOException err) {
        throw new UncheckedIOException(err);
    }
}
```