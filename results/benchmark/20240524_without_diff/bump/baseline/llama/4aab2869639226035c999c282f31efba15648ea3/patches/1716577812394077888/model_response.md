```java
public Policy<?> getPolicy(final PolicyConfig config) {
    final PolicyConfig sub = config.config("storage");
    final Map<String, Object> yamlMap = Yaml.createYamlInput(sub.toString()).readYamlMapping();
    final String type = sub.string("type");
    return new YamlPolicy(new BlockingStorage(new Storages().newStorage(type, yamlMap)));
}
```