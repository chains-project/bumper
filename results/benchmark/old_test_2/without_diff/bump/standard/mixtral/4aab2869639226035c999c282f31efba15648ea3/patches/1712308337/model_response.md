Here is a fixed version of the code, addressing the "cannot find symbol" error related to the `Storages` class:

```java
@java.lang.Override
public com.artipie.security.policy.Policy<?> getPolicy(final com.artipie.security.policy.PolicyConfig config) {
    final com.artipie.security.policy.PolicyConfig sub = config.config("storage");
    try {
        return new com.artipie.security.policy.YamlPolicy(new com.artipie.asto.blocking.BlockingStorage(new com.artipie.asto.Storage<>(com.artipie.asto.ext.Extensions.storage(sub.string("type")), com.amihaiemil.eoyaml.Yaml.createYamlInput(sub.toString()).readYamlMapping()))));
    } catch (final java.io.IOException err) {
        throw new java.io.UncheckedIOException(err);
    }
}
```

The change is using `com.artipie.asto.Storage` instead of `com.artipie.security.policy.Storages`. The `Storage` class provides similar functionality, allowing you to create a new storage with the specified type and yaml mapping.