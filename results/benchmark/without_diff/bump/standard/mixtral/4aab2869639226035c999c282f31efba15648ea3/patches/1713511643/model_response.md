Here's a fixed version of the `getPolicy` method. I created a `storages` variable to replace the direct usage of `Storages` class.

```java
@java.lang.Override
public com.artipie.security.policy.Policy<?> getPolicy(final com.artipie.security.policy.PolicyConfig config) {
    final com.artipie.security.policy.PolicyConfig sub = config.config("storage");
    final com.artipie.asto.Storage storage = new com.artipie.security.policy.storages().newStorage(sub.string("type"), com.amihaiemil.eoyaml.Yaml.createYamlInput(sub.toString()).readYamlMapping());
    try {
        return new com.artipie.security.policy.YamlPolicy(new com.artipie.asto.blocking.BlockingStorage(storage));
    } catch (final java.io.IOException err) {
        throw new java.io.UncheckedIOException(err);
    }
}
```

In this updated code, I replaced the line `new com.artipie.security.policy.Storages()` with `new com.artipie.security.policy.storages()`. This change should resolve the "cannot find symbol" error.