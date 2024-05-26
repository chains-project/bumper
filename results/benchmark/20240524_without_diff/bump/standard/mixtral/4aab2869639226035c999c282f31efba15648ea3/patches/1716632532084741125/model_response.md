Here'1s a possible fix for the given client code:
```java
@java.lang.Override
public com.artipie.security.policy.Policy<?> getPolicy(final com.artipie.security.policy.PolicyConfig config) {
    final com.artipie.security.policy.PolicyConfig sub = config.config("storage");
    try {
        return new com.artipie.security.policy.YamlPolicy(new com.artipie.asto.blocking.BlockingStorage(new com.artipie.asto.Storage.Default(com.artipie.asto.Either.right(new com.artipie.asto.memory.InMemoryAsync()), com.artip.asto.Tarball.class.getName()), com.amihaiemil.eoyaml.Yaml.createYamlInput(sub.toString()).readYamlMapping()));
    } catch (final java.io.IOException err) {
        throw new java.io.UncheckedIOException(err);
    }
}
```
In this updated code, I replaced the `com.artipie.security.policy.Storages` class with a new `com.artipie.asto.Storage.Default` object, which wraps an `com.artipie.asto.InMemoryAsync` object and implements the `com.artipie.asto.Storage` interface.

Note that this is just one possible way to fix the issue, and there might be other ways to solve it as well.

In addition, please note that the `com.artip.asto.Tarball.class.getName()` is used as a parameter for the `com.artipie.asto.Storage.Default` constructor, which is not used in the original code. You might need to adjust it based on your specific use case.