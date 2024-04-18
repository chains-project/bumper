```java
  import org.yaml.snakeyaml.inspector.TrustedTagInspector;
  import org.yaml.snakeyaml.nodes.Tag;

  import java.util.Arrays;
  import java.util.Collections;
  import java.util.List;
  import java.util.Set;

public class AbstractTest {

    private static final Set<Tag> DEFAULT_TAGS = Collections.unmodifiableSet(
            Arrays.asList(Tag.MAP, Tag.SEQ, Tag.STR, Tag.INT, Tag.FLOAT, Tag.NULL, Tag.BOOL, Tag.OPAQUE));

    private static final TrustedTagInspector DEFAULT_INSPECTOR = new TrustedTagInspector() {
        @Override
        public boolean isSafeTag(Tag tag) {
            return true;
        }

        @Override
        public List<Tag> getTags() {
            return Collections.emptyList();
        }
    };

    protected TrustedTagInspector getTrustedTagInspector() {
        return DEFAULT_INSPECTOR;
    }

    protected Set<Tag> getDefaultTags() {
        return DEFAULT_TAGS;
    }
}
```