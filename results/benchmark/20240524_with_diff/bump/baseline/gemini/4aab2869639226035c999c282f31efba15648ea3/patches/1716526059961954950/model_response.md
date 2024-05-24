```java
  @Override
    public Policy<?> getPolicy(final PolicyConfig config) {
        final PolicyConfig sub = config.config("storage");

        final String type = sub.string("type");
        final YamlMapping yaml = Yaml.createYamlInput(sub.toString()).readYamlMapping();

        final StorageFactory factory = new StoragesLoader().newObject(type, new Config(yaml));

        try {
            return new YamlPolicy(
                new BlockingStorage(
                    factory.newStorage(new Config(yaml))
                )
            );
        } catch (final IOException err) {
            throw new UncheckedIOException(err);
        }
    }
```