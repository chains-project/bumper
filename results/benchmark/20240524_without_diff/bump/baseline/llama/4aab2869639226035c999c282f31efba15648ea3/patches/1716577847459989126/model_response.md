```java
public Policy<?> getPolicy(final PolicyConfig config) {
    final PolicyConfig sub = config.config("storage");
    final Object yamlInput = Yaml.createYamlInput(sub.toString());
    final Map<String, Object> yamlMapping = yamlInput.readYamlMapping();
    return new YamlPolicy(
        new BlockingStorage(
            new Storages().newStorage(
                sub.string("type"), yamlMapping
            )
        )
    );
}
```