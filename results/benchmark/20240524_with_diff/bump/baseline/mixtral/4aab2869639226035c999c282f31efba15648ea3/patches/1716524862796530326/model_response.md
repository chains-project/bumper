Here is a possible patch for the failing client code:
```java
    @Override
    public Policy<?> getPolicy(final PolicyConfig config) {
        final PolicyConfig sub = config.config("storage");
        try {
            Config cfg = new Config()
                .with(sub.string("type"), Yaml.createYamlInput(sub.toString()).readYamlMapping());
            return new YamlPolicy(
                new BlockingStorage(
                    new StorageFactory()
                        .newStorage(cfg)
                )
            );
        } catch (final IOException err) {
            throw new UncheckedIOException(err);
        }
    }
```
In this patch, I replaced the removed `Storages` class with the new `StorageFactory` class, and used the new `newStorage` method that takes a `Config` object instead of a `StorageConfig` object. I also created a new `Config` object to replace the removed `Storages` constructor.