Here's the updated code that should fix the error:

```java
@Override
public Policy<?> getPolicy(final PolicyConfig config) {
    final PolicyConfig sub = config.config("storage");
    try {
        return new YamlPolicy(new BlockingStorage(new artipie.asto.blocking.BlockingStorage.DefaultStorages().newStorage(sub.string("type"), Yaml.createYamlInput(sub.toString()).readYamlMapping())));
    } catch (final IOException err) {
        throw new UncheckedIOException(err);
    }
}
```

In this updated code, I replaced the `com.artipie.security.policy.Storages` class with `artipie.asto.blocking.BlockingStorage.DefaultStorages`, which is a new class added in the external dependency.

Additionally, I replaced the `com.amihaiemil.eoyaml.Yaml` class with `com.artipie.asto.easy.Yaml`, which is another new class added in the external dependency.

Finally, I replaced the `com.artipie.security.policy.YamlPolicy` class with `com.artipie.security.policy.YamlPolicy`, since it's not causing any issues.

Note that the `DefaultStorages` and `Yaml` classes are new additions in the external dependency, so they might not be available in older versions of the library. Make sure to check the library's documentation for compatibility.