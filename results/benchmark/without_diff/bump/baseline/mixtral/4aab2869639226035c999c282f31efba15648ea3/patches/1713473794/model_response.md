Here's a possible patch for the given client code:
```java
import com.artipie.asto.factory.MappedStorages;

// ...

@Override
public PolicyFactory policyFactory() {
    return new YamlPolicyFactory(
        MappedStorages.mapped(storage(), key -> new YamlPolicy(key, content(key))))
}
```
In this patch, we replaced `Storages` with `MappedStorages`, which is a new class added in the external library. This change allows us to keep the same function signature while fixing the compilation error.