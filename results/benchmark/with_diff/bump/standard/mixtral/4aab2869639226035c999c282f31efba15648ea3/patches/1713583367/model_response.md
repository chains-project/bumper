Here's a possible patch for the failing client code:
```java
@java.lang.Override
public com.artipie.security.policy.Policy<?> getPolicy(final com.artipie.security.policy.PolicyConfig config) {
    final com.artipie.security.policy.PolicyConfig sub = config.config("storage");
    try {
        StoragesLoader storages = new StoragesLoader();
        return new com.artipie.security.policy.YamlPolicy(new com.artipie.asto.blocking.BlockingStorage(storages.newStorage("type", com.amihaiemil.eoyaml.Yaml.createYamlInput(sub.toString()).readYamlMapping())));
    } catch (final java.io.IOException err) {
        throw new java.io.UncheckedIOException(err);
    }
}
```
The changes I made are:

* Import the new `StoragesLoader` class.
* Create a new `StoragesLoader` object.
* Use the `newStorage` method of `StoragesLoader` to create a new `Storage` object.

Note that this is just one possible solution, and there may be other ways to fix the code as well.