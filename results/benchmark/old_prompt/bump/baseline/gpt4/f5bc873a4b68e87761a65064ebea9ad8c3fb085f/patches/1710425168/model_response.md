It seems that the error is due to the unavailability of the class `DependencyResolutionRequiredException` in the imported package. This could be due to the class being deprecated or removed from the version of the library you are using.

If you are using Maven version 3.x, the `DependencyResolutionRequiredException` class is no longer available in the package `org.apache.maven.artifact`. Instead, it has been moved to `org.apache.maven.project`. 

Here is the corrected import statement:

```java
import org.apache.maven.project.DependencyResolutionRequiredException;
```