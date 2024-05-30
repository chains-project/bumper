Here's the suggested patch for the failing method:
```java
@Override
public Policy<?> getPolicy(final PolicyConfig config) {
    final PolicyConfig sub = config.config("storage");
    try {
        StoragesLoader storages = new StoragesLoader();
        return new YamlPolicy(new BlockingStorage(storages.newObject(sub.string("type"), new YamlInput(sub.toString()).asMapping())));
    } catch (final IOException err) {
        throw new UncheckedIOException(err);
    }
}

private static class YamlInput implements com.artipie.asto.factory.Config.YamlInput {
    private final com.amihaiemil.eoyaml.YamlInput yamlInput;

    YamlInput(String yaml) {
        this.yamlInput = new com.amihaiemil.eoyaml.Yaml.createYamlInput(yaml);
    }

    @Override
    public com.amihaiemil.eoyaml.YamlMapping asMapping() {
        return yamlInput.readYamlMapping();
    }
}
```
Changes made:

1. Replaced `com.artipie.asto.factory.Storages` with `com.artipie.asto.factory.StoragesLoader`.
2. Created a helper class `YamlInput` to convert `com.amihaiemil.eoyaml.YamlInput` to `com.artipie.asto.factory.Config.YamlInput`.
3. Simplified exception handling using `java.io.UncheckedIOException`.

This solution assumes that the appropriate versions of `com.amihaiemil.eoyaml` and `com.artipie` dependencies are used.