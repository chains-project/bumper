```java
import org.yaml.snakeyaml.nodes.Tag;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.List;

public class TrustedTagInspector {

    private final List<Tag> allowedTags;

    public TrustedTagInspector(List<Tag> allowedTags) {
        this.allowedTags = Collections.unmodifiableList(new ArrayList<>(allowedTags));
    }

    public TrustedTagInspector() {
        this(Collections.emptyList());
    }

    public boolean isGlobalTagAllowed(Tag tag) {
        return allowedTags.isEmpty() || allowedTags.contains(tag);
    }
}
```