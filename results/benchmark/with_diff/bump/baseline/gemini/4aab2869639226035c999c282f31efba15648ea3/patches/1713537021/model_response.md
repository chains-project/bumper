```java
  public Policy<?> getPolicy(final PolicyConfig config) {
        final PolicyConfig sub = config.config("storage");
        try {
            final StorageFactory factory = new StoragesLoader().newObject(sub.string("type"), sub);
            return new YamlPolicy(
                new BlockingStorage(
                    factory.newStorage(sub)
                )
            );
        } catch (final IOException err) {
            throw new UncheckedIOException(err);
        }
    }
```