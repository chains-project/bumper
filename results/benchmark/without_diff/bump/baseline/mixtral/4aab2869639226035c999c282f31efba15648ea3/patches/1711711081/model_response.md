Here's a proposed patch for the failing client code:
```java
@Override
public Policy<?> getPolicy(PolicyConfig config) {
    final PolicyConfig sub = config.config("storage");
    ObjectMapper objectMapper = new ObjectMapper(new YAMLFactory());
    try {
        return new YamlPolicy(
            new BlockingStorage(
                new Storages().newStorage(
                    sub.string("type"), objectMapper.readValue(sub.toString(), Map.class)
                )
            )
        );
    } catch (final IOException err) {
        throw new UncheckedIOException(err);
    }
}
```
In this patch, I replaced the `Yaml` class with `ObjectMapper` from the Jackson library to parse the YAML string. The `Yaml` class may have been removed in the new version of the external dependency, so I used an alternative library method to parse the YAML string instead.