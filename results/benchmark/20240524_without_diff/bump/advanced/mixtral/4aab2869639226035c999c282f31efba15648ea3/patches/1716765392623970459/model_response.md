Here's the proposed patch:

```java
@java.lang.Override
public com.artipie.security.policy.Policy<?> getPolicy(final com.artipie.security.policy.PolicyConfig config) {
    final com.artipie.security.policy.PolicyConfig sub = config.config("storage");
    try {
        return new com.artipie.security.policy.YamlPolicy(new com.artipie.asto.blocking.BlockingStorage(new com.artipie.asto.Storage<>(com.artipie.security.policy.PolicyConfigs.storages().newStorage(sub.string("type"), com.amihaiemil.eoyaml.Yaml.createYamlInput(sub.toString()).readYamlMapping()))));
    } catch (final java.io.IOException err) {
        throw new java.io.UncheckedIOException(err);
    }
}
```

The changes include:

* Replace `new com.artipie.security.policy.Storages()` with `com.artipie.security.policy.PolicyConfigs.storages()`, which is a new method added in the external dependency.
* Import the missing class: `import com.artipie.security.policy.PolicyConfigs;`