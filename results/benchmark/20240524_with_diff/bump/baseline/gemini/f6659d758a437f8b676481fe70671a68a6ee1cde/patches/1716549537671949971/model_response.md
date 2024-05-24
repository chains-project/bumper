```java
import org.yaml.snakeyaml.constructor.Constructor;
import org.yaml.snakeyaml.nodes.Tag;
import org.yaml.snakeyaml.representer.Representer;

public class AbstractTest {

    protected Constructor createConstructor() {
        Constructor constructor = new Constructor();
        constructor.addTypeDescription(new Tag("!secret"), Secret.class);
        return constructor;
    }

    protected Representer createRepresenter() {
        Representer representer = new Representer();
        representer.addClassTag(Secret.class, new Tag("!secret"));
        return representer;
    }
}
```