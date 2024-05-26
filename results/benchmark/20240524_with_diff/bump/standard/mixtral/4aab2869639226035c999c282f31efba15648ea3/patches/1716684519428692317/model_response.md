Here'UDCFE the updated code for the `getPolicy` method that takes into account the changes in the new library version:
```java
@java.lang.Override
public com.artipie.security.policy.Policy<?> getPolicy(final com.artipie.security.policy.PolicyConfig config) {
    final com.artipie.security.policy.PolicyConfig sub = config.config("storage");
    try {
        com.artipie.asto.Storage storage = new com.artipie.asto.factory.StoragesLoader().newObject(sub.string("type"), new com.artipie.asto.factory.Params(com.amihaiemil.eoyaml.Yaml.createYamlInput(sub.toString()).readYamlMapping()));
        return new com.artipie.security.policy.YamlPolicy(new com.artipie.asto.blocking.BlockingStorage(storage));
    } catch (final java.io.IOException err) {
        throw new java.io.UncheckedIOException(err);
    }
}
```
The main changes are:

* We're using `com.artipie.asto.factory.StoragesLoader` instead of `com.artipie.asto.factory.Storages` to create a new storage.
* We' Instead of passing `com.artipie.asto.factory.StorageConfig`, we're now passing `com.artip yie.asto.factory.Config` to the `newObject` method.
* We're using `com.artipie.asto.factory.Params` to wrap the `com.amihaiemil.eoyaml.YamlMapping` from the configuration.
* The `newStorage` method has been removed from `com.artipie.asto.factory.StorageFactory`, so we've updated the code to use the new `newObject` method from `com.artipie.asto.factory.StoragesLoader` instead.
* The `newStorage` method from `com.artipie.asto.factory.Storages` has been removed, so we've updated the code to use the new `newObject` method from `com.artipie.asto.factory.StoragesLoader` instead.
* The `type` field in the `com.artipie.security.policy.PolicyConfig` is now expected to contain the fully qualified class name of the storage, instead of just the type.