```java
@java.lang.Override
public com.artipie.security.policy.Policy<?> getPolicy(final com.artipie.security.policy.PolicyConfig config) {
    final com.artipie.security.policy.PolicyConfig sub = config.config("storage");
    try {
        com.artipie.asto.factory.StoragesLoader storagesLoader = new com.artipie.asto.factory.StoragesLoader();
        com.artipie.asto.factory.Config storageConfig = new com.artipie.asto.factory.Config(sub.string("type"), com.amihaiemil.eoyaml.Yaml.createYamlInput(sub.toString()).readYamlMapping());
        return new com.artipie.security.policy.YamlPolicy(new com.artipie.asto.blocking.BlockingStorage(storagesLoader.newObject(sub.string("type"), storageConfig)));
    } catch (final java.io.IOException err) {
        throw new java.io.UncheckedIOException(err);
    }
}
```