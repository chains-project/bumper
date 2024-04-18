Here's a possible patch to fix the error:
```java
@java.lang.Override
public com.artipie.security.policy.Policy<?> getPolicy(final com.artipie.security.policy.PolicyConfig config) {
    final com.artipie.security.policy.PolicyConfig sub = config.config("storage");
    try {
        return new com.artipie.security.policy.YamlPolicy(new com.artipie.asto.blocking.BlockingStorage(new com.artipie.security.policy.Storages() {
            @Override
            public com.artipie.security.policy.Storage newStorage(final String type, final com.amihaiemil.eoyaml.YamlInput yaml) {
                return new com.artipie.security.policy.Storages().newStorage(type, yaml);
            }
        }.newStorage(sub.string("type"), com.amihaiemil.eoyaml.Yaml.createYamlInput(sub.toString()).readYamlMapping())));
    } catch (final java.io.IOException err) {
        throw new java.io.UncheckedIOException(err);
    }
}
```
The patch creates a new anonymous inner class that implements `com.artipie.security.policy.Storages`, and overrides the `newStorage` method to delegate the call to the `com.artipie.security.policy.Storages` instance. This allows the `YamlPolicy` constructor to work even if the `Storages` class is not available.