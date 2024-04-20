```java
@java.lang.Override
public com.artipie.security.policy.Policy<?> getPolicy(final com.artipie.security.policy.PolicyConfig config) {
    final com.artipie.security.policy.PolicyConfig sub = config.config("storage");
    try {
        final com.artipie.asto.factory.Config storageConfig = new com.artipie.asto.factory.Config.From(sub);
        return new com.artipie.security.policy.YamlPolicy(
                new com.artipie.asto.blocking.BlockingStorage(
                        com.artipie.asto.factory.StoragesLoader.getInstance().newObject(
                                sub.string("type"), storageConfig)));
    } catch (final java.io.IOException err) {
        throw new java.io.UncheckedIOException(err);
    }
}
```