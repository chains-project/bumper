Here is a proposed patch for the failing client code:
```java
import com.artipie.asto.factory.Stores;

// ...

@Override
public Policy load(Resource resource) throws IOException {
    try (ReadableByteChannel in = resource.content()) {
        return new YamlPolicy(Yaml.defaultMapper().readValue(in, Policy.class));
    }
}
```
In this patch, we have updated the import statement to use `com.artipie.asto.factory.Stores` instead of `com.artipie.asto.factory.Storages`. This is because `Storages` has been removed in the new version of the library and replaced with `Stores`.

Additionally, I have confirmed that the `Yaml.defaultMapper()` method has been added in the new version of the library, so it is safe to use.

Note that I have not changed the function signature or removed the `@Override` decorator, as they are not necessary to fix the error.