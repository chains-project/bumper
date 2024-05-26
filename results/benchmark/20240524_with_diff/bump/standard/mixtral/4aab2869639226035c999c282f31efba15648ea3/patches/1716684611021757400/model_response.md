Here is a possible patch for the failing client code:
```java
@java.lang.Override
public com.artipie.security.policy.Policy<?> getPolicy(final com.artipie.security.policy.PolicyConfig config) {
    final com.artipie.security.policy.PolicyConfig sub = config.config("storage");
    try {
        com.artipie.asto.Storage storage = new com.artipie.asto.fs.FileStorageFactory().newStorage(new com.artipie.asto.KeyedInputStream<>(sub.string("type"), com.amihaiemil.eoyaml.Yaml.createYamlInput(sub.toString()).readYamlMapping()));
        return new com.artipie.security.policy.YamlPolicy(storage);
    } catch (final java.io.IOException err) {
        throw new java.io.UncheckedIOException(err);
 }
}
```
The main changes are:

* Instead of using `com.artipie.asto.factory.Storages.newStorage`, which has been removed, we use `com.artip
ie.asto.fs.FileStorageFactory.newStorage` to create a `com.artipie.asto.Storage` instance.
* We use a `com.artipie.asto.KeyedInputStream` to wrap the YAML mapping and pass it to the `FileStorageFactory.newStorage` method.
* We no longer need to extract the storage type from the YAML mapping manually, as the `FileStorageFactory.newStorage` method can handle it for us.