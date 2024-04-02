Here's a proposed patch to fix the error:
```java
@Override
public Policy<?> getPolicy(final PolicyConfig config) {
    final PolicyConfig sub = config.config("storage");
    try {
        return new YamlPolicy(
            new BlockingStorage(
                new StoragesLoader().newStorage(
                    sub.string("type"), Yaml.createYamlInput(sub.toString()).readYamlMapping()
                )
            )
        );
    } catch (final IOException err) {
        throw new UncheckedIOException(err);
    }
}
```
The patch removes the usage of `Storages` class, which is removed in the new library version, and instead uses the `StoragesLoader` class, which is added in the new version, to create a `Storage` instance.
The `StoragesLoader` class provides a way to load storage instances from a configuration, which is what the `YamlPolicyFactory` class is trying to do.
The `newStorage` method of `StoragesLoader` takes a `String` parameter representing the type of storage, and a `Config` object, which in this case is a `PolicyConfig` object.
The `YamlPolicy` constructor takes a `BlockingStorage` argument, which is created using the `newStorage` method of `StoragesLoader`.
The rest of the code remains unchanged.
This patch should fix the error and allow the code to compile and run with the new library version.