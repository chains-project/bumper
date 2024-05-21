Here is a possible patch for the failing client code:
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
In this patch, I have replaced the `com.artipie.security.policy.Storages` class with the `com.artipie.asto.ext.ExtStorage` class, which provides a similar `newStorage` method. I have also imported the fully qualified name of `ExtStorage` for clarity.

Note that this patch assumes that the `ExtStorage` class provides the necessary functionality to replace `Storages`. If this is not the case, a different approach may be needed.