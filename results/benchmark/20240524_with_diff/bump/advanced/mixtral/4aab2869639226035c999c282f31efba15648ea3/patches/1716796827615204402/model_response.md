Here's a potential patch for the failing client code:

```java
import com.artipie.asto.factory.StoragesLoader;
import com.artipie.asto.factory.Config;
import com.artipie.asto.Storage;
import java.util.Map;
import java.util.Collections;

@Override
public Policy<?> getPolicy(final PolicyConfig config) {
    final PolicyConfig sub = config.config("storage");
    try {
        StoragesLoader loader = new StoragesLoader(Collections.emptyMap());
        return new YamlPolicy(new BlockingStorage(loader.newObject(
            sub.string("type"),
            new com.amihaiemil.eoyaml.YamlInput(sub.toString()).as(Config.class)
        )));
    } catch (final IOException err) {
        throw new UncheckedIOException(err);
    }
}
```

In this patch, we create a new `StoragesLoader` instance and use its `newObject` method to create a new `Storage` object based on the `type` configuration value. We also use the `YamlInput` class directly instead of the deprecated `Yaml.createYamlInput` method.