```java
import org.yaml.snakeyaml.nodes.Tag;

import java.util.List;

public class AbstractTest {

    public AbstractTest() {
        super();
    }

    public void test() {
        List<Tag> allowedTags = List.of(Tag.MAP, Tag.SEQ, Tag.STR, Tag.INT, Tag.FLOAT, Tag.NULL, Tag.BOOL, Tag.TIMESTAMP);
        TrustedTagInspector inspector = new TrustedTagInspector(allowedTags);
    }
}
```