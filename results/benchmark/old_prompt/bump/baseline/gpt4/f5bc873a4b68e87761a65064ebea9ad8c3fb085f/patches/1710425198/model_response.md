The error message indicates that the symbol `DependencyResolutionRequiredException` cannot be found. This could be due to several reasons such as the library not being present in the classpath, the library not containing the class or the class being moved to a different package in a newer version of the library.

Assuming that the library is present and correctly added to the classpath, the class `DependencyResolutionRequiredException` might have been moved to a different package in a newer version of the library. 

The `DependencyResolutionRequiredException` class is a part of the Maven Artifact library. In some versions of this library, the class is present in the package `org.apache.maven.artifact.resolver` instead of `org.apache.maven.artifact`.

Therefore, you can try replacing the import statement with the following:

```java
import org.apache.maven.artifact.resolver.DependencyResolutionRequiredException;
```

This should resolve the issue if the class has been moved to this package in the version of the library you are using.