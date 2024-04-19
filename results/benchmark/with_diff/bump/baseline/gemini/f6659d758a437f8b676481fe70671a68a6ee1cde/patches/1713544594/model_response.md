```java
import org.yaml.snakeyaml.nodes.Tag;
import org.yaml.snakeyaml.representer.Representer;

public abstract class AbstractTest {

    protected Representer representer;

    public AbstractTest() {
        representer = new Representer();
        representer.addImplicitResolver(Tag.MAP, representer.nullRepresent, "!");
        representer.addImplicitResolver(Tag.SET, representer.nullRepresent, "!");
        representer.addImplicitResolver(Tag.SEQ, representer.nullRepresent, "!");
    }

    public boolean isGlobalTagAllowed(Tag tag) {
        return representer.isGlobalTagAllowed(tag);
    }
}
```