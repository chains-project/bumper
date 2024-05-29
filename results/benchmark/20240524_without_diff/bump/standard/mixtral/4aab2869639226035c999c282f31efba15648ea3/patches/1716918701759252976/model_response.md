Here's the proposed patch:

```java
@java.lang.Override
public com.artipie.security.policy.Policy<?> getPolicy(final com.artipie.security.policy.PolicyConfig config) {
    final com.artipie.security.policy.PolicyConfig sub = config.config("storage");
    try {
        return new com.artipie.security.policy.YamlPolicy(new com.artipie.asto.blocking.BlockingStorage(new com.artipie.asto.Storage<>(com.artipie.security.policy.Policy.class, new com.artipie.security.policy.storages.Storages()).newStorage(sub.string("type"), com.amihaiemil.eoyaml.Yaml.createYamlInput(sub.toString()).readYamlMapping())));
    } catch (final java.io.IOException err) {
        throw new java.io.UncheckedIOException(err);
    }
}
```

In this patch, I replaced the removed `com.artipie.security.policy.Storages` class with a fully qualified alternative: `com.artipie.security.policy.storages.Storages`. This assumes that the `storages` package is present in the classpath and contains the necessary `Storages` class. If that's not the case, you may need to adjust the package name accordingly.