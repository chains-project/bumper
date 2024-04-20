Here's a possible patch for the failing client code:

```java
@java.lang.Override
public com.artipie.security.policy.Policy<?> getPolicy(final com.artipie.security.policy.PolicyConfig config) {
    final com.artipie.security.policy.PolicyConfig sub = config.config("storage");
    try {
        StoragesLoader storagesLoader = new com.artipie.asto.factory.StoragesLoader();
        return new com.artipie.security.policy.YamlPolicy(new com.artipie.asto.blocking.BlockingStorage(storagesLoader.newStorage(sub.string("type"), com.amihaiemil.eoyaml.Yaml.createYamlInput(sub.toString()).readYamlMapping())));
    } catch (final java.io.IOException err) {
        throw new java.io.UncheckedIOException(err);
    }
}
```

In this patch, I changed the way the `Storage` object is created. Instead of using the `Storages` class, which has been removed in the new library version, I used the `StoragesLoader` class, which can be used to create `Storage` objects.

Note that this patch assumes that the `Storage` objects can be created using the default package (`com.artipie.asto.factory`), which is the package returned by the `defPackage()` method of the `StoragesLoader` class. If the `Storage` objects need to be created using a different package, you may need to modify the `StoragesLoader` constructor accordingly.