```java
import org.yaml.snakeyaml.constructor.Constructor;
import org.yaml.snakeyaml.nodes.Tag;

import java.util.List;

public class AbstractTest {

    public void test() {
        Constructor constructor = new Constructor();
        List<Tag> tags = List.of(Tag.MAP, Tag.SEQ, Tag.STR);
        constructor.setTagInspector(new TrustedTagInspector(tags));
    }
}
```