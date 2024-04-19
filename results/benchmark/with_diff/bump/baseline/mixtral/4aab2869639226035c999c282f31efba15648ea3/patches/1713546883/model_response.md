Sure, here's a possible patch for the failing code:
```java
import com.artipie.asto.factory.StorageFactory;
import com.artipie.asto.factory.Config;
import java.util.Map;

// ...

Storage storage = StorageFactory.newStorage(new Config() {
        @Override
        public String type() {
            return "your-storage-type";
        }

        @Override
        public Map<String, Object> params() {
            return Map.of(
                "your-param-key", "your-param-value"
            );
        }
    });
```
Explanation:

* We import the new `StorageFactory` class, which has replaced the old `Storages` class.
* We create a new anonymous class extending `Config` to provide the necessary configuration for the storage.
* We call the new `newStorage` method on `StorageFactory`, passing in an instance of our `Config` subclass.

Note that you'll need to replace `"your-storage-type"` and `"your-param-value"` with the appropriate values for your use case. Also, if your storage configuration requires more parameters, you can add them to the `params()` method.