Here's a proposed patch to fix the error:
```java
import org.apache.maven.artifact.DependencyResolutionRequiredException;

// ...

try {
    // ...
} catch (DependencyResolutionRequiredException e) {
    // ...
}
```
Replace the failing code with the above patch. The `DependencyResolutionRequiredException` class has been removed in the new version of the library, so we need to remove the import statement and any references to the class. Instead, we can use a try-catch block to handle the exception.