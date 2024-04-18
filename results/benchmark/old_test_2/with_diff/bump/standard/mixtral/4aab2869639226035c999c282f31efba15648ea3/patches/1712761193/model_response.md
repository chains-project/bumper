Here's the fixed failing method with the necessary changes:

```java
@Override
public Policy<?> getPolicy(final PolicyConfig config) {
    final PolicyConfig sub = config.config("storage");
    try {
        StoragesLoader storagesLoader = new StoragesLoader();
        return new YamlPolicy(new BlockingStorage(storagesLoader.newObject(
                sub.string("type"),
                new YamlInput(sub.toString()).readYamlMapping()
        )));
    } catch (final IOException err) {
        throw new UncheckedIOException(err);
    }
}

private static class YamlInput implements com.amihaiemil.eoyaml.YamlInput {
    private final String input;

    public YamlInput(String input) {
        this.input = input;
    }

    @Override
    public YamlSequence readSequence() {
        // Implement this method if needed
        throw new UnsupportedOperationException();
    }

    @Override
    public YamlMapping readYamlMapping() {
        return (YamlMapping) com.amihaiemil.eoyaml.Yaml.createYaml().load(input);
    }
}
```

Changes made:

1. Replaced `com.artipie.asto.factory.Storages` with `com.artipie.asto.factory.StoragesLoader`.
2. Created a helper class `YamlInput` to read YAML input since `com.amihaiemil.eoyaml.YamlInput` is no longer present.
3. Updated the import statements accordingly.