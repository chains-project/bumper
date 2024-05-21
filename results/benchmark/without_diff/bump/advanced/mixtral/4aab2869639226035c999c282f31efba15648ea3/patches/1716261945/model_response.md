Here's the proposed patch:

```java
@java.lang.Override
public com.artipie.security.policy.Policy<?> getPolicy(final com.artipie.security.policy.PolicyConfig config) {
    final com.artipie.security.policy.PolicyConfig sub = config.config("storage");
    try {
        return new com.artipie.security.policy.YamlPolicy(new com.artipie.asto.blocking.BlockingStorage(new com.artipie.asto.Storage(com.artipie.asto.Containers.memory(), sub.string("type"), com.amihaiemil.eoyaml.Yaml.createYamlInput(sub.toString()).readYamlMapping())));
    } catch (final java.io.IOException err) {
        throw new java.io.UncheckedIOException(err);
    }
}
```

The change is to replace the `com.artipie.security.policy.Storages` class, which seems to be missing, with `com.artipie.asto.Storage`. I also replaced `com.artipie.security.policy.Storages.newStorage` with `com.artipie.asto.Containers.memory`. This way, the code is now using available classes and methods.