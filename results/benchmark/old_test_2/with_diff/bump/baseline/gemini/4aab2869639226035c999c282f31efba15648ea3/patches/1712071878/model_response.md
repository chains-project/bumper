```java
  @Override
    public Policy<?> getPolicy(final PolicyConfig config) {
        final PolicyConfig sub = config.config("storage");
        try {
            return new YamlPolicy(
                new BlockingStorage(
                    StoragesLoader.newObject(
                        sub.string("type"),
                        new Config(Yaml.createYamlInput(sub.toString()).readYamlMapping())
                    )
                )
            );
        } catch (final IOException err) {
            throw new UncheckedIOException(err);
        }
    }
```