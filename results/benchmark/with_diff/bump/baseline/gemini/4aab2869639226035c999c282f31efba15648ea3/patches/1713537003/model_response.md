```java
public Policy<?> getPolicy(final PolicyConfig config) {
    final PolicyConfig sub = config.config("storage");
    try {
        final StoragesLoader storagesLoader = new StoragesLoader();
        final StorageFactory storageFactory = storagesLoader.newObject(sub.string("type"), sub);
        return new YamlPolicy(
            new BlockingStorage(
                storageFactory.newStorage(sub)
            )
        );
    } catch (final IOException err) {
        throw new UncheckedIOException(err);
    }
}
```