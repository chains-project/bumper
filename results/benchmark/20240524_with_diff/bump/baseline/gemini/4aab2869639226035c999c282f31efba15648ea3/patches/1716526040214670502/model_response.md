```java
@Override
public Policy<?> getPolicy(final PolicyConfig config) {
    final PolicyConfig sub = config.config("storage");
    try {
        final Config storageConfig = new Config.SimpleConfig(sub.asMap());
        final StorageFactory storageFactory = new StoragesLoader().newObject(sub.string("type"), storageConfig);
        return new YamlPolicy(
            new BlockingStorage(
                storageFactory.newStorage(storageConfig)
            )
        );
    } catch (final IOException err) {
        throw new UncheckedIOException(err);
    }
}
```