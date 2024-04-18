Here's a proposed patch to fix the error:

```java
@java.lang.Override
public com.artipie.security.policy.Policy<?> getPolicy(final com.artipie.security.policy.PolicyConfig config) {
    final com.artipie.security.policy.PolicyConfig sub = config.config("storage");
    try {
        return new com.artipie.security.policy.YamlPolicy(new com.artipie.asto.blocking.BlockingStorage(new com.artipie.asto.Storage.Default(com.artipie.asto.Async.await(com.artipie.asto.Ext.store(sub.string("type"), com.amihaiemil.eoyaml.Yaml.createYamlInput(sub.toString()).readYamlMapping()))))));
    } catch (final java.io.IOException err) {
        throw new java.io.UncheckedIOException(err);
    }
}
```

In this patch, I replaced the `com.artipie.security.policy.Storages` class with `com.artipie.asto.Storage.Default` and used `com.artipie.asto.Ext.store` method instead of `com.artipie.security.policy.Storages.newStorage` method to create a new storage. This should fix the "cannot find symbol" error.