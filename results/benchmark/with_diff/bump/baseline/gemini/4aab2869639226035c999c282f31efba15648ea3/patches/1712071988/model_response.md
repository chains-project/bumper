```java
  @Override
    public Policy<?> getPolicy(final PolicyConfig config) {
        final PolicyConfig sub = config.config("storage");
        try {
            final Config storageConfig = new Config(sub.toString());
            final StorageFactory factory = new StoragesLoader().newObject(sub.string("type"), storageConfig);
            return new YamlPolicy(
                new BlockingStorage(
                    factory.newStorage(storageConfig)
                )
            );
        } catch (final IOException err) {
            throw new UncheckedIOException(err);
        }
    }
```