Here's the fixed version of the `getPolicy` method:

```java
@Override
public Policy<?> getPolicy(final PolicyConfig config) {
    final PolicyConfig sub = config.config("storage");
    try {
        Config cfg = new Config().with("type", sub.string("type"));
        cfg = cfg.with("config", Yaml.createYamlInput(sub.toString()).readYamlMapping());
        return new YamlPolicy(new BlockingStorage(new StoragesLoader().newStorage(cfg)));
    } catch (final IOException err) {
        throw new UncheckedIOException(err);
    }
}
```

In this fixed version, I replaced the usage of the removed `Storages` class with the new `StoragesLoader` class. I also modified the creation of the `Config` object to accommodate the new method signature of the `newStorage` method in the `StoragesLoader` class.