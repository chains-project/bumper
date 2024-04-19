Here's the updated code that fixes the error:

```java
@Override
public Policy<?> getPolicy(final PolicyConfig config) {
    final PolicyConfig sub = config.config("storage");
    try {
        return new YamlPolicy(new BlockingStorage(new com.artipie.asto.Storage<>(com.artipie.asto.memory.InMemoryKeyValueService.single().memStorage(sub.string("type")), com.amihaiemil.eoyaml.Yaml.createYamlInput(sub.toString()).readYamlMapping()))){};
    } catch (final IOException err) {
        throw new UncheckedIOException(err);
    }
}
```

In this updated code, I replaced the `Storages` class with `com.artipie.asto.Storage` which is an added library method identified with `++`. Additionally, I replaced `com.artipie.security.policy.Storages` with `com.artipie.asto.asto.memory.InMemoryKeyValueService.single().memStorage` which is a new way of creating a storage. I also removed the unnecessary `newStorage` method call and simplified the instantiation of `YamlPolicy` class.