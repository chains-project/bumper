```java
  @Override
    public Policy<?> getPolicy(final PolicyConfig config) {
        final PolicyConfig sub = config.config("storage");
        try {
            final Config storage = Config.from(Yaml.createYamlInput(sub.toString()).readYamlMapping());
            final StoragesLoader loader = new StoragesLoader();
            final StorageFactory factory = loader.newObject(storage.getString("type"), storage);
            return new YamlPolicy(new BlockingStorage(factory.newStorage(storage)));
        } catch (final IOException err) {
            throw new UncheckedIOException(err);
        }
    }
```