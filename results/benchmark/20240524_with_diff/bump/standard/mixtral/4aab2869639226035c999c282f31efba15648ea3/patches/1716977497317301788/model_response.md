Here is a fixed version of your method that uses the new `StoragesLoader` class to create a storage:
```java
@Override
public Policy<?> getPolicy(PolicyConfig config) {
    final PolicyConfig sub = config.config("storage");
    try {
        StoragesLoader storages = new StoragesLoader();
        return new YamlPolicy(new BlockingStorage(storages.newObject(
            sub.string("type"),
            new Yaml().createYamlInput(sub.toString()).readYamlMapping()
        )));
    } catch (IOException err) {
        throw new UncheckedIOException(err);
    }
}
```
Note that I had to import the following classes in order for the code to compile:
```java
import com.amihaiemil.eoyaml.Yaml;
import com.artipie.asto.blocking.BlockingStorage;
import com.artipie.asto.factory.Config;
import com.artipie.asto.factory.StoragesLoader;
import com.artipie.security.policy.Policy;
import com.artipie.security.policy.PolicyConfig;
import com.artipie.security.policy.YamlPolicy;
import java.io.IOException;
import java.io.UncheckedIOException;
```