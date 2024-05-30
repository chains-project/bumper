Here's the proposed patch:

```java
@Override
public Policy<?> getPolicy(final PolicyConfig config) {
    final PolicyConfig sub = config.config("storage");
    try {
        StoragesLoader storagesLoader = new StoragesLoader();
        return new YamlPolicy(new BlockingStorage(storagesLoader.newObject(
            sub.string("type"),
            new YamlInput(sub.toString()).asInput()
        )));
    } catch (final IOException err) {
        throw new UncheckedIOException(err);
    }
}

private static class YamlInput implements Config {
    private final String yaml;

    public YamlInput(String yaml) {
        this.yaml = yaml;
    }

    public InputStream asInput() {
        return new ByteArrayInputStream(yaml.getBytes(StandardCharsets.UTF_8));
    }
}
```

The patch replaces the usage of the deprecated `Storages` class with the new `StoragesLoader` class. The `StoragesLoader` class provides a method `newObject` that can be used to create a new `Storage` object based on a given type and configuration. The `YamlInput` class is a simple wrapper around a YAML string that implements the `Config` interface required by the `newObject` method. The `InputStream` returned by the `asInput` method is used to read the YAML configuration.