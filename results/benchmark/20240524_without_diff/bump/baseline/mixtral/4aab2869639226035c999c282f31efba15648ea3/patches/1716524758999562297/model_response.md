Here's a patch that you can apply to fix the error:

```java
import com.artipie.asto.factory.StoragesLoader;
import com.artipie.asto.factory.Config;

@Override
public Policy<?> getPolicy(final PolicyConfig config) {
    final PolicyConfig sub = config.config("storage");
    try {
        StoragesLoader storagesLoader = new StoragesLoader();
        return new YamlPolicy(
            new BlockingStorage(
                storagesLoader.newStorage(
                    sub.string("type"), Yaml.createYamlInput(sub.toString()).readYamlMapping()
                )
            )
        );
    } catch (final IOException err) {
        throw new UncheckedIOException(err);
    }
}
```

The patch creates a new instance of `StoragesLoader` and uses it to create a new storage object. This is possible because the new library version includes the `StoragesLoader` class, which provides a new way to create storage objects.