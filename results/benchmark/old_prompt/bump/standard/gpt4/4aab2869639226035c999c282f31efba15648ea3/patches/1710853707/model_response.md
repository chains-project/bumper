Based on the error message, it seems like the class `Storages` cannot be found. Perhaps the `Storages` class has been moved or renamed in a recent update of the external dependency. Without knowing the exact changes in the external dependency, it's hard to provide a precise solution. However, assuming that `Storages` has been replaced with a new class called `StorageFactory`, here's a potential fix:

```java
@java.lang.Override
public com.artipie.security.policy.Policy<?> getPolicy(final com.artipie.security.policy.PolicyConfig config) {
    final com.artipie.security.policy.PolicyConfig sub = config.config("storage");
    try {
        return new com.artipie.security.policy.YamlPolicy(new com.artipie.asto.blocking.BlockingStorage(new com.artipie.security.policy.StorageFactory().newStorage(sub.string("type"), com.amihaiemil.eoyaml.Yaml.createYamlInput(sub.toString()).readYamlMapping())));
    } catch (final java.io.IOException err) {
        throw new java.io.UncheckedIOException(err);
    }
}
```

In this code, `Storages` is replaced with `StorageFactory`. Please replace `StorageFactory` with the actual class that provides the same functionality as the old `Storages` class.