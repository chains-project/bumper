Here's a possible patch to fix the error:
```java
@java.lang.Override
public com.artipie.security.policy.Policy<?> getPolicy(final com.artipie.security.policy.PolicyConfig config) {
    final com.artipie.security.policy.PolicyConfig sub = config.config("storage");
    try {
        return new com.artipie.security.policy.YamlPolicy(new com.artipie.asto.blocking.BlockingStorage(new com.artipie.security.policy.Storages() {
            @Override
            public com.artipie.security.policy.Storage newStorage(final String type, final com.amihaiemil.eoyaml.YamlInput yaml) {
                return new com.artipie.security.policy.YamlStorage(type, yaml);
            }
        }.newStorage(sub.string("type"), com.amihaiemil.eoyaml.Yaml.createYamlInput(sub.toString()).readYamlMapping())));
    } catch (final java.io.IOException err) {
        throw new java.io.UncheckedIOException(err);
    }
}
```
The patch creates a new anonymous class that implements `com.artipie.security.policy.Storages`, which provides a custom implementation of the `newStorage` method that returns an instance of `com.artipie.security.policy.YamlStorage`. This allows the code to compile without the need for the `Storages` class.