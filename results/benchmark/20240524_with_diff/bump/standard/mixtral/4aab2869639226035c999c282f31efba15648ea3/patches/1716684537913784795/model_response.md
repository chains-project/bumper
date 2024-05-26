Here is a possible patch for the failing client code:

```java
@java.lang.Override
public com.artipie.security.policy.Policy<?> getPolicy(final com.artipcom.security.policy.PolicyConfig config) {
    final com.artipie.security.policy.PolicyConfig sub = config.config("storage");
    try {
        return new com.artipie.security.policy.YamlPolicy(new com.artipie.asto.blocking.BlockingStorage(new com.artipie.asto.factory.StoragesLoader().newStorage(sub.string("type"), com.amihaiemil.eoyaml.Yaml.createYamlInput(sub.toString()).readYamlMapping())));
    } catch (final java.io.IOException err) {
        throw new java.io.UncheckedIOException(err);
   
    }
}
```

The main changes are:

* Replace `new com.artipie.security.policy.Storages().newStorage(...)` with `new com.artipie.asto.factory.StoragesLoader().newStorage(...)`
* Add import statement for `com.artipie.asto.factory.StoragesLoader` if not already imported.

The reason for this is that the `Storages` class has been removed and replaced with `StoragesLoader` in the new library version. The `newStorage` method has also changed its parameter from `StorageConfig` to `Config`.