```java
  @Override
    public Policy<?> getPolicy(final PolicyConfig config) {
        final PolicyConfig sub = config.config("storage");
        try {
            return new YamlPolicy(
                new BlockingStorage(
                    StoragesLoader.newObject(sub.string("type"), Config.of(sub))
                )
            );
        } catch (final IOException err) {
            throw new UncheckedIOException(err);
        }
    }
```