```java
@Override
public Policy<?> getPolicy(final PolicyConfig config) {
    final PolicyConfig sub = config.config("storage");
    try {
        return new YamlPolicy(
            new BlockingStorage(
                new Storages().newStorage(
                    sub.string("type"), Yaml.createYamlInput(sub.string("config")).readYamlMapping()
                )
            )
        );
    } catch (final IOException err) {
        throw new UncheckedIOException(err);
    }
}
```
In the original code, `sub.toString()` was being used which is likely returning a string representation of the object and not the actual configuration data that is expected by `Yaml.createYamlInput()`. The patch replaces `sub.toString()` with `sub.string("config")` to retrieve the actual configuration data.