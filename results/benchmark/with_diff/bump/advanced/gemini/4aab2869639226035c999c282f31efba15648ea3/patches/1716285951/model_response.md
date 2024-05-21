```java
@java.lang.Override
public com.artipie.security.policy.Policy<?> getPolicy(final com.artipie.security.policy.PolicyConfig config) {
    final com.artipie.security.policy.PolicyConfig sub = config.config("storage");
    try {
        return new com.artipie.security.policy.YamlPolicy(
                new com.artipie.asto.fs.FileStorageFactory().newStorage(
                        new com.artipie.asto.factory.Config(
                                com.artipie.asto.factory.StorageFactory.class,
                                new java.util.HashMap() {{
                                    put("type", sub.string("type"));
                                    put("path", sub.string("path"));
                                }}
                        )
                )
        );
    } catch (final java.io.IOException err) {
        throw new java.io.UncheckedIOException(err);
    }
}
```