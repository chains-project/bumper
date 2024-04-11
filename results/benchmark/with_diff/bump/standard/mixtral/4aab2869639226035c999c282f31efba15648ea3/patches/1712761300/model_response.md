Here's the proposed patch to fix the error:

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

The patch replaces the usage of the removed `Storages` class with the new `StoragesLoader` class, which provides a similar functionality. The `StoragesLoader` class is used to create a `Storage` object, which is then used to create a `BlockingStorage` object. The `StoragesLoader` class is part of the `com.artipie.asto.factory` package, which is included in the new library version.