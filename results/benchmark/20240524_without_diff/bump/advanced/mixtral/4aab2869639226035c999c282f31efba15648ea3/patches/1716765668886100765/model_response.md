Here's the proposed patch:

```java
@java.lang.Override
public com.artipie.security.policy.Policy<?> getPolicy(final com.artipie.security.policy.PolicyConfig config) {
    final com.artipie.security.policy.PolicyConfig sub = config.config("storage");
    try {
        return new com.artipie.security.policy.YamlPolicy(new com.artipie.asto.blocking.BlockingStorage(new com.artipie.asto.Storage.Default(com.artipie.asto.ext.MemFS.class.getDeclaredConstructor().newInstance()), com.amihaiemil.eoyaml.Yaml.createYamlInput(sub.toString()).readYamlMapping())));
    } catch (final java.io.IOException | java.lang.reflect.InvocationTargetException err) {
        throw new java.io.UncheckedIOException(err);
    }
}
```

In this patch, I replaced the `com.artipie.security.policy.Storages` class with `com.artipie.asto.Storage.Default`, and used `com.artipie.asto.ext.MemFS` to create a default storage. The `com.artipie.asto.ext.MemFS` class provides an in-memory file system implementation, which can be used as a replacement for the external dependency.