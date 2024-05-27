Here's the proposed patch:

```java
@java.lang.Override
public com.artipie.security.policy.Policy<?> getPolicy(final com.artipie.security.policy.PolicyConfig config) {
    final com.artipie.security.policy.PolicyConfig sub = config.config("storage");
    try {
        return new com.artipie.security.policy.YamlPolicy(new com.artipie.asto.blocking.BlockingStorage(new com.artipie.asto.Storage.Default(com.artipie.asto.Async.defaultAsync(), com.artipie.asto.Containers.empty(), new com.artipie.asto.StorageWrapper.Simple(sub.string("type"),
                com.amihaiemil.eoyaml.Yaml.createYamlInput(sub.toString()).readYamlMapping()))));
    } catch (final java.io.IOException err) {
        throw new java.io.UncheckedIOException(err);
    }
}
```

I changed the line that creates the `Storage` object by using `com.artipie.asto.Storage.Default` instead of `com.artipie.security.policy.Storages`. This should fix the error you're encountering.