```java
import org.yaml.snakeyaml.nodes.Tag;

import java.util.List;

public class TrustedTagInspector {

    private final List<String> allowedTags;

    public TrustedTagInspector(List<String> allowedTags) {
        this.allowedTags = allowedTags;
    }

    public boolean isGlobalTagAllowed(Tag tag) {
        return allowedTags.contains(tag.getValue());
    }
}
```