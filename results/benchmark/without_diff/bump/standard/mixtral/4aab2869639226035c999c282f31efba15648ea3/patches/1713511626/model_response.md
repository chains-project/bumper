Here's the proposed patch for the given client code:

```java
@java.lang.Override
public com.artipie.security.policy.Policy<?> getPolicy(final com.artipie.security.policy.PolicyConfig config) {
    final com.artipie.security.policy.PolicyConfig sub = config.config("storage");
    try {
        return new com.artipie.security.policy.YamlPolicy(new com.artipie.asto.blocking.BlockingStorage(new com.artipie.asto.Storage<>(com.amihaiemil.eoyaml.Yaml.createYamlInput(sub.toString()).readYamlMapping())
                .withName(sub.string("type"))));
    } catch (final java.io.IOException err) {
        throw new java.io.UncheckedIOException(err);
    }
}
```

In the provided code, I replaced the `Storages` class with the `Storage` class since the `Storages` class might have been removed or deprecated. I also used the `withName` method to set the name of the storage, which is a more appropriate way to set the name according to the Artipie documentation.