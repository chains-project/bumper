Here's the proposed patch:

```java
@java.lang.Override
public com.artipie.security.policy.Policy<?> getPolicy(final com.artipie.security.policy.PolicyConfig config) {
    final com.artipie.security.policy.PolicyConfig sub = config.config("storage");
    try {
        StoragesLoader storagesLoader = new com.artipie.asto.factory.StoragesLoader();
        return new com.artipie.security.policy.YamlPolicy(new com.artipie.asto.blocking.BlockingStorage(storagesLoader.newStorage(sub.string("type"), com.amihaiemil.eoyaml.Yaml.createYamlInput(sub.toString()).readYamlMapping())));
    } catch (final java.io.IOException err) {
        throw new java.io.UncheckedIOException(err);
    }
}
```

In this patch, we replaced the `Storages` class with the new `StoragesLoader` class, which provides a `newStorage` method that can be used to create a storage object. We also removed the `com.artipie.asto.factory.StorageConfig` parameter from the `newStorage` method and replaced it with the more general `com.artipie.asto.factory.Config` parameter. This allows us to use the same method to create a storage object for any type of configuration.