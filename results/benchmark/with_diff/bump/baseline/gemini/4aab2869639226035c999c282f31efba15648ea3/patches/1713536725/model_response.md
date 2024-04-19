```java
  import com.artipie.asto.factory.StoragesLoader;

  public class YamlPolicyFactory {

    private final StoragesLoader loader;

    public YamlPolicyFactory(StoragesLoader loader) {
      this.loader = loader;
    }

    public YamlPolicyFactory() {
      this(new StoragesLoader());
    }

    public Policy policy(YamlMapping mapping) {
      return new Policy(
          mapping.value("name").asScalarString(),
          mapping.value("description").asScalarString(),
          mapping.value("subjects").asSequence().stream()
              .map(subject -> new Subject(
                  subject.value("type").asScalarString(),
                  subject.value("value").asScalarString()))
              .collect(Collectors.toList()),
          mapping.value("actions").asSequence().stream()
              .map(action -> new Action(
                  action.value("type").asScalarString(),
                  action.value("value").asScalarString()))
              .collect(Collectors.toList()),
          mapping.value("resources").asSequence().stream()
              .map(resource -> new Resource(
                  resource.value("type").asScalarString(),
                  resource.value("value").asScalarString()))
              .collect(Collectors.toList())
      );
    }
  }
```