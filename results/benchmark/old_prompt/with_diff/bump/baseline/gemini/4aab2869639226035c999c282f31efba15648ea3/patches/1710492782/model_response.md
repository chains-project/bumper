```java
  public Policy<?> getPolicy(final PolicyConfig config) {
        final PolicyConfig sub = config.config("storage");
        try {
            ++final Config storageConfig = new Config(Yaml.createYamlInput(sub.toString()).readYamlMapping());
            return new YamlPolicy(
                new BlockingStorage(
                    ++new StoragesLoader().newObject(
                        sub.string("type"), storageConfig
                    )
                )
            );
        } catch (final IOException err) {
            throw new UncheckedIOException(err);
        }
    }
```