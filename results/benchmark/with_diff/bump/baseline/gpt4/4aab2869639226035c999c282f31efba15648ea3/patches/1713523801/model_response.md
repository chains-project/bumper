```java
@Override
public Policy<?> getPolicy(final PolicyConfig config) {
    final PolicyConfig sub = config.config("storage");
    try {
        StoragesLoader storagesLoader = new StoragesLoader();
        return new YamlPolicy(
            new BlockingStorage(
                storagesLoader.newObject(
                    sub.string("type"), new Config(sub.toString())
                )
            )
        );
    } catch (final IOException err) {
        throw new UncheckedIOException(err);
    }
}
```