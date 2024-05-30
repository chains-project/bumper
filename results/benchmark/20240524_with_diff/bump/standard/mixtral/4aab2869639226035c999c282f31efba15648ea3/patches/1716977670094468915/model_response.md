Here's a possible patch for the failing client code:
```java
@java.lang.Override
public com.artipie.security.policy.Policy<?> getPolicy(final com.artipie.security.policy.PolicyConfig config) {
    final com.artipie.security.policy.PolicyConfig sub = config.config("storage");
    try {
        StoragesLoader storages = new com.artipie.asto.factory.StoragesLoader();
        return new com.artipie.security.policy.YamlPolicy(new com.artipie.asto.blocking.BlockingStorage(storages.newObject(sub.string("type"), new com.artipie.asto.factory.Config() {
            @java.util.function.Function<String, String> string(String key) {
                return sub.string(key);
            }

            @java.util.function.Function<String, java.io.InputStream> inputStream(String key) {
                return () -> new java.io.ByteArrayInputStream(sub.toString().getBytes());
            }
        })));
    } catch (final java.io.IOException err) {
        throw new java.io.UncheckedIOException(err);
    }
}
```
The changes I made are:

* Replace `com.artipie.asto.factory.Storages` with `com.artipie.asto.factory.StoragesLoader`, which is the new class that replaces the old `Storages` class.
* Use the `newObject` method of `StoragesLoader` to create a new `Storage` object, passing in the `type` string from the `PolicyConfig` and a custom `Config` object that can extract the necessary configuration information from the `PolicyConfig`.
* Define a custom `Config` object that implements the `com.artipie.asto.factory.Config` interface. This object has two methods: `string(String key)` and `inputStream(String key)`, which are used by the `StoragesLoader` to extract the necessary configuration information from the `PolicyConfig`.
* Use a `ByteArrayInputStream` to convert the `toString()` value of the `PolicyConfig` to an `InputStream`, which is required by the `StoragesLoader`.

Note that this patch assumes that the `type` string in the `PolicyConfig` corresponds to a valid storage type that is supported by the new `StoragesLoader` class. If this is not the case, then the `newObject` method will throw an exception.