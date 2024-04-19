Sure, here's a possible patch for the failing code:
```java
import com.artipie.asto.factory.StorageFactory;
import com.artipie.asto.factory.Config;

import java.util.Map;

import static java.util.Collections.singletonMap;

// ...

Storage storage = StorageFactory.newStorage(new Config() {
    @Override
    public Map<String, Object> asMap() {
        return singletonMap("type", "in-memory");
    }
});
```
Explanation:

* I changed the import statement from `com.artipie.asto.factory.Storages` to `com.artipie.asto.factory.StorageFactory`.
* I created a new anonymous class that implements the `Config` interface, which is a parameter of the `newStorage` method.
* The `asMap` method of the `Config` interface returns a map that contains the configuration of the storage. In this case, I set the type of the storage to "in-memory".
* I created a new `Storage` object by calling the `newStorage` method of the `StorageFactory` class, passing the new `Config` object as a parameter.

Note that the `newStorage` method of the `StorageFactory` class is an abstract method that was added in the new version of the library. The `Storages` class and its methods were removed in the new version, so we cannot use them anymore.