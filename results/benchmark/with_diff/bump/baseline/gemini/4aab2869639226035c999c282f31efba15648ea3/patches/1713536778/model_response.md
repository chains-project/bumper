```java
  import com.artipie.asto.factory.StoragesLoader;

  public class YamlPolicyFactory {

    private final StoragesLoader storagesLoader;

    public YamlPolicyFactory(StoragesLoader storagesLoader) {
      this.storagesLoader = storagesLoader;
    }

    public static YamlPolicyFactory from(YamlMapping config) {
      return new YamlPolicyFactory(new StoragesLoader(config.yamlMapping("storages")));
    }

    // ...
  }
```