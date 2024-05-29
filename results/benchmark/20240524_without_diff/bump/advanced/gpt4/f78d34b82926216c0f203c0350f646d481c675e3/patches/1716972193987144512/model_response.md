It seems like the package `develop.p2p.lib` is not available in your classpath. You might be missing a dependency or the package might have been renamed or removed. 

Unfortunately, without more context, it's impossible to provide a specific code fix. However, you should check your project's dependencies and ensure that the required library is correctly included. If the library has been updated, you may need to adjust your imports to match the new package structure.

If the WaveCreator class has been moved to a different package, you should update the import statement accordingly. For example, if the WaveCreator class is now in the `com.example.lib` package, you would change the import statement to:

```java
import com.example.lib.WaveCreator;
```

Please replace `com.example.lib` with the actual package name where the WaveCreator class is located.