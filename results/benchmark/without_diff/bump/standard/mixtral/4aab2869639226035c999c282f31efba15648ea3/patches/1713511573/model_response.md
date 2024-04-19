Here's a fixed version of the `getPolicy` method. I changed `com.artipie.security.policy.Storages` to `com.artipie.asto.Storage` as the former seems to be removed:

```java
@java.lang.Override
public com.artipie.security.policy.Policy<?> getPolicy(final com.artipie.security.policy.PolicyConfig config) {
    final com.artipie.security.policy.PolicyConfig sub = config.config("storage");
    try {
        return new com.artipie.security.policy.YamlPolicy(new com.artipie.asto.blocking.BlockingStorage(new com.artipie.asto.Storage.DefaultStorage(sub.string("type"), com.amihaiemil.eoyaml.Yaml.createYamlInput(sub.toString()).readYamlMapping())));
    } catch (final java.io.IOException err) {
        throw new java.io.UncheckedIOException(err);
    }
}
```

This code uses `com.artipie.asto.Storage.DefaultStorage` instead of `com.artipie.security.policy.Storages`. The `DefaultStorage` class can be found in the `artipie-asto` library, which has been added according to the `++` notation.