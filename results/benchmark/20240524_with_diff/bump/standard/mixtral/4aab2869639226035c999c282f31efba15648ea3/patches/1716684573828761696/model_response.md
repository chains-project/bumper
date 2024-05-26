Here is the updated code that should fix the error:

```java
@java.lang.Override
public com.artipie.security.policy.Policy<?> getPolicy(final com.artipie.security.policy.PolicyConfig config) {
    final com.artipie.security.policy.PolicyConfig sub = config.config("storage");
    try {
        return new com.artipie.security.policy.YamlPolicy(new com.artipie.asto.blocking.BlockingStorage(new com.artipie.asto.factory.StoragesLoader().newObject(sub.string("type"), com.amihaiemil.eoyaml.Yaml.createYamlInput(sub.toString()).readYamlMapping())));
    } catch (final java.io.IOException err) {
        throw new java.io.UncheckedIOException(err);
  }
}
```

The main change is the way we create a `Storage` object. Instead of using `newStorage` method on `Storages` object, we now use the `newObject` method on `StoragesLoader` object. This is because the `Storages` class has been removed and replaced with `StoragesLoader` in the new library version.

Note that the `newObject` method takes a `String` and a `YamlMapping` as arguments, just like the `newStorage` method did. This means that we can use the same code to create the `YamlMapping` object as before.

Also, note that the `StorageConfig` class has been replaced with a more generic `Config` class. This means that we can still use the same `Config` object that we were using before.

Finally, note that the `StoragesLoader` object needs to be instantiated using its default constructor or using a `Map` as an argument. In this case, we are using the default constructor.