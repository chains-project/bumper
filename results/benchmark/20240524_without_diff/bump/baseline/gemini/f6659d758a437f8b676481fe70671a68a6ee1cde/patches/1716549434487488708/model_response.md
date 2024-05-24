```java
  import org.yaml.snakeyaml.constructor.Constructor;
import org.yaml.snakeyaml.nodes.Tag;
import org.yaml.snakeyaml.representer.Representer;

import java.util.Collections;
import java.util.List;
import java.util.Map;
import java.util.Set;

public class AbstractTest {

    private static final String[] YAML_TAGS = new String[]{"!include", "!import", "!merge", "!delete", "!set", "!unset", "!add", "!remove"};

    protected Constructor buildYamlConstructor() {
        Representer representer = new Representer();
        representer.setDefaultFlowStyle(DumperOptions.FlowStyle.BLOCK);
        representer.getPropertyUtils().setSkipMissingProperties(true);
        representer.getProperties().setSortKeys(false);

        Constructor constructor = new Constructor();
        constructor.addTypeDescription(new Tag("!include", Map.class), IncludeTag.class);
        constructor.addTypeDescription(new Tag("!import", Map.class), ImportTag.class);
        constructor.addTypeDescription(new Tag("!merge", Map.class), MergeTag.class);
        constructor.addTypeDescription(new Tag("!delete", Map.class), DeleteTag.class);
        constructor.addTypeDescription(new Tag("!set", Map.class), SetTag.class);
        constructor.addTypeDescription(new Tag("!unset", Map.class), UnsetTag.class);
        constructor.addTypeDescription(new Tag("!add", Map.class), AddTag.class);
        constructor.addTypeDescription(new Tag("!remove", Map.class), RemoveTag.class);
        constructor.addTypeDescription(new Tag("!null", Object.class), NullTag.class);
        constructor.addTypeDescription(new Tag("!timestamp", Object.class), TimestampTag.class);
        constructor.addTypeDescription(new Tag("!binary", Object.class), BinaryTag.class);
        constructor.addTypeDescription(new Tag("!omap", Map.class), OmapTag.class);
        constructor.addTypeDescription(new Tag("!pairs", List.class), PairsTag.class);
        constructor.addTypeDescription(new Tag("!set", Set.class), SetTag.class);
        return constructor;
    }
}
```