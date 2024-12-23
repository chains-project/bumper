```java
import org.yaml.snakeyaml.nodes.Tag;
import org.yaml.snakeyaml.constructor.Constructor;

import java.util.Set;

public class AbstractTest {

    protected Constructor constructor;

    public AbstractTest() {
        constructor = new Constructor();
        constructor.setAllowDuplicateKeys(false);
        constructor.setWrappedToBean(true);
    }

    protected void allowTag(Tag tag) {
        constructor.addTypeDescription(new SetTag(tag));
    }

    private static class SetTag extends org.yaml.snakeyaml.introspector.BeanAccess {
        private final Tag tag;

        public SetTag(Tag tag) {
            this.tag = tag;
        }

        @Override
        public Set<Property> getProperties(Class<? extends Object> type) {
            Set<Property> properties = super.getProperties(type);
            for (Property property : properties) {
                property.setType(tag);
            }
            return properties;
        }
    }
}
```