The error message suggests that the symbol `Storages` cannot be found in `com.artipie.asto.factory`. This could be due to various reasons such as the class `Storages` does not exist, it is not public, or the package `com.artipie.asto.factory` does not exist.

Without the specific details about the external dependency, it's hard to provide a precise solution. However, a general approach to fix this kind of issue is to ensure that the correct package is imported. 

If the `Storages` class exists in a different package, you should update the import statement to reflect the correct package. For example, if `Storages` is in the `com.artipie.asto.storage` package, the import statement should be:

```java
import com.artipie.asto.storage.Storages;
```

If the `Storages` class has been renamed or removed in a newer version of the library, you should update your code to use the new class or an alternative class. For example, if the `Storages` class has been renamed to `StorageFactory`, the import statement should be:

```java
import com.artipie.asto.factory.StorageFactory;
```

Please replace the import statement with the correct one based on your specific situation.