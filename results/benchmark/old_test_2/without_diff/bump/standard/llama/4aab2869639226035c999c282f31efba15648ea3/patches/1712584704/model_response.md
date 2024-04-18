Here's a possible patch to fix the error:
```java
@java.lang.Override
public com.artipie.security.policy.Policy<?> getPolicy(final com.artipie.security.policy.PolicyConfig config) {
    final com.artipie.security.policy.PolicyConfig sub = config.config("storage");
    try {
        final com.amihaiemil.eoyaml.Yaml yaml = com.amihaiemil.eoyaml.Yaml.createYamlInput(sub.toString());
        return new com.artipie.security.policy.YamlPolicy(new com.artipie.asto.blocking.BlockingStorage(new com.artipie.security.policy.Storages() {
            @Override
            public com.artipie.security.policy.Storage createStorage(final String type) {
                return new com.artipie.security.policy.YamlStorage(yaml.readYamlMapping());
            }
        }.newStorage(sub.string("type"))));
    } catch (final java.io.IOException err) {
        throw new java.io.UncheckedIOException(err);
    }
}
```
The patch creates a new `YamlStorage` instance using the `Yaml` instance created from the configuration string, and passes it to the `BlockingStorage` constructor. This allows the `YamlPolicy` constructor to work without the need for the `Storages` class.

Note that this patch assumes that the `Yaml` instance can correctly parse the configuration string and create a valid `YamlMapping` object. If this is not the case, additional changes may be needed to handle invalid configuration strings.