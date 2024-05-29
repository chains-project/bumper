Here's a fixed version of the `getPolicy` method:

```java
@Override
public Policy<?> getPolicy(final PolicyConfig config) {
    final PolicyConfig sub = config.config("storage");
    try {
        return new YamlPolicy(new BlockingStorage(new com.artipie.asto.Storage.Default(new com.artipie.asto.EsMemoryStorage()))){
            @Override
            public String type() {
                return sub.string("type");
            }
        };
    } catch (final IOException err) {
        throw new UncheckedIOException(err);
    }
}
```

In this version, I've replaced the `com.artipie.security.policy.Storages` class with `com.artipie.asto.Storage.Default` class, which is an added library method identified with `++`. I've also created a new anonymous class extending `YamlPolicy` to override the `type` method and return the type from the configuration.

Note that this is just a workaround for the issue caused by the external dependency failure. It's recommended to investigate and fix the root cause of the failure in the external dependency.