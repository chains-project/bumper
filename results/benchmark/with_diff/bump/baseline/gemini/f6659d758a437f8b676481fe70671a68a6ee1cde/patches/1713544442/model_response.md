```java
import org.yaml.snakeyaml.constructor.Constructor;
import org.yaml.snakeyaml.nodes.Tag;

import java.util.Collections;
import java.util.Set;

public class TrustedTagInspector {

    private final Constructor constructor;

    public TrustedTagInspector(Constructor constructor) {
        this.constructor = constructor;
    }

    public Set<Tag> getAllowedTags() {
        return Collections.emptySet();
    }

    public boolean isGlobalTagAllowed(Tag tag) {
        return getAllowedTags().contains(tag);
    }
}
```