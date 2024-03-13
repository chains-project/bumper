It seems like the error message suggests that the symbol `Storages` cannot be found in the package `com.artipie.asto.factory`. This could be due to several reasons, such as the class `Storages` does not exist in the package, the package does not exist, or the package is not correctly imported.

Unfortunately, without more information about the package structure and the class `Storages`, it's hard to provide a specific fix.

However, a common fix for such problems is to ensure that the package and the class are correctly defined and exist in your project. If the class `Storages` is in a different package, you should correct the import statement to reflect the correct package.

For example, if the `Storages` class is in the package `com.artipie.asto`, the corrected import statement would be:

```java
import com.artipie.asto.Storages;
```

If the `Storages` class does not exist, you should remove the import statement, and replace the usage of `Storages` with the correct class or classes.

Without more context, it's hard to provide a more specific fix. You should check your project structure and ensure that all packages and classes are correctly defined and imported.