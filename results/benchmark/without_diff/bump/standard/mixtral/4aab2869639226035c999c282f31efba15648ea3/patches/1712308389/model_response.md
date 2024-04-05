Here is a possible patch for the failing method:

```java
import com.artipie.asto.ext.KeyValueStorages;

@Override
public com.artipie.security.policy.Policy<?> getPolicy(final com.artipie.security.policy.PolicyConfig config) {
    final com.artipie.security.policy.PolicyConfig sub = config.config("storage");
    try {
        return new com.artipie.security.policy.YamlPolicy(new com.artipie.asto.blocking.BlockingStorage(new KeyValueStorages().newStorage(sub.string("type"), com.amihaiemil.eoyaml.Yaml.createYamlInput(sub.toString()).readYamlMapping())));
    } catch (final java.io.IOException err) {
        throw new java.io.UncheckedIOException(err);
    }
}
```

This patch replaces the `com.artipie.security.policy.Storages` class with `com.artipie.asto.ext.KeyValueStorages`, which is a new class added in a later version of the library. This should fix the "cannot find symbol" error.