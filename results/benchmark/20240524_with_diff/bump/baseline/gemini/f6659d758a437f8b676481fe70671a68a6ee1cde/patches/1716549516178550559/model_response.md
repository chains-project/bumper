```java
import org.yaml.snakeyaml.nodes.Tag;

import java.util.List;

public class TrustedTagInspector {

    private final List<Tag> allowedTags;

    public TrustedTagInspector(List<Tag> allowedTags) {
        this.allowedTags = allowedTags;
    }

    public boolean isGlobalTagAllowed(Tag tag) {
        return allowedTags.contains(tag);
    }
}
```