Here's a fixed version of the `getPolicy` method. I replaced the usage of `com.artipie.security.policy.Storages` with `com.artipie.asto.ext.Storages`, which is likely the class you meant to use:

```java
@java.lang.Override
public com.artipie.security.policy.Policy<?> getPolicy(final com.artipie.security.policy.PolicyConfig config) {
    final com.artipie.security.policy.PolicyConfig sub = config.config("storage");
    try {
        return new com.artipie.security.policy.YamlPolicy(new com.artipie.asto.blocking.BlockingStorage(new com.artipie.asto.ext.Storages().newStorage(sub.string("type"), com.amihaiemil.eoyaml.Yaml.createYamlInput(sub.toString()).readYamlMapping())));
    } catch (final java.io.IOException err) {
        throw new java.io.UncheckedIOException(err);
    }
}
```

Please note that I cannot guarantee this will solve your issue, as I don't have the full context of your codebase and dependencies. However, this should resolve the compilation error you provided.