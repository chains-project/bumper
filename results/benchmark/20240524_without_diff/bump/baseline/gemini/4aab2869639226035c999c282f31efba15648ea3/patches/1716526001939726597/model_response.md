```java
  public Policy<?> getPolicy(final PolicyConfig config) {
        final PolicyConfig sub = config.config("storage");
        final Config cfg = new Config.Simple(sub.asMap());
        try {
            return new YamlPolicy(
                new BlockingStorage(
                    new StoragesLoader().newObject(
                        sub.string("type"), cfg
                    )
                )
            );
        } catch (final IOException err) {
            throw new UncheckedIOException(err);
        }
    }
```