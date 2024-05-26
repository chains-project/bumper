Here is the updated code that uses `StoragesLoader` instead of `Starts`:
```java
@java.lang.Override
public com.artipie.security.policy.Policy<?> getPolicy(final com.artipie.security.policy.PolicyConfig config) {
    final com.artipie.security.policy.PolicyConfig sub = config.config("storage");
    try {
        com.artipie.asto.Storage storage = new com.artipie.asto.factory.StoragesLoader().newObject(sub.string("type"), new com.artipie.asto.factory.Yaml().load(com.amihaiemil.eoyaml.Yaml.createYamlInput(sub.toString()).readYamlMapping()));
        return new com.artipie.security.policy.YamlPolicy(new com.artipie.asto.blocking.BlockingStorage(storage));
    } catch (final java.io.IOException err) {
        throw new java.io.UncheckedIOException(err);
   :    }
}
```
I created a new variable `storage` to make the code a bit easier to understand.
The `StorgesLoader` is used to create a `Storage` object with the given type and configuration.
The `Yaml` class is used to parse the configuration.
The `BlockingStorage` is used to wrap the `Storage` object.
The `YamlPolicy` is used to create a new `Policy` object with the `BlockingStorage`.