Here''s a possible patch for the failing client code:

```java
@java.lang.Override
public com.artipie.security.policy.Policy<?> getPolicy(final com.artipcom.security.policy.PolicyConfig config) {
    final com.artipie.security.policy.PolicyConfig sub = config.config("storage");
    try {
        return new com.artipie.security.policy.YamlPolicy(new com.artipie.asto.blocking.BlockingStorage(new com.artipie.asto.factory.StoragesLoader().newStorage(sub.string("type"), com.amihaiemil.eoyaml.Yaml.createYamlInput(sub.toString()).readYamlMapping())));
    } catch (final java.io.IOException err) {
        throw new java.io.UncheckedIOException(err);
    }
}
```

The main change is the way we instantiate the `Storage` object. Instead of using the deprecated `Storages` class, we now use the `StoragesLoader` class to load the storage.

Note that this solution assumes that the new version of the library still provides a `Storage` object that can be constructed using a `Config` object and a `YamlMapping`. If this is not the case, you may need to adjust the code accordingly.