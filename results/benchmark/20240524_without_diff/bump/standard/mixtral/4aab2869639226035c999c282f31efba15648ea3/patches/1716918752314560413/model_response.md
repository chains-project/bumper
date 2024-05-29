Here's the proposed patch for the failing client code:

```java
@java.lang.Override
public com.artipie.security.policy.Policy<?> getPolicy(final com.artipie.security.policy.PolicyConfig config) {
    final com.artipie.security.policy.PolicyConfig sub = config.config("storage");
    try {
        return new com.artipie.security.policy.YamlPolicy(new com.artipie.asto.blocking.BlockingStorage(new com.artipie.asto.Storage<>(new com.artipie.asto.memory.InMemoryKeyValueStore()), com.amihaiemil.eoyaml.Yaml.createYamlInput(sub.toString()).readYamlMapping())));
    } catch (final java.io.IOException err) {
        throw new java.io.UncheckedIOException(err);
    }
}
```

In this patch, I replaced the `com.artipie.security.policy.Storages` class with `com.artipie.asto.Storage` and used `com.artipie.asto.memory.InMemoryKeyValueStore` as the implementation of `com.artipie.asto.Storage`. This should fix the error caused by the missing `Storages` class.