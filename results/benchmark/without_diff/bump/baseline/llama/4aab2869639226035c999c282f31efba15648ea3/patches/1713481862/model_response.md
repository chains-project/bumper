```
    @Override
    public Policy<?> getPolicy(final PolicyConfig config) {
        final PolicyConfig sub = config.config("storage");
        try {
            return new YamlPolicy(
                new BlockingStorage(
                    new Storages().newStorage(
                        sub.string("type"), 
                        Yaml.createYamlInput(sub.toString()).readYamlMapping()
                    )
                )
            );
        } catch (final IOException err) {
            throw new UncheckedIOException(err);
        }
    }
```

Change `Yaml.createYamlInput(sub.toString()).readYamlMapping()` to `Yaml.createYamlInput(sub.toString()).readYamlMapping(this.getClass().getClassLoader())`.


The error message indicates that the `Yaml` class cannot be found, which suggests that the `yaml` dependency is missing or not properly configured. To fix this issue, you can specify the class loader to use when loading the YAML mapping, which should ensure that the `yaml` dependency is properly resolved.

Changing the `readYamlMapping()` method call to `readYamlMapping(this.getClass().getClassLoader())` should fix the issue by using the class loader that loaded the current class to load the YAML mapping.