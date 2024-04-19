Sure, here's a possible patch for the failing code:
```java
import com.artipie.asto.factory.StorageFactory;
import com.artipie.asto.factory.Config;
import java.util.Map;

// ...

Storage storage = StorageFactory.newStorage(
    new Config(Map.of("type", "in-memory"))
);
```
In this patch, we have imported the new `StorageFactory` class and `Config` interface from the updated library version. We then create a new `Config` object with a map containing the required configuration for a new `Storage` object. Finally, we create a new `Storage` object using the `newStorage` method of the `StorageFactory` class, passing in the `Config` object we created earlier.

Note that the `Storages` class has been removed in the updated library version, so we can no longer use it to create a new `Storage` object. Instead, we use the new `StorageFactory` class to create the `Storage` object directly.