Here's the proposed patch for the given client code:

```java
@Override
public Policy<?> getPolicy(PolicyConfig config) {
    final PolicyConfig sub = config.config("storage");
    try {
        StoragesLoader storagesLoader = new StoragesLoader();
        return new YamlPolicy(new BlockingStorage(storagesLoader.newObject(
            sub.string("type"),
            new YamlInput(sub.toString()).asInput()
        )));
    } catch (IOException err) {
        throw new UncheckedIOException(err);
    }
}

private static class YamlInput implements Config {
    private final String yaml;

    public YamlInput(String yaml) {
        this.yaml = yaml;
    }

    public Input asInput() {
        return new YamlMappingInput(Yaml.createYamlInput(yaml).readYamlMapping());
    }
}

private static class YamlMappingInput implements Input {
    private final YamlMapping mapping;

    public YamlMappingInput(YamlMapping mapping) {
        this.mapping = mapping;
    }

    @Override
    public String key(String name) {
        return mapping.string(name);
    }

    @Override
    public Input input(String name) {
        return new YamlMappingInput(mapping.mapping(name));
    }
}
```

This patch replaces the use of the deprecated `Storages` class with the new `StoragesLoader` class to create a `Storage` object. I've also added two utility classes, `YamlInput` and `YamlMappingInput`, to simplify the creation of a `YamlMapping` object from a string and to provide a simple implementation of the `Input` interface, respectively.