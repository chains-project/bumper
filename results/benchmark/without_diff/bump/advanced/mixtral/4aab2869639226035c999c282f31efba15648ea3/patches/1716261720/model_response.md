Here's the proposed patch:

```java
@Override
public Policy<?> getPolicy(final PolicyConfig config) {
    final PolicyConfig sub = config.config("storage");
    try {
        return new YamlPolicy(new BlockingStorage(new com.artipie.asto.Storage.Default(com.artipie.asto.ext.Refs.class, new com.artipie.asto.Storage.StorageCntlr(sub.string("type"), com.amihaiemil.eoyaml.Yaml.createYamlInput(sub.toString()).readYamlMapping()))));
    } catch (final IOException err) {
        throw new UncheckedIOException(err);
    }
}
```

This patch uses the `Default` class from `com.artipie.asto.Storage` package instead of the removed `Storages` class. It also replaces the `com.artipie.security.policy.Storages` with `com.artipie.asto.Storage.Default` and `com.artipie.security.policy.Storages.newStorage` with `com.artipie.asto.Storage.Default`. The `Refs` class from `com.artipie.asto.ext` package is used instead of the removed `com.artipie.security.policy.Storages.Refs`.