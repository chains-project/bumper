It seems like the import statement is failing because the symbol `Storages` cannot be found in the package `com.artipie.asto.factory`. This could be due to a number of reasons such as the class might have been removed, renamed or moved to a different package in the updated version of the library. 

Without specific information about the changes in the updated library, I can suggest a generic solution: 

Firstly, check the updated library documentation or source code to find if `Storages` class is still available. If it is, update the import statement with the correct package path.

If the `Storages` class is not available, you might need to replace it with an equivalent class or functionality provided in the updated library. 

As I don't have the specific information, I can't provide the exact code. However, here is a general structure of how the updated code might look like:

```java
import com.newpackage.NewEquivalentClass; 
```

Replace `com.newpackage.NewEquivalentClass` with the correct import statement based on your library update.