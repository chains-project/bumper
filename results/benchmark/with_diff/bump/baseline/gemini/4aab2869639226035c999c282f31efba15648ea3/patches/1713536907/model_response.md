```java
  public Policy<?> getPolicy(final PolicyConfig config) {
    final PolicyConfig sub = config.config("storage");
    final String type = sub.string("type");
    final YamlMapping mapping = Yaml.createYamlInput(sub.toString()).readYamlMapping();
    try {
      return new YamlPolicy(
        new BlockingStorage(
          new StoragesLoader().newObject(type, new Config(mapping))
        )
      );
    } catch (final IOException err) {
      throw new UncheckedIOException(err);
    }
  }
```