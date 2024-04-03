Here is a fixed version of the method that should compile with the new library version:

```java
@Override
public Policy<?> getPolicy(final PolicyConfig config) {
    final PolicyConfig sub = config.config("storage");
    try {
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
        return new YamlPolicy(
            new BlockingStorage(
                new StoragesLoader().newStorage(
                    cfg
                )
            )
        );
    } catch (final IOException err) {
        throw new UncheckedIOException(err);
    }
}
```

The main change is the use of `StoragesLoader` instead of `Storages` and the creation of an anonymous `Config` implementation that can be used with the new `newStorage` method.