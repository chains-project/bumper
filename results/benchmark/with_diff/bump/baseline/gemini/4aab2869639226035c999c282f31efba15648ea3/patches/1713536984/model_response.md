```java
@Override
public Policy<?> getPolicy(final PolicyConfig config) {
    final PolicyConfig sub = config.config("storage");
    final StoragesLoader loader = new StoragesLoader();
    try {
        return new YamlPolicy(
            new BlockingStorage(
                loader.newObject(sub.string("type"), sub)
            )
        );
    } catch (final IOException err) {
        throw new UncheckedIOException(err);
    }
}
```