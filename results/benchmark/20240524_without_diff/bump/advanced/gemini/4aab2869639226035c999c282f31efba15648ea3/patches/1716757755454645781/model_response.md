```java
@java.lang.Override
public com.artipie.security.policy.Policy<?> getPolicy(final com.artipie.security.policy.PolicyConfig config) {
    final com.artipie.security.policy.PolicyConfig sub = config.config("storage");
    try {
        return new com.artipie.security.policy.YamlPolicy(new com.artipie.asto.blocking.BlockingStorage(new com.artipie.asto.Storage() {
            @java.lang.Override
            public java.util.concurrent.CompletionStage<java.lang.Void> save(final java.lang.String key, final java.io.InputStream stream) {
                return java.util.concurrent.CompletableFuture.completedFuture(null);
            }

            @java.lang.Override
            public java.util.concurrent.CompletionStage<java.io.InputStream> load(final java.lang.String key) {
                return java.util.concurrent.CompletableFuture.completedFuture(new java.io.ByteArrayInputStream(sub.toString().getBytes()));
            }
        }));
    } catch (final java.io.IOException err) {
        throw new java.io.UncheckedIOException(err);
    }
}
```