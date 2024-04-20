Here's a proposed patch for the failing client code:

```java
@java.lang.Override
public com.artipie.security.policy.Policy<?> getPolicy(final com.artipie.security.policy.PolicyConfig config) {
    final com.artipie.security.policy.PolicyConfig sub = config.config("storage");
    try {
        return new com.artipie.security.policy.YamlPolicy(new com.artipie.asto.blocking.BlockingStorage(new com.artipie.asto.factory.StoragesLoader().newStorage(sub.string("type"), com.amihaiemil.eoyaml.Yaml.createYamlInput(sub.toString()).readYamlMapping())));
    } catch (final java.io.IOException err) {
        throw new java.io.UncheckedIOException(err);
    }
}
```

The main change is replacing the deprecated `Storages` class with the new `StoragesLoader` class. The `newStorage` method has been updated to take a `Config` object instead of a `StorageConfig` object, and the `Storages` constructor has been removed, so we use the `StoragesLoader` class instead.