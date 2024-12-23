Here's a proposed patch for the failing method:
```java
import com.artipie.asto.ext.ExtStorage;

@Override
public com.artipie.security.policy.Policy<?> getPolicy(final com.artipie.security.policy.PolicyConfig config) {
    final com.artipie.security.policy.PolicyConfig sub = config.config("storage");
    try {
        return new com.artipie.security.policy.YamlPolicy(new com.artipie.asto.blocking.BlockingStorage(new ExtStorage().newStorage(sub.string("type"), com.amihaiemil.eoyaml.Yaml.createYamlInput(sub.toString()).readYamlMapping())));
    } catch (final java.io.IOException err) {
        throw new java.io.UncheckedIOException(err);
    }
}
```
The patch replaces the usage of the removed `com.artipie.security.policy.Storages` class with the new `com.artipie.asto.ext.ExtStorage` class, which provides a similar method for creating a storage object.