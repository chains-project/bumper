```java
@java.lang.Override
public com.artipie.security.policy.Policy<?> getPolicy(final com.artipie.security.policy.PolicyConfig config) {
    final com.artipie.security.policy.PolicyConfig sub = config.config("storage");
    try {
        com.artipie.asto.factory.StoragesLoader loader = new com.artipie.asto.factory.StoragesLoader();
        com.artipie.asto.Storage storage = loader.newObject(sub.string("type"), sub);
        return new com.artipie.security.policy.YamlPolicy(storage);
    } catch (final java.io.IOException err) {
        throw new java.io.UncheckedIOException(err);
    }
}
```