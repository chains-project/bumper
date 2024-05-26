Here'1s the updated code that should fix the error:

```java
@java.lang.Override
public com.artipie.security.policy.Policy<?> getPolicy(final com.artipie.security.policy.PolicyConfig config) {
    final com.artipie.security.policy.PolicyConfig sub = config.config("storage");
    try {
        return new com.artipie.security.policy.YamlPolicy(new com.artipie.asto.blocking.BlockingStorage(new com.artipie.asto.Storage.Default(com.artipie.asto.memory.Memory.class).newStorage(sub.string("type"), com.amihaiemil.eoyaml.Yaml.createYamlInput(sub.toString()).readYamlMapping())));
    } catch (final java.io.IOException err) {
        throw new java.io.UncheckedIOException(err);
 }
}
```

In this updated code, I replaced the `com.artipie.security.policy.Storages` class with `com.artipie.asto.Storage.Default(com.artipie.asto.memory.Memory.class)`. This way, we create a `Storage` object using the `Default` constructor and `Memory` class, which should be available in the same package.

Note that this change assumes that the behavior of `com.artipie.security.policy.Storages` is similar to `com.artipie.asto.Storage.Default(com.artipie.asto.memory.Memory.class)`. Adjust the code as needed.