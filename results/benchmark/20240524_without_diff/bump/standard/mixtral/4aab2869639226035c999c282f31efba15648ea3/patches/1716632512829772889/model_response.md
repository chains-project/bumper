Here'1s a patch for the failing client code, which addresses the error message by using the fully qualified name for the `Storages` class:

```java
@java.lang.Override
public com.artipie.security.policy.Policy<?> getPolicy(final com.artipie.security.policy.PolicyConfig config) {
    final com.artipie.security.policy.PolicyConfig sub = config.config("storage");
    try {
        return new com.artipie.security.policy.YamlPolicy(new com.artipie.asto.blocking.BlockingStorage(new com.artipie.security.policy.package.artipie.asto.BlockingStorage.Storages().newStorage(sub.string("type"), com.amihaiemil.eoyaml.Yaml.createYamlInput(sub.toString()).readYamlMapping())));
    } catch (final java.io.IOException err) {
        throw new java.io.UncheckedIOException(err);
 }
}
```

Note that I've replaced `new com.artipie.security.policy.Storages()` with `new com.artipie.security.policy.package.artipie.asto.BlockingStorage.Storages()` to use the fully qualified name for the `Storages` class.