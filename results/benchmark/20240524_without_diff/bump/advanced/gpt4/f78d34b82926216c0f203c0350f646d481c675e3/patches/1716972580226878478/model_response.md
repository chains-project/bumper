It seems like the package `develop.p2p.lib` is no longer available or has been moved. You might have updated a dependency which caused this package to be unavailable. You need to find the new package that contains `WaveCreator` class and import that. If you cannot find the new package, you might need to downgrade the dependency to the version which contains `develop.p2p.lib`. 

Since I don't have information about the new package or the dependency, I cannot provide a specific code solution. But the import statement should look something like this:

```java
import new.package.path.WaveCreator;
```

Replace `new.package.path` with the correct package path that contains `WaveCreator` class.