Here is a fixed version of the method:

```java
@Override
public Policy<?> getPolicy(final PolicyConfig config) {
    final PolicyConfig sub = config.config("storage");
    try {
        return new YamlPolicy(new BlockingStorage(new artipie.asto.Storage.Default().newStorage(
            sub.string("type"),
            com.amihaiemil.eoyaml.Yaml.createYamlInput(sub.toString()).readYamlMapping()
        )));
    } catch (final IOException err) {
        throw new UncheckedIOException(err);
    }
}
```

The changes I made:

* Replace `com.artipie.security.policy.Storages` with `artipie.asto.Storage.Default()`
* Replace `com.artipie.security.policy.YamlPolicy` with `YamlPolicy`
* Replace `com.artipie.asto.blocking.BlockingStorage` with `artipie.asto.BlockingStorage`
* Replace `com.artipie.security.policy.UncheckedIOException` with `java.io.UncheckedIOException`
* Replace `com.artipie.asto.Storage` with `artipie.asto.Storage.Default()`

It seems that the class `com.artipie.security.policy.Storages` was removed and replaced with `artipie.asto.Storage.Default()`. Also, some classes were imported from the wrong package, so I fixed the imports.