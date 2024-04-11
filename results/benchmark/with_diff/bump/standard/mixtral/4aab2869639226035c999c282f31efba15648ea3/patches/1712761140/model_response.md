Here's a possible patch for the given code:

```java
@java.lang.Override
public com.artipie.security.policy.Policy<?> getPolicy(final com.artipie.security.policy.PolicyConfig config) {
    final com.artipie.security.policy.PolicyConfig sub = config.config("storage");
    try {
        StoragesLoader loader = new com.artipie.asto.factory.StoragesLoader();
        return new com.artipie.security.policy.YamlPolicy(new com.artipie.asto.blocking.BlockingStorage(loader.newObject(sub.string("type"), new com.artipie.asto.factory.Config() {{
            put("path", sub.toString());
        }}).get()));
    } catch (final java.io.IOException err) {
        throw new java.io.UncheckedIOException(err);
    }
}
```

The main change is the use of `StoragesLoader` instead of `Storages`, and the creation of a new `Config` object to replace the `StorageConfig` object. The `Config` object is created as an anonymous class extending `com.artipie.asto.factory.Config` and setting the `path` property to the value of `sub.toString()`.