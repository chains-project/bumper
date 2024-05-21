Here is the proposed patch:

```java
@java.lang.Override
public com.artipie.security.policy.Policy<?> getPolicy(final com.artipie.security.policy.PolicyConfig config) {
    final com.artipie.security.policy.PolicyConfig sub = config.config("storage");
    try {
        return new com.artipie.security.policy.YamlPolicy(new com.artipie.asto.blocking.BlockingStorage(new com.artipie.asto.Storage.Base(com.artipie.asto.Storage.of(sub.string("type"), context -> new com.amihaiemil.eoyaml.Yaml(context).loadYamlMapping(sub.toString())))]);
    } catch (final java.io.IOException err) {
        throw new java.io.UncheckedIOException(err);
    }
}
```

In this patch, I replaced the usage of `com.artipie.security.policy.Storages` with `com.artipie.asto.Storage.Base` and `com.artipie.asto.Storage.of` to create a new storage. I also replaced the usage of `com.amihaiemil.eoyaml.Yaml.createYamlInput` with `com.amihaiemil.eoyaml.Yaml` to load the YAML mapping. This should fix the error of "cannot find symbol" for `Storages`.