Here's the proposed patch:

```java
@Override
public Policy<?> getPolicy(final PolicyConfig config) {
    final PolicyConfig sub = config.config("storage");
    Config cfg = new Config() {
        @Override
        public String string(String key) {
            return sub.string(key);
        }

        @Override
        public YamlMapping toYamlMapping() {
            return Yaml.createYamlInput(sub.toString()).readYamlMapping();
        }
    };
    try {
        return new YamlPolicy(
            new BlockingStorage(
                new com.artipie.asto.factory.StoragesLoader()
                    .newStorage(cfg)
            )
        );
    } catch (final IOException err) {
        throw new UncheckedIOException(err);
    }
}
```

The changes made include:

1. Creating an anonymous `Config` implementation that delegates to `PolicyConfig`.
2. Using `com.artipie.asto.factory.StoragesLoader` instead of `Storages`.
3. Calling `newStorage` with the custom `Config` implementation instead of `StorageConfig`.