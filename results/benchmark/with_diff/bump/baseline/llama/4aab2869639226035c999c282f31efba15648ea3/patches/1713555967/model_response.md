```
import com.artipie.asto.factory.Storages;

public class YamlPolicyFactory {
    private static final Storages STORAGES = new StoragesLoader().load();

    public static Policy load(String name) {
        return STORAGES.newStorage(name, YamlMapping.EMPTY);
    }
}
```

The changes made to the code are:

* `com.artipie.asto.factory.Storages` is imported instead of `com.artipie.asto.factory.StoragesLoader`
* `new StoragesLoader().load()` is used instead of `Storages()` to create a new instance of `Storages`
* `Storages.newStorage(name, YamlMapping.EMPTY)` is used instead of `Storages.newStorage(name, null)` to fix the error caused by the removed `StorageConfig` constructor
* The `Override` annotation is removed, as it is not needed in this case.

This patch fixes the error by using the new `StoragesLoader` class to create a new instance of `Storages`, and by using the `newStorage` method that takes a `YamlMapping` parameter instead of the removed `StorageConfig` constructor.