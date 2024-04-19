Here's the proposed patch:

```java
@java.lang.Override
public com.artipie.security.policy.Policy<?> getPolicy(final com.artipie.security.policy.PolicyConfig config) {
    final com.artipie.security.policy.PolicyConfig sub = config.config("storage");
    try {
        return new com.artipie.security.policy.YamlPolicy(new com.artipie.asto.blocking.BlockingStorage(new com.artipie.asto.Storage.Base(com.artipie.asto.Storage.of(sub.string("type"), context -> new com.artipie.asto.memory.InMemoryStorage()))));
    } catch (final java.io.IOException err) {
        throw new java.io.UncheckedIOException(err);
    }
}
```

In this patch, I replaced the `com.artipie.security.policy.Storages` class with `com.artipie.asto.Storage.Base`, which is an added library method identified with `++`. I also replaced the `com.artipie.security.policy.Storages.newStorage` method with `com.artipie.asto.Storage.of`, which is also an added library method. This should fix the "cannot find symbol" error for the `Storages` class.