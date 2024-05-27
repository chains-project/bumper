Here's the proposed patch:

```java
@Override
public Policy<?> getPolicy(final PolicyConfig config) {
    final PolicyConfig sub = config.config("storage");
    try {
        return new YamlPolicy(new BlockingStorage(new com.artipie.asto.storage.Storage(sub.string("type"), com.amihaiemil.eoyaml.Yaml.createYamlInput(sub.toString()).readYamlMapping())));
    } catch (final IOException err) {
        throw new UncheckedIOException(err);
    }
}
```

The changes include:

* Replace `com.artipie.security.policy.Storages` with `com.artipie.asto.storage.Storage`
* Replace `com.artipie.security.policy.Storages().newStorage(sub.string("type"), com.amihaiemil.eoyaml.Yaml.createYamlInput(sub.toString()).readYamlMapping())` with `new com.artipie.asto.storage.Storage(sub.string("type"), com.amihaiemil.eoyaml.Yaml.createYamlInput(sub.toString()).readYamlMapping())`
* Replace `new com.artipie.asto.blocking.BlockingStorage` with `new BlockingStorage`
* Replace `com.artipie.security.policy.YamlPolicy` with `YamlPolicy`
* Replace `java.io.IOException` with `IOException`
* Replace `java.io.UncheckedIOException` with `UncheckedIOException`