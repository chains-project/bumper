Here's a possible patch for the given client code:
```java
@Override
public Policy<?> getPolicy(PolicyConfig config) {
    final PolicyConfig sub = config.config("storage");
    try {
        StoragesLoader storages = new StoragesLoader();
        return new YamlPolicy(new BlockingStorage(storages.newObject(
            sub.string("type"),
            new YamlInput(sub.toString())
        )));
    } catch (IOException err) {
        throw new UncheckedIOException(err);
    }
}

private static class YamlInput implements Config {
    private final YamlMapping yaml;

    YamlInput(String yamlStr) {
        this.yaml = Yaml.createYamlInput(yamlStr).readYamlMapping();
    }

    @Override
    public String string(String key) {
        return yaml.string(key);
    }

    @Override
    public Config config(String key) {
        return new YamlInput(yaml.string(key));
    }

    @Override
    public Set<String> keys() {
        return yaml.keys();
    }
}
```
Explanation:
- Replace `com.artipie.asto.factory.Storages` with `com.artipie.asto.factory.StoragesLoader`
- Replace `com.artipie.asto.factory.Storages.newStorage` with `com.artipie.asto.factory.StoragesLoader.newObject`
- Create a new private inner class `YamlInput` that implements `com.artipie.asto.factory.Config` interface to read YAML input and provide a way to access its properties
- Use `com.amihaiemil.eoyaml.Yaml.createYamlInput(sub.toString()).readYamlMapping()` to create `YamlMapping` object and pass it to `YamlInput` constructor
- Replace `com.artipie.security.policy.Storages.newStorage` with `storages.newObject`
- Replace `com.artipie.security.policy.Storages.types` with `com.artipie.asto.factory.StoragesLoader.types`
- Replace `com.artipie.asto.blocking.BlockingStorage` constructor argument with `new YamlInput(sub.toString())` instead of `com.amihaiemil.eoyaml.Yaml.createYamlInput(sub.toString()).readYamlMapping()`
- Remove `import com.amihaiemil.eoyaml.Yaml;` and add `import com.artipie.asto.factory.Config;`
- Remove `import com.artipie.asto.factory.Storages;` and add `import com.artipie.asto.factory.StoragesLoader;`
- Remove `import com.artipie.asto.factory.StorageConfig;` and add `import com.artipie.asto.factory.Config;`
- Remove `import com.artipie.asto.Storage;` and add `import com.artipie.asto.factory.Storage;`
- Remove `import com.artipie.asto.factory.StorageFactory;`
- Remove `import com.artipie.asto.fs.FileStorageFactory;`
- Remove `import com.artipie.asto.s3.S3StorageFactory;`
- Remove `import com.artipie.security.policy.Policy;`
- Remove `import com.artipie.security.policy.PolicyConfig;`
- Remove `import com.artipie.security.policy.YamlPolicy;`
- Remove `import com.artipie.security.policy.YamlPolicyFactory;`
- Remove `import com.artipie.asto.blocking.BlockingStorage;`
- Remove `import com.artipie.asto.Storage;`
- Remove `import com.artipie.asto.factory.StorageConfig;`
- Remove `import com.artipie.asto.factory.Storages;`
- Remove `import java.util.Map;`
- Remove `import java.util.Set;`
- Remove `import java.io.IOException;`
- Remove `import java.io.UncheckedIOException;`
- Remove `import java.util.stream.Collectors;`
- Remove `import java.util.stream.Stream;`
- Remove `import com.amihaiemil.eoyaml.YamlMapping;`
- Remove `import com.amihaiemil.eoyaml.YamlSequence;`
- Remove `import com.amihaiemil.eoyaml.Yaml;`