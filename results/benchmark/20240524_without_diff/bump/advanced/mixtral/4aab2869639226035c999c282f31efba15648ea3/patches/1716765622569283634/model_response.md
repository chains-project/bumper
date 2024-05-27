Here's a fixed version of the method that replaces the usage of `com.artipie.security.policy.Storages` with the fully qualified name `com.artipie.asto.Storage`:

```java
@java.lang.Override
public com.artipie.security.policy.Policy<?> getPolicy(final com.artipie.security.policy.PolicyConfig config) {
    final com.artipie.security.policy.PolicyConfig sub = config.config("storage");
    try {
        return new com.artipie.security.policy.YamlPolicy(new com.artipie.asto.blocking.BlockingStorage(new com.artipie.asto.Storage.Default(sub.string("type"), com.amihaiemil.eoyaml.Yaml.createYamlInput(sub.toString()).readYamlMapping())));
    } catch (final java.io.IOException err) {
        throw new java.io.UncheckedIOException(err);
    }
}
```

Note that I also changed the constructor call for `com.artipie.asto.Storage` to `com.artipie.asto.Storage.Default` since the former is deprecated.