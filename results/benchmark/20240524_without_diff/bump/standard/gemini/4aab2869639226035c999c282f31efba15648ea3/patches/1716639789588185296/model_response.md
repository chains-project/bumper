```java
@java.lang.Override
public com.artipie.security.policy.Policy<?> getPolicy(final com.artipie.security.policy.PolicyConfig config) {
    final com.artipie.security.policy.PolicyConfig sub = config.config("storage");
    try {
        final com.amihaiemil.eoyaml.YamlMapping mapping = com.amihaiemil.eoyaml.Yaml.createYamlInput(sub.toString()).readYamlMapping();
        final com.artipie.asto.Storage storage = new com.artipie.asto.memory.InMemoryStorage();
        if (mapping.value("type").asScalar().string().equals("file")) {
            storage.save(mapping.value("path").asScalar().string(), mapping.value("data").asBinary());
        }
        return new com.artipie.security.policy.YamlPolicy(storage);
    } catch (final java.io.IOException err) {
        throw new java.io.UncheckedIOException(err);
    }
}
```