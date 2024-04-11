Here's a proposed patch for the given client code, taking into account the changes in the new library version:

```java
@Override
public com.artipie.security.policy.Policy<?> getPolicy(final com.artipie.security.policy.PolicyConfig config) {
    final com.artipie.security.policy.PolicyConfig sub = config.config("storage");
    try {
        return new com.artipie.security.policy.YamlPolicy(new com.artipie.asto.blocking.BlockingStorage(new com.artipie.asto.factory.StoragesLoader()
            .newObject(sub.string("type"), new com.artipie.asto.factory.Config() {
                @Override
                public <T> T property(java.lang.Class<T> key) {
                    return (T) sub.toString();
                }
            }))
        );
    } catch (final java.io.IOException err) {
        throw new java.io.UncheckedIOException(err);
    }
}
```

This patch replaces the removed `Storages` class with the new `StoragesLoader` class, which has a `newObject` method to create a storage. Additionally, a simple anonymous `Config` implementation is provided to pass the required configuration for the storage.