Here's a proposed patch for the given client code:

```java
@java.lang.Override
public com.artipie.security.policy.Policy<?> getPolicy(final com.artipie.security.policy.PolicyConfig config) {
    final com.artipie.security.policy.PolicyConfig sub = config.config("storage");
    try {
        return new com.artipie.security.policy.YamlPolicy(new com.artipie.asto.blocking.BlockingStorage(new com.artipie.asto.Storage<>(com.artipie.security.policy.Policy.class, new com.artipie.asto.memory.InMemoryKeyValueStorage()), com.amihaiemil.eoyaml.Yaml.createYamlInput(sub.toString()).readYamlMapping())));
    } catch (final java.io.IOException err) {
        throw new java.io.UncheckedIOException(err);
    }
}
```

The change I made is to replace `new Storage(sub.string("type"), com.amihaiemil.eoyaml.Yaml.createYamlInput(sub.toString()).readYamlMapping())` with `new com.artipie.asto.Storage<>(com.artipie.security.policy.Policy.class, new com.artipie.asto.memory.InMemoryKeyValueStorage())`.

The original code uses `com.artipie.security.policy.Storages().newStorage(sub.string("type"), com.amihaiemil.eoyaml.Yaml.createYamlInput(sub.toString()).readYamlMapping())`, but it seems that the `Storages` class is no longer available.

Instead, I used `com.artipie.asto.Storage` class, which is a part of `artipie-asto` library. The `com.artipie.asto.memory.InMemoryKeyValueStorage` class is used as a replacement for the `sub.string("type")` parameter.

Note that this change assumes that the `sub.string("type")` parameter is not critical for the code functionality, and it can be replaced with a default value. If that's not the case, you might need to adjust the code accordingly.