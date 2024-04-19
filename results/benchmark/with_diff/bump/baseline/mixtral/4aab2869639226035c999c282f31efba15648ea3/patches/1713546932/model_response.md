Sure, here's a possible patch for the failing code:
```java
import com.artipie.asto.factory.StorageFactory;
import com.artipie.asto.factory.Config;
import java.util.Map;

// ...

Storage storage = StorageFactory.newStorage(
    new Config(Map.of("type", "local"))
);
```
Here, we're using the new `StorageFactory` class and its `newStorage` method to create a new `Storage` object. We pass in a `Config` object that specifies the type of storage we want to create. In this case, we're creating a local filesystem storage.

Note that the `Config` class takes a `Map` of configuration options. In this case, we're only specifying the `type` option, but you can add more options as needed.

Also note that the `StorageConfig` class has been removed in the new library version, so we can no longer use it to create a `Storage` object. Instead, we use the new `Config` class.

Finally, note that the `Storages` class has been removed in the new library version, so we can no longer use it to create a `Storage` object. Instead, we use the new `StorageFactory` class.