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

The patch creates a `Default` `Storage` instance using `MemFS` instead of the missing `Storages` class. Additionally, the `InvocationTargetException` is added to the `catch` block to handle any exceptions thrown during the constructor invocation.