```java
@Override
public Policy<?> getPolicy(final PolicyConfig config) {
    final PolicyConfig sub = config.config("storage");
    try {
        final StoragesLoader loader = new StoragesLoader();
        final Config storageConfig =
            new Config.Simple(
                new HashMap<String, Object>() {{
                    put("type", sub.string("type"));
                    put("mapping", Yaml.createYamlInput(sub.toString()).readYamlMapping());
                }}
            );
        return new YamlPolicy(
            new BlockingStorage(
                loader.newObject(sub.string("type"), storageConfig)
            )
        );
    } catch (final IOException err) {
        throw new UncheckedIOException(err);
    }
}
```