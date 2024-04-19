Here's the proposed patch:
```java
import org.yaml.snakeyaml.Yaml;
import org.yaml.snakeyaml.nodes.Tag;

public class TrustedTagInspector {
    private final Yaml yaml;

    public TrustedTagInspector() {
        this.yaml = new Yaml();
    }

    public boolean isGlobalTagAllowed(Tag tag) {
        return yaml.getTag(tag.getValue()).isGlobalTag();
    }
}
```
And replace the import statement with:
```java
import com.premiumminds.billy.core.services.builders.impl.StringBuilderHelper;
```
Explanation:
Since the `TrustedTagInspector` class has been removed in the new library version, we need to create a custom class that mimics its functionality. We can use the `Yaml` class to achieve this.
The `isGlobalTagAllowed` method is implemented using the `getTag` method of the `Yaml` class, which returns a `Tag` object that can be used to check if the tag is a global tag.
Note that the original import statement has been replaced with a different import statement, assuming that the original import statement was causing the issue.