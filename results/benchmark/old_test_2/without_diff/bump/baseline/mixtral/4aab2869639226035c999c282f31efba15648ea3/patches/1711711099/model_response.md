Here is a fixed version of the `getPolicy` method:
```java
    @Override
    public Policy<?> getPolicy(final PolicyConfig config) {
        final PolicyConfig sub = config.config("storage");
        Storages storages = new Storages();
        try {
            return new YamlPolicy(
                new BlockingStorage(
                    storages.newStorage(
                        sub.string("type"), Yaml.createYamlInput(sub.toString()).readYamlMapping()
                    )
                )
            );
        } catch (final IOException err) {
            throw new UncheckedIOException(err);
        }
    }
```
The only change made is the addition of the line `Storages storages = new Storages();`. This creates a new instance of the `Storages` class, which is then used in the `newStorage` method call. This is likely necessary because the `newStorage` method is no longer a static method in the updated version of the external library, and so an instance of the `Storages` class is required to call it.