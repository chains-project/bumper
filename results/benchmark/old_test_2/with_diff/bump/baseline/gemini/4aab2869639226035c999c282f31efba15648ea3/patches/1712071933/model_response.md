```java
  public Policy<?> getPolicy(final PolicyConfig config) {
    final PolicyConfig sub = config.config("storage");
    try {
      final StorageFactory storageFactory = new StoragesLoader().newObject(sub.string("type"), sub.toString());
      return new YamlPolicy(
          new BlockingStorage(
              storageFactory.newStorage(
                  new Config() {
                    @Override
                    public String get(final String key) {
                      return sub.string(key);
                    }
                  }
              )
          )
      );
    } catch (final IOException err) {
      throw new UncheckedIOException(err);
    }
  }
```