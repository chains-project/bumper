@java.lang.Override
public com.artipie.security.policy.Policy<?> getPolicy(final com.artipie.security.policy.PolicyConfig config) {
    final com.artipie.security.policy.PolicyConfig sub = config.config("storage");
    try {
        return new com.artipie.security.policy.YamlPolicy(new com.artipie.asto.blocking.BlockingStorage(new com.artipie.asto.factory.StoragesLoader().newObject(sub.string("type"), new com.artipie.asto.factory.Config(sub.toString())).readYamlMapping()));
    } catch (final java.io.IOException err) {
        throw new java.io.UncheckedIOException(err);
    }
}