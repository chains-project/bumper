Here's the proposed patch for the failing method:
```java
@java.lang.Override
public com.artipie.security.policy.Policy<?> getPolicy(final com.artipie.security.policy.PolicyConfig config) {
    final com.artipie.security.policy.PolicyConfig sub = config.config("storage");
    try {
        return new com.artipie.security.policy.YamlPolicy(new com.artipie.asto.blocking.BlockingStorage(new com.artipie.asto.factory.StoragesLoader()
          .newObject(sub.string("type"), new com.artipie.asto.factory.Config() {
              @java.lang.Override
              public java.util.Map<java.lang.String, java.lang.String> asMap() {
                  return com.amihaiemil.eoyaml.Yaml.createYamlInput(sub.toString()).readYamlMapping();
              }
          }))));
    } catch (final java.io.IOException err) {
        throw new java.io.UncheckedIOException(err);
    }
}
```
The main change is the creation of an anonymous `Config` implementation for the `StoragesLoader.newObject` method. This allows us to use the new `StoragesLoader` class instead of the removed `Storages` class. The `Config` implementation converts the `YamlMapping` returned by the `sub.toString()` method to a `Map` required by the `Config.asMap()` method.