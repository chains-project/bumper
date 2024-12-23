```java
import org.yaml.snakeyaml.constructor.Constructor;
import org.yaml.snakeyaml.introspector.PropertyUtils;
import org.yaml.snakeyaml.nodes.Node;
import org.yaml.snakeyaml.nodes.Tag;
import org.yaml.snakeyaml.parser.ParserImpl;
import org.yaml.snakeyaml.resolver.Resolver;

  import org.yaml.snakeyaml.Yaml;
  import org.yaml.snakeyaml.constructor.Constructor;
  import org.yaml.snakeyaml.introspector.PropertyUtils;
  import org.yaml.snakeyaml.nodes.Node;
  import org.yaml.snakeyaml.nodes.Tag;
  import org.yaml.snakeyaml.parser.ParserImpl;
  import org.yaml.snakeyaml.resolver.Resolver;

  public class MyConstructor extends Constructor {
    public MyConstructor() {
      this(Object.class);
    }

    public MyConstructor(Class<? extends Object> theClass) {
      super(theClass);
      yamlConstructors.put(Tag.MAP, new ConstructYamlMap(this));
      yamlConstructors.put(Tag.SEQ, new ConstructYamlSeq(this));
    }

    @Override
    protected PropertyUtils createPropertyUtils() {
      return new PropertyUtils() {
        @Override
        public Set<Property> getProperties(Class<?> type) {
          Set<Property> properties = super.getProperties(type);
          for (Property property : properties) {
            Tag tag = (Tag) property.getAnnotation(Tag.class);
            if (tag != null) {
              property.setType(tag.value());
            }
          }
          return properties;
        }
      };
    }

    @Override
    protected Resolver createResolver() {
      return new Resolver() {
        @Override
        public Tag resolve(Node node, Tag defaultTag) {
          if (node.getTag() != null) {
            return node.getTag();
          }
          return super.resolve(node, defaultTag);
        }
      };
    }

    @Override
    protected ParserImpl createParser(Resolver resolver) {
      return new ParserImpl(resolver) {
        @Override
        protected Node doConstructDocument(Node node) {
          Node document = super.doConstructDocument(node);
          document.setTag(Tag.MAP);
          return document;
        }
      };
    }
  }

  public static void main(String[] args) {
    Yaml yaml = new Yaml(new MyConstructor());
    Map<String, Object> map = yaml.load("foo: bar");
    System.out.println(map);
  }
```