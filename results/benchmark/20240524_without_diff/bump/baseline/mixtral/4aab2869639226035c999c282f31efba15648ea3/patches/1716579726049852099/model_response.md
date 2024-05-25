Here's a possible patch for the failing client code:
```java
import com.artipie.asto.factory.MappedStorages;

// ...

@Override
public Optional<Policy> policy(final Path path) {
    return policy0(path).flatMap(policy -> {
        if (policy instanceof YamlPolicy) {
            return Optional.of(policy);
        }
        return Optional.ofNullable(
            MappedStorages.single("policy", policy)
        ).flatMap(sto -> YamlPolicy.class.cast(
            new YamlPolicyFactory(sto).create(path)
        ));
    });
}
```
This patch replaces the usage of `Storages` with `MappedStorages`, which is a new class added in the updated version of the external library. It also wraps the original policy in a `MappedStorage` and creates a new `YamlPolicy` instance using the new `YamlPolicyFactory`.

Note that this patch assumes that the `YamlPolicyFactory` constructor and the `create` method still exist and have the same signature as in the previous version of the library. If that's not the case, the patch might need to be adjusted accordingly.