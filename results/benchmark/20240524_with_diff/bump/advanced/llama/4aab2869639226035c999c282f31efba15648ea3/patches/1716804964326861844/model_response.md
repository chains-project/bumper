```java
@java.lang.Override
public com.artipie.security.policy.Policy<?> getPolicy(final com.artipie.security.policy.PolicyConfig config) {
    final com.artipie.security.policy.PolicyConfig sub = config.config("storage");
    try {
        com.amihaiemil.eoyaml.YamlMapping yamlMapping = com.amihaiemil.eoyaml.Yaml.createYamlInput(sub.toString()).readYamlMapping();
        com.artipie.asto.Storage storage = com.artipie.asto.factory.Storages.newStorage(sub.string("type"), yamlMapping);
        return new com.artipie.security.policy.YamlPolicy(new com.artipie.asto.blocking.BlockingStorage(storage));
    } catch (final java.io.IOException err) {
        throw new java.io.UncheckedIOException(err);
    }
}
```