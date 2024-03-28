It seems like the import statement is failing because the symbol 'Storages' is not found in the package 'com.artipie.asto.factory'. This could be due to an update in the external dependency where the 'Storages' class is removed or moved to a different package. 

To fix the issue, you need to find out the new location of the 'Storages' class and update the import statement accordingly. 

If the 'Storages' class is moved to a different package, the updated import statement could look something like this:

```java
import com.artipie.asto.newlocation.Storages;
```

If the 'Storages' class is removed, you have to replace it with the new class that provides the same functionality. Assuming the new class is 'StorageFactory' in the same package, the updated import statement would be:

```java
import com.artipie.asto.factory.StorageFactory;
```

Please replace 'newlocation' or 'StorageFactory' with the actual package or class name.