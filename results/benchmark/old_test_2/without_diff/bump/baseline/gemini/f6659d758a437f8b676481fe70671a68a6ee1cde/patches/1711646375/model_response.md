```java
  import org.yaml.snakeyaml.constructor.Constructor;
  import org.yaml.snakeyaml.introspector.Property;
  import org.yaml.snakeyaml.introspector.PropertyUtils;
  import org.yaml.snakeyaml.nodes.Node;
  import org.yaml.snakeyaml.nodes.Tag;
  import org.yaml.snakeyaml.parser.Parser;
  import org.yaml.snakeyaml.parser.ParserImpl;
  import org.yaml.snakeyaml.resolver.Resolver;
  import org.yaml.snakeyaml.resolver.ResolverImpl;

  import java.util.List;
  import java.util.Map;
  import java.util.Set;

  public class CustomParser extends ParserImpl {
    private final Resolver resolver;
    private final Constructor constructor;
    private final Map<Tag, PropertyUtils> propertyUtilsCache;

    public CustomParser(Resolver resolver, Constructor constructor) {
      super(resolver, constructor);
      this.resolver = resolver;
      this.constructor = constructor;
      this.propertyUtilsCache = constructor.getPropertyUtilsCache();
    }

    @Override
    public void checkNode(Node node) {
      if (node.getTag() == null) {
        Tag tag = resolver.resolve(node.getValue(), node.getStartMark());
        node.setTag(tag);
      }
      List<Property> properties = null;
      if (node.getTag() != null) {
        properties = propertyUtilsCache.get(node.getTag()).getProperties(node.getType());
      }
      if (properties != null) {
        for (Property property : properties) {
          if (property.getName() == null) {
            continue;
          }
          if (node.getValue() instanceof Map) {
            Map<Object, Object> map = (Map<Object, Object>) node.getValue();
            if (map.containsKey(property.getName())) {
              Object value = map.get(property.getName());
              if (value != null) {
                Node valueNode = new Node(value, property.getType(), node.getStartMark(), node.getEndMark(), node.getScalarStyle());
                checkNode(valueNode);
                map.put(property.getName(), valueNode.getValue());
              }
            }
          } else if (node.getValue() instanceof List) {
            List<Object> list = (List<Object>) node.getValue();
            for (int i = 0; i < list.size(); i++) {
              Object value = list.get(i);
              if (value != null) {
                Node valueNode = new Node(value, property.getType(), node.getStartMark(), node.getEndMark(), node.getScalarStyle());
                checkNode(valueNode);
                list.set(i, valueNode.getValue());
              }
            }
          } else if (node.getValue() instanceof Set) {
            Set<Object> set = (Set<Object>) node.getValue();
            for (Object value : set) {
              if (value != null) {
                Node valueNode = new Node(value, property.getType(), node.getStartMark(), node.getEndMark(), node.getScalarStyle());
                checkNode(valueNode);
                set.add(valueNode.getValue());
              }
            }
          }
        }
      }
    }
  }
```