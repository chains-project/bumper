Here's the proposed patch:

```java
@java.lang.Override
public com.artipie.security.policy.Policy<?> getPolicy(final com.artipie.security.policy.PolicyConfig config) {
    final com.artipie.security.policy.PolicyConfig sub = config.config("storage");
    try {
        return new com.artipie.security.policy.YamlPolicy(new com.artipie.asto.blocking.BlockingStorage(new com.artipie.asto.Storage<>(com.artipie.asto.ext.Extensions.storage(sub.string("type")), com.amihaiemil.eoyaml.Yaml.createYamlInput(sub.toString()).readYamlMapping())));
    } catch (final java.io.IOException err) {
        throw new java.io.UncheckedIOException(err);
    }
}
```

The change is to replace `new Storage(com.artipie.security.policy.Storages().newStorage(sub.string("type")), ...)` with `new Storage<>(com.artipie.asto.ext.Extensions.storage(sub.string("type")), ...)`. This is because the `Storages` class has been removed and replaced with the `com.artipie.asto.ext.Extensions.storage()` method in the external dependency.