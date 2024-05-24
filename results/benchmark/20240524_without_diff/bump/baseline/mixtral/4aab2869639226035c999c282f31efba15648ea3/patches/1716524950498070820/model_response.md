Here's a possible patch for the code:

```java
  @Override
  public Policy<?> getPolicy(final PolicyConfig config) {
    final PolicyConfig sub = config.config("storage");
    try {
      Config cfg = new Config()
        .with(Sub Configs.single("type", sub.string("type")))
        .with(Sub Configs.single("params", Yaml.createYamlInput(sub.toString()).readYamlMapping()));
      return new YamlPolicy(
          new BlockingStorage(
              new StorageFactory().newStorage(cfg)
          )
      );
    } catch (final IOException err) {
      throw new UncheckedIOException(err);
    }
  }
```

In this patch, I removed the dependency on `Storages` and used `StorageFactory` instead, which is a new class that was added in the updated library version. I also used the new `Config` class and `Sub Configs` class to build a configuration object for the new `StorageFactory`.