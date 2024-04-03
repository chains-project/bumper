Here's the fixed version of the `getPolicy` method:

```java
@Override
public Policy<?> getPolicy(final PolicyConfig config) {
    final PolicyConfig sub = config.config("storage");
    try {
        Config cfg = new YamlConfig(sub.toString());
        return new YamlPolicy(
            new BlockingStorage(
                new StoragesLoader().newStorage(
                    cfg.string("type")
                )
            )
        );
    } catch (final IOException err) {
        throw new UncheckedIOException(err);
    }
}
```

I changed the following:

1. Replaced `Storages` with `StoragesLoader` since the former has been removed.
2. Changed the `YamlInput` usage to a `YamlConfig` to read the config from the YAML string.
3. Modified the `newStorage` call to match the new method signature in `StoragesLoader`.

This code should resolve the "cannot find symbol" error for `Storages`.