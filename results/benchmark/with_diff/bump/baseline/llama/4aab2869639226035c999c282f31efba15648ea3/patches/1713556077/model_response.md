Here's a proposed patch to fix the error:
```java
@Override
public Policy<?> getPolicy(final PolicyConfig config) {
    final PolicyConfig sub = config.config("storage");
    try {
        return new YamlPolicy(
            new BlockingStorage(
                new StoragesLoader().newObject(sub.string("type"), Yaml.createYamlInput(sub.toString()).readYamlMapping())
            )
        );
    } catch (final IOException err) {
        throw new UncheckedIOException(err);
    }
}
```
The changes made were:

* Removed `new Storages()` as it's no longer available in the new library version.
* Instead, used `new StoragesLoader()` to create a `Storages` instance.
* Used `StoragesLoader.newObject()` to create a `Storage` instance instead of `Storages.newStorage()`.
* Passed `Yaml.createYamlInput(sub.toString()).readYamlMapping()` as the second argument to `new BlockingStorage()` instead of `YamlPolicyFactory.yamlMapping()` as it's no longer available in the new library version.

This patch should fix the error and allow the code to compile and run with the new library version.