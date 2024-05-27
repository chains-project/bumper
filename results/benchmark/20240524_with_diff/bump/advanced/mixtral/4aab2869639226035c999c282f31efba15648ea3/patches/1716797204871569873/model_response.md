Here is a fixed version of the `getPolicy` method that uses the new `StoragesLoader` class to create a `Storage` object:
```java
@Override
public Policy<?> getPolicy(final PolicyConfig config) {
    final PolicyConfig sub = config.config("storage");
    try {
        StoragesLoader loader = new StoragesLoader();
        return new YamlPolicy(new BlockingStorage(loader.newObject(sub.string("type"), sub.toString())));
    } catch (final IOException err) {
        throw new UncheckedIOException(err);
    }
}
```
In this version, we first create a new `StoragesLoader` object, and then use its `newObject` method to create a `Storage` object using the configuration from the `sub` object. Note that the `StoragesLoader` class has several other methods that may be useful in other contexts, such as `types` and `scanPackagesEnv`.