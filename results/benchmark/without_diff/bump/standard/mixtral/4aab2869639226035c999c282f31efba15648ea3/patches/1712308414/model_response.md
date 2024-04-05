Here's the proposed patch:

```java
@java.lang.Override
public com.artipie.security.policy.Policy<?> getPolicy(final com.artipie.security.policy.PolicyConfig config) {
    final com.artipie.security.policy.PolicyConfig sub = config.config("storage");
    try {
        return new com.artipie.security.policy.YamlPolicy(new com.artipie.asto.blocking.BlockingStorage(new com.artipie.asto.Storage<>(com.artipie.asto.ext.ConfiguredAsync Hawk.class).newStorage(sub.string("type"), com.amihaiemil.eoyaml.Yaml.createYamlInput(sub.toString()).readYamlMapping())));
    } catch (final java.io.IOException err) {
        throw new java.io.UncheckedIOException(err);
    }
}
```

I replaced `com.artipie.security.policy.Storages` with `com.artipie.asto.Storage` and `com.artipie.security.policy.Storages.newStorage` with `com.artipie.asto.Storage.newStorage`. Additionally, I added `com.artipie.asto.ext.ConfiguredAsyncHawk.class` as a type parameter for `com.artipie.asto.Storage`. This should resolve the error.