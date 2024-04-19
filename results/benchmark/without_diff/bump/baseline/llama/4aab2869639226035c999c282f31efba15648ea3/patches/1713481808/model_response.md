Here's a possible patch to fix the error:
```java
@Override
public Policy<?> getPolicy(final PolicyConfig config) {
    final PolicyConfig sub = config.config("storage");
    try {
        return new YamlPolicy(
            new BlockingStorage(
                new Storages().newStorage(
                    sub.string("type"), Yaml.createYamlInput(sub.toString()).readYamlMapping()
                )
            )
        );
    } catch (final IOException err) {
        throw new UncheckedIOException(err);
    }
}
```

The error is caused by the fact that the `YamlPolicyFactory` class is trying to use the `Yaml` class from the `com.artipie.asto` package, which is not available in the dependencies of the project.

To fix the error, we can replace the `Yaml` class with the `Yaml` class from the `com.artipie.asto` package, which is available in the project's dependencies. We can do this by changing the import statement for the `Yaml` class to the following:
```
import com.artipie.asto.Yaml;
```
This will allow the `YamlPolicyFactory` class to use the `Yaml` class from the `com.artipie.asto` package, which should resolve the error.

Here's the modified code with the changed import statement:
```java
@Override
public Policy<?> getPolicy(final PolicyConfig config) {
    final PolicyConfig sub = config.config("storage");
    try {
        return new YamlPolicy(
            new BlockingStorage(
                new Storages().newStorage(
                    sub.string("type"), com.artipie.asto.Yaml.createYamlInput(sub.toString()).readYamlMapping()
                )
            )
        );
    } catch (final IOException err) {
        throw new UncheckedIOException(err);
    }
}
```
This modified code should compile and run without any errors related to the `Yaml` class.