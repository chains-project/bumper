Here's a proposed patch for the failing client code:

```java
@java.lang.Override
public com.artipie.security.policy.Policy<?> getPolicy(final com.artipie.security.policy.PolicyConfig config) {
    final com.artipie.security.policy.PolicyConfig sub = config.config("storage");
    try {
        return new com.artipie.security.policy.YamlPolicy(new com.artipie.asto.blocking.BlockingStorage(new com.artipie.asto.Storage.Default(com.artipie.asto.Async.defaultAsync(), com.artipie.asto.Containers.empty(), new com.artipie.asto.memory.InMemoryKeyValue.InMemoryKV(com.artipie.asto.misc.Converters.stringConverter()))).newStorage(sub.string("type"), com.amihaiemil.eoyaml.Yaml.createYamlInput(sub.toString()).readYamlMapping()));
    } catch (final java.io.IOException err) {
        throw new java.io.UncheckedIOException(err);
    }
}
```

In this patch, I replaced the `com.artipie.security.policy.Storages` class with `com.artipie.asto.Storage.Default` class, which provides similar functionality. I also replaced the `com.artipie.security.policy.Storages.newStorage` method with `com.artipie.asto.Storage.Default.newStorage` method. Additionally, I added three new classes to create a default `com.artipie.asto.Storage` instance: `com.artipie.asto.Async.Default`, `com.artipie.asto.Containers.empty()`, and `com.artipie.asto.memory.InMemoryKeyValue.InMemoryKV`. These classes are used to create a default `com.artipie.asto.Storage` instance, which is then used to create a new storage for the `com.artipie.security.policy.YamlPolicy` instance.