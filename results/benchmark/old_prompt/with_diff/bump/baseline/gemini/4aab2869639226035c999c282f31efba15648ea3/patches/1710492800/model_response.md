```java
  @Override
    public Policy<?> getPolicy(final PolicyConfig config) {
        final PolicyConfig sub = config.config("storage");
        try {
            final Config config =
                new Config() {
                  @Override
                  public String string(final String key) {
                    return sub.string(key);
                  }

                  @Override
                  public <T> T object(final String key, final Class<T> type) {
                    return null;
                  }
                };
            return new YamlPolicy(
                new BlockingStorage(new StoragesLoader().newObject(sub.string("type"), config))
            );
        } catch (final IOException err) {
            throw new UncheckedIOException(err);
        }
    }
```