```java
  public Policy<?> getPolicy(final PolicyConfig config) {
        final PolicyConfig sub = config.config("storage");
        try {
            final String type = sub.string("type");
            final YamlMapping mapping = Yaml.createYamlInput(sub.toString()).readYamlMapping();
            final Config storageConfig = new Config.Simple(mapping);
            final Storage storage = new StoragesLoader().newObject(type, storageConfig);
            return new YamlPolicy(
                new BlockingStorage(
                    storage
                )
            );
        } catch (final IOException err) {
            throw new UncheckedIOException(err);
        }
    }
```