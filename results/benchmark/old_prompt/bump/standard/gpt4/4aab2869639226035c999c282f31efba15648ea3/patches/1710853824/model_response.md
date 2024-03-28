It seems like the class `Storages` is not found in the package `com.artipie.security.policy`. If the `Storages` class is removed or its location is changed, you need to replace it with the correct class or method to create a new storage. Here is a patch assuming that a method `createStorage` exists in the `PolicyConfig` class that accepts the same parameters:

```java
@java.lang.Override
public com.artipie.security.policy.Policy<?> getPolicy(final com.artipie.security.policy.PolicyConfig config) {
    final com.artipie.security.policy.PolicyConfig sub = config.config("storage");
    try {
        return new com.artipie.security.policy.YamlPolicy(new com.artipie.asto.blocking.BlockingStorage(sub.createStorage(sub.string("type"), com.amihaiemil.eoyaml.Yaml.createYamlInput(sub.toString()).readYamlMapping())));
    } catch (final java.io.IOException err) {
        throw new java.io.UncheckedIOException(err);
    }
}
```
This patch replaces the missing `Storages` class with a hypothetical `createStorage` method in the `PolicyConfig` class. Check your `PolicyConfig` class for the correct method to create a new storage.