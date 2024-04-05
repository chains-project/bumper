Here's a proposed patch for the failing method:
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
The change is the replacement of `new com.artipie.security.policy.Storages()` with `new KeyValueStorages()`, which is an added library method identified with `++`.