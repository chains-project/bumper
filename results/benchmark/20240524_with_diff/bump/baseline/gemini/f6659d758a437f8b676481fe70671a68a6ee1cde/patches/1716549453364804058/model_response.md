```java
  import org.yaml.snakeyaml.nodes.Tag;

  import java.util.List;

  public abstract class AbstractTest {

      private static final List<Tag> ALLOWED_TAGS = List.of(
              new Tag("!include"),
              new Tag("!>),
              new Tag("!<!"),
              new Tag("!>"),
              new Tag("!<"),
              new Tag("!|"),
              new Tag("!."),
              new Tag("!{"),
              new Tag("!}"),
              new Tag("![")
      );

      protected TrustedTagInspector createTrustedTagInspector() {
          return new TrustedTagInspector() {
              @Override
              public boolean isGlobalTagAllowed(Tag tag) {
                  return ALLOWED_TAGS.contains(tag);
              }
          };
      }
  }
```