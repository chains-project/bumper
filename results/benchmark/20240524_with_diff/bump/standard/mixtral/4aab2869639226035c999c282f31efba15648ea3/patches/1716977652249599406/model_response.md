Here's a possible patch for the failing client code:
```java
@Override
public Policy<?> getPolicy(PolicyConfig config) {
    final PolicyConfig sub = config.config("storage");
    try {
        StoragesLoader storagesLoader = new StoragesLoader();
        return new YamlPolicy(new BlockingStorage(storagesLoader.newObject(
            sub.string("type"),
            new YamlInput(sub.toString()).readYamlMapping()
        )));
    } catch (IOException err) {
        throw new UncheckedIOException(err);
    }
}

private static class YamlInput implements com.amihaiemil.eoyaml.YamlInput {
    private final String yaml;

    public YamlInput(String yaml) {
        this.yaml = yaml;
    }

    @Override
    public YamlMapping readYamlMapping() throws IOException {
        return (YamlMapping) new Yaml().load(yaml);
    }
}
```
The patch replaces the `Storages` class with the new `StoragesLoader` class, and creates a helper `YamlInput` class to handle the YAML input. Note that the `StoragesLoader` and `Yaml` classes are assumed to be imported from `com.artipie.asto.factory` and `com.amihaiemil.eoyaml` packages, respectively.