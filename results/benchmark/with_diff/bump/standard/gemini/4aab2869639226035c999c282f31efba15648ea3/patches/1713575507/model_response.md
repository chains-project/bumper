```java
@java.lang.Override
public com.artipie.security.policy.Policy<?> getPolicy(final com.artipie.security.policy.PolicyConfig config) {
    final com.artipie.security.policy.PolicyConfig sub = config.config("storage");
    try {
        final com.artipie.asto.factory.Config cfg = new com.artipie.asto.factory.Config() {
            @java.lang.Override
            public java.lang.String get(final java.lang.String key) {
                return sub.string(key);
            }
        };
        final com.artipie.asto.factory.StoragesLoader loader = new com.artipie.asto.factory.StoragesLoader();
        return new com.artipie.security.policy.YamlPolicy(new com.artipie.asto.blocking.BlockingStorage(loader.newObject(sub.string("type"), cfg)));
    } catch (final java.io.IOException err) {
        throw new java.io.UncheckedIOException(err);
    }
}
```