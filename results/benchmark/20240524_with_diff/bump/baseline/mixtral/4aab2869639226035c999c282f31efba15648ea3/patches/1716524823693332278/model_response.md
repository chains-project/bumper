Here's the proposed patch:

```java
  @Override
  public Policy<?> getPolicy(final PolicyConfig config) {
    final PolicyConfig sub = config.config("storage");
    try {
      Configasto configAsto = Configasto.create(sub.toString());
      return new YamlPolicy(
          new BlockingStorage(
              new StoragesLoader()
                  .newObject(configAsto.type(), configAsto.yamlMapping())
          )
      );
    } catch (final IOException err) {
      throw new UncheckedIOException(err);
    }
  }

  static class Configasto {
    private Configasto(final String yamlMapping) {
      this.yamlMapping = yamlMapping;
    }

    static Configasto create(final String config) {
      return new Configasto(Yaml.createYamlInput(config).readYamlMapping());
    }

    String type() {
      return yamlMapping.string("type");
    }

    YamlMapping yamlMapping() {
      return yamlMapping;
    }

    private final YamlMapping yamlMapping;
  }
```

I added a helper class `Configasto` to parse the configuration and extract the necessary information. The `StoragesLoader` class is used instead of the removed `Storages` class. The `newStorage` method now takes a `Config` object instead of a `StorageConfig` object.