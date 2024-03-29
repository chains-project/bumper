Here is a possible patch for the failing method:
```java
@Override
public Policy<?> getPolicy(final PolicyConfig config) {
    final PolicyConfig sub = config.config("storage");
    Object storageConfig = Yaml.createYamlInput(sub.toString()).readYamlMapping();
    try {
        return new YamlPolicy(
            new BlockingStorage(
                new Storages().newStorage(
                    sub.string("type"), storageConfig
                )
            )
        );
    } catch (final IOException err) {
        throw new UncheckedIOException(err);
    }
}
```
This patch removes the dependency on the `com.artipie.asto` package, which was causing the "cannot find symbol" error. Instead, it reads the storage configuration directly from the `PolicyConfig` object using the `Yaml` utility class. This should allow the method to compile and run without errors.

Note that this patch assumes that the `Yaml` class has a `createYamlInput` method that can parse a string into a `Mapping` object, and that the `PolicyConfig` class has a `toString` method that returns a string representation of the configuration. If these assumptions are incorrect, the patch may need to be modified accordingly.