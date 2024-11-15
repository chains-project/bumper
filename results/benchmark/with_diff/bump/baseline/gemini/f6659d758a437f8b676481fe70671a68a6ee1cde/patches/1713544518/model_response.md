```java
import org.yaml.snakeyaml.nodes.Tag;

import java.util.Arrays;
import java.util.HashSet;
import java.util.Set;

public class TrustedTagInspector {

    private static final Set<Tag> GLOBAL_TAGS = new HashSet<>(Arrays.asList(
            new Tag("tag:yaml.org,2002:str"),
            new Tag("tag:yaml.org,2002:int"),
            new Tag("tag:yaml.org,2002:float"),
            new Tag("tag:yaml.org,2002:bool"),
            new Tag("tag:yaml.org,2002:null"),
            new Tag("tag:yaml.org,2002:timestamp"),
            new Tag("tag:yaml.org,2002:binary"),
            new Tag("tag:yaml.org,2002:omap"),
            new Tag("tag:yaml.org,2002:pairs"),
            new Tag("tag:yaml.org,2002:set"),
            new Tag("tag:yaml.org,2002:seq"),
            new Tag("tag:yaml.org,2002:map")
    ));

    public boolean isGlobalTagAllowed(Tag tag) {
        return GLOBAL_TAGS.contains(tag);
    }
}
```