```java
@java.lang.Override
public com.artipie.security.policy.Policy<?> getPolicy(final com.artipie.security.policy.PolicyConfig config) {
    final com.artipie.security.policy.PolicyConfig sub = config.config("storage");
    try {
        final com.amihaiemil.eoyaml.YamlMapping mapping = com.amihaiemil.eoyaml.Yaml.createYamlInput(sub.toString()).readYamlMapping();
        final com.artipie.asto.Storage storage = new com.artipie.security.policy.Storages().newStorage(sub.string("type"), mapping);
        return new com.artipie.security.policy.YamlPolicy(new com.artipie.asto.blocking.BlockingStorage(storage));
    } catch (final java.io.IOException err) {
        throw new java.io.UncheckedIOException(err);
    }
}
```