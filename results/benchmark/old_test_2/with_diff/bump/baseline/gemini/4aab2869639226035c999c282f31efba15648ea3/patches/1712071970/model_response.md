```java
  public Policy<?> getPolicy(final PolicyConfig config) {
        final PolicyConfig sub = config.config("storage");
        try {
            final Config storageConfig = new Config.FromYaml(Yaml.createYamlInput(sub.toString()).readYamlMapping());
            final StorageFactory storageFactory = new StoragesLoader().newFactory(sub.string("type"));
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