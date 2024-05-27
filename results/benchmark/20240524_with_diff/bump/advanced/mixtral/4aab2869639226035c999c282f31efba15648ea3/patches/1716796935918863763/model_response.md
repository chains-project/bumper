Here's the proposed patch for the failing method:
```java
import com.artipie.asto.factory.StoragesLoader;
import com.artipie.asto.fs.FileStorageFactory;
import com.artipie.asto.s3.S3StorageFactory;

@Override
public Policy<?> getPolicy(final PolicyConfig config) {
    final PolicyConfig sub = config.config("storage");
    try {
        StoragesLoader storages = new StoragesLoader();
        return new YamlPolicy(new BlockingStorage(storages.newObject(
            sub.string("type"),
            new StoragesLoader.Config() {
                @Override
                public String config() {
                    return sub.toString();
                }
            }
        )));
    } catch (final IOException err) {
        throw new UncheckedIOException(err);
    }
}
```
In this patch, we create a `StoragesLoader` instance and use its `newObject` method to create a storage object based on the type specified in the configuration. We also define a nested `Config` class implementing the `com.artipie.asto.factory.StoragesLoader.Config` interface, which is used to provide the configuration for the storage.

Note that this patch assumes that the `FileStorageFactory` and `S3StorageFactory` classes are still available in the new library version, as they are used to create the `BlockingStorage` instance. If they have been removed, you may need to modify this patch accordingly.