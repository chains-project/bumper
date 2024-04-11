Here's a possible patch for the given code:

```java
@Override
public Policy<?> getPolicy(PolicyConfig config) {
    PolicyConfig sub = config.config("storage");
    try {
        StoragesLoader storages = new StoragesLoader();
        return new YamlPolicy(new BlockingStorage(storages.newStorage(sub.string("type"), com.amihaiemil.eoyaml.Yaml.createYamlInput(sub.toString()).readYamlMapping())));
    } catch (IOException err) {
        throw new UncheckedIOException(err);
    }
}
```

The changes made include:

* Importing the `StoragesLoader` class from the `com.artipie.asto.factory` package.
* Creating a new `StoragesLoader` instance.
* Using the `newStorage` method of `StoragesLoader` instead of `Storages`.

Note that this solution assumes that the `StoragesLoader` class and its `newStorage` method are available and work as intended. If that's not the case, you may need to use a different approach.