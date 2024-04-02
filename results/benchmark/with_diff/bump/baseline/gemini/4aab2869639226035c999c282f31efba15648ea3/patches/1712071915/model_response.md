```java
  public Policy<?> getPolicy(final PolicyConfig config) {
    final PolicyConfig sub = config.config("storage");
    try {
      final Config cfg = Config.of(sub);
      final StorageFactory factory = new StoragesLoader().newObject(sub.string("type"), cfg);
      return new YamlPolicy(
          new BlockingStorage(
              factory.newStorage(cfg)
          )
      );
    } catch (final IOException err) {
      throw new UncheckedIOException(err);
    }
  }
```