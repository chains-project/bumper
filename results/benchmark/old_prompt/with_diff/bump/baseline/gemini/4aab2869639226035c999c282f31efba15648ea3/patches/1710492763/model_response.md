```java
  public Policy<?> getPolicy(final PolicyConfig config) {
        final PolicyConfig sub = config.config("storage");
        try {
            return new YamlPolicy(
                new BlockingStorage(
                    new StoragesLoader().newObject(
                        sub.string("type"),
                        Yaml.createYamlInput(sub.toString()).readYamlMapping()
                    )
                )
            );
        } catch (final IOException err) {
            throw new UncheckedIOException(err);
        }
    }
```