Here's a possible patch to fix the error:
```java
@java.lang.Override
public com.artipie.security.policy.Policy<?> getPolicy(final com.artipie.security.policy.PolicyConfig config) {
    final com.artipie.security.policy.PolicyConfig sub = config.config("storage");
    try {
        com.amihaiemil.eoyaml.Yaml yaml = com.amihaiemil.eoyaml.Yaml.createYamlInput(sub.toString());
        return new com.artipie.security.policy.YamlPolicy(new com.artipie.asto.blocking.BlockingStorage(new com.artipie.security.policy.Storages(yaml.readYamlMapping())));
    } catch (final java.io.IOException err) {
        throw new java.io.UncheckedIOException(err);
    }
}
```
The patch creates a `com.amihaiemil.eoyaml.Yaml` instance from the `sub.toString()` representation of the `PolicyConfig` object, and then uses it to read a `YamlMapping` object, which is then passed to the `Storages` constructor to create a new `BlockingStorage` instance.

Note that this patch assumes that the `Storages` class is available in the same package as the `YamlPolicyFactory` class. If that's not the case, you may need to adjust the patch accordingly.