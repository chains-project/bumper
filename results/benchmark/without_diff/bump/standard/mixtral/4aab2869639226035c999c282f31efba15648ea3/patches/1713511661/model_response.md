Here is a potential patch for the given code:
```java
@java.lang.Override
public com.artipie.security.policy.Policy<?> getPolicy(final com.artipie.security.policy.PolicyConfig config) {
    final com.artipie.security.policy.PolicyConfig sub = config.config("storage");
    try {
        return new com.artipie.security.policy.YamlPolicy(new com.artipie.asto.blocking.BlockingStorage(new com.artipie.asto.Storage<>(com.amihaiemil.eoyaml.Yaml.createYamlInput(sub.toString()).readYamlMapping()), sub.string("type")));
    } catch (final java.io.IOException err) {
        throw new java.io.UncheckedIOException(err);
    }
}
```
I replaced the `com.artipie.security.policy.Storages` class with `com.artipie.asto.Storage` class, and passed the `Yaml` mapping as the first parameter and the `type` as the second parameter to the `Storage` constructor. This should fix the error you were encountering.