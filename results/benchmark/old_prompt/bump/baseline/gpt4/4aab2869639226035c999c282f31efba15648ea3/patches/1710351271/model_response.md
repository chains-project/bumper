The error message indicates that the symbol `Storages` cannot be found. This could be due to a number of reasons such as the class not existing, the package not existing, or the class not being accessible due to its access level. 

However, as a specialist in breaking dependency updates, I suspect that the class `Storages` might have been moved to a different package or renamed in a newer version of the library `com.artipie.asto`. 

Unfortunately, without knowing the exact changes in the library, I cannot provide a precise fix. However, I can suggest general steps to resolve this issue:

1. Check the latest documentation of the library `com.artipie.asto` to find the new location or name of the class `Storages`. 

2. Update the import statement with the new location or name.

Let's assume that the class `Storages` has been renamed to `StorageFactory` and is still in the same package. Then the fixed client code would be:

```java
  import com.artipie.asto.factory.StorageFactory;
```

Please replace `StorageFactory` with the actual new name or location of the class `Storages` based on the library's latest documentation.