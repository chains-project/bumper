Here's a fixed version of the method using the fully qualified name for `Storages`:

```java
@Override
public Policy<?> getPolicy(final PolicyConfig config) {
    final PolicyConfig sub = config.config("storage");
    try {
        return new YamlPolicy(new BlockingStorage(new com.artipie.asto.storage.Storages().newStorage(sub.string("type"), com.amihaiemil.eoyaml.Yaml.createYamlInput(sub.toString()).readYamlMapping())));
    } catch (final java.io.IOException err) {
        throw new java.io.UncheckedIOException(err);
    }
}
```

I replaced `new com.artipie.security.policy.Storages()` with `new com.artipie.asto.storage.Storages()`.