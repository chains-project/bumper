```java
import org.yaml.snakeyaml.nodes.Tag;

public class AbstractTest {

    public void test() {
        // Create a new TrustedTagInspector instance.
        TrustedTagInspector trustedTagInspector = new TrustedTagInspector();

        // Create a new Tag instance.
        Tag tag = new Tag("!foo");

        // Check if the tag is allowed.
        boolean isAllowed = trustedTagInspector.isGlobalTagAllowed(tag);

        // Assert that the tag is allowed.
        assertTrue(isAllowed);
    }
}
```