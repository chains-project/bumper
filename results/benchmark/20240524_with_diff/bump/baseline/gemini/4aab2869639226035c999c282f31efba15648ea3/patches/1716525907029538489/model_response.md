```java
@Override
public Policy<?> getPolicy(final PolicyConfig config) {
    final PolicyConfig sub = config.config("storage");
    try {
        final StoragesLoader loader = new StoragesLoader();
        final Config storageConfig = new Config.From(sub.asMap());
        final String factoryName = loader.getFactoryName(BlockingStorage.class);
        final Storage storage = loader.newObject(factoryName, storageConfig);
        return new YamlPolicy(new BlockingStorage(storage));
    } catch (final IOException err) {
        throw new UncheckedIOException(err);
    }
}
```