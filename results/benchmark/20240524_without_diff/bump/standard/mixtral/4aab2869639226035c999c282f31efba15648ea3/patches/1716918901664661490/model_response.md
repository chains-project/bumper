Here's the proposed patch:

```java
@java.lang.Override
public com.artipie.security.policy.Policy<?> getPolicy(final com.artipie.security.policy.PolicyConfig config) {
    final com.artipie.security.policy.PolicyConfig sub = config.config("storage");
    try {
        return new com.artipie.security.policy.YamlPolicy(new com.artipie.asto.blocking.BlockingStorage(new com.artipie.asto.Storage<>(new com.artipie.asto.memory.InMemoryStorage()::new, sub.string("type"), com.amihaiemil.eoyaml.Yaml.createYamlInput(sub.toString()).readYamlMapping())));
    } catch (final java.io.IOException err) {
        throw new java.io.UncheckedIOException(err);
    }
}
```

The change is to replace the `com.artipie.security.policy.Storages` class with a new `com.artipie.asto.Storage` instance created using the `com.artipie.asto.memory.InMemoryStorage` class. This should fix the error by removing the dependency on the `Storages` class.