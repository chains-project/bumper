```java
public Policy<?> getPolicy(final PolicyConfig config) {
    final PolicyConfig sub = config.config("storage");
    try {
        StoragesLoader loader = new StoragesLoader();
        return new YamlPolicy(
            new BlockingStorage(
                loader.newObject(sub.string("type"), new Config(sub.toString()))
            )
        );
    } catch (final IOException err) {
        throw new UncheckedIOException(err);
    }
}
```