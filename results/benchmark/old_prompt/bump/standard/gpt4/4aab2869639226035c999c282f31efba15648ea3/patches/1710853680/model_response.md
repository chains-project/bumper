It seems like the class `Storages` is not found in the package `com.artipie.security.policy`. It could be that the class has been moved to a different package or it has been renamed. 

Without knowing the exact changes in the dependencies, I'll assume that the class `Storages` has been renamed to `StorageFactory`. Here is the fixed code:

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

Please replace the class `Storages` with the correct one if my assumption is not correct.