@java.lang.Override
public com.artipie.security.policy.Policy<?> getPolicy(final com.artipie.security.policy.PolicyConfig config) {
    final com.artipie.security.policy.PolicyConfig sub = config.config("storage");
    try {
        com.artipie.asto.factory.StoragesLoader storagesLoader = new com.artipie.asto.factory.StoragesLoader();
        return new com.artipie.security.policy.YamlPolicy(new com.artipie.asto.blocking.BlockingStorage(storagesLoader.newObject(sub.string("type"), sub)));
    } catch (final java.io.IOException err) {
        throw new java.io.UncheckedIOException(err);
    }
}