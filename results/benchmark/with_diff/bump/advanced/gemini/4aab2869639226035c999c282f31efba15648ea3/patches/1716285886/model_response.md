```java
@java.lang.Override
public com.artipie.security.policy.Policy<?> getPolicy(final com.artipie.security.policy.PolicyConfig config) {
    final com.artipie.security.policy.PolicyConfig sub = config.config("storage");
    final com.artipie.asto.factory.StorageFactory storageFactory = new com.artipie.asto.factory.StorageFactory();
    try {
        return new com.artipie.security.policy.YamlPolicy(storageFactory.newStorage(new com.artipie.asto.factory.Config() {
            @Override
            public java.lang.String string(final java.lang.String key) {
                return sub.string(key);
            }
        }));
    } catch (final java.io.IOException err) {
        throw new java.io.UncheckedIOException(err);
    }
}
```