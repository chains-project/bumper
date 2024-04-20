Here's a possible patch for the failing client code:

```java
@java.lang.Override
public com.artipie.security.policy.Policy<?> getPolicy(final com.artipie.security.policy.PolicyConfig config) {
    final com.artipie.security.policy.PolicyConfig sub = config.config("storage");
    try {
        StoragesLoader storages = new com.artipie.asto.factory.StoragesLoader();
        return new com.artipie.security.policy.YamlPolicy(new com.artipie.asto.blocking.BlockingStorage(storages.newStorage(sub.string("type"), com.amihaiemil.eoyaml.Yaml.createYamlInput(sub.toString()).readYamlMapping())));
    } catch (final java.io.IOException err) {
        throw new java.io.UncheckedIOException(err);
    }
}
```

The main change is the creation of a `StoragesLoader` object, which can be used to create a `Storage` object for the given config. Note that the `Storages` class has been removed in the new library version, and has been replaced by the `StoragesLoader` class.