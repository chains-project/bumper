Here's a possible patch to fix the error:
```diff
@java.lang.Override
public com.artipie.security.policy.Policy<?> getPolicy(final com.artipie.security.policy.PolicyConfig config) {
    final com.artipie.security.policy.PolicyConfig sub = config.config("storage");
    try {
        return new com.artipie.security.policy.YamlPolicy(new com.artipie.asto.blocking.BlockingStorage(new com.artipie.security.policy.StoragesLoader().newStorage(sub.string("type"), com.amihaiemil.eoyaml.Yaml.createYamlInput(sub.toString()).readYamlMapping())));
    } catch (final java.io.IOException err) {
        throw new java.io.UncheckedIOException(err);
    }
}
```
The patch removes the usage of `com.artipie.asto.factory.Storages` and instead uses `com.artipie.asto.factory.StoragesLoader` to create the `BlockingStorage` instance.

The `StoragesLoader` class is a new addition in the updated library version, which provides a way to load storage instances from the configured storage factory.

With this patch, the code should now compile and work as expected.