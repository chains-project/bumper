The error message indicates that the symbol `Storages` cannot be found in the package `com.artipie.asto.factory`. This might be due to a couple of reasons such as the `Storages` class does not exist in the specified package, the package does not exist, or the dependency containing the package is not correctly configured or included in your project.

Without knowing the exact structure of the `com.artipie.asto.factory` package or the available classes in the dependency, it's difficult to provide a specific solution. However, a common solution is to correct the import statement.

If `Storages` class has been moved to a different package, you should update the import statement to reflect the new package. If `Storages` class has been renamed or replaced, you should import the new class.

For example, if `Storages` class has been moved to `com.artipie.asto.storage` package, the corrected import statement should be:

```java
import com.artipie.asto.storage.Storages;
```

If `Storages` class has been renamed to `StorageFactory`, the corrected import statement should be:

```java
import com.artipie.asto.factory.StorageFactory;
```

Please replace the package and class names in the examples with the actual package and class names in your dependency.