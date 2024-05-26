Here's the patched version of the `getClassesLoc` method that uses an added library method `DirectoryScanner.getWildcard()` instead of the missing method `TestListResolver.getWildcard()`:
```java
import org.apache.maven.plugin.surefire.util.DirectoryScanner;

static java.util.List<java.lang.String> getClassesLoc(java.io.File testSrcFolder) {
    org.apache.maven.plugin.surefire.util.DirectoryScanner directoryScanner = new org.apache.maven.plugin.surefire.util.DirectoryScanner(testSrcFolder, directoryScanner.getWildcard());
    return directoryScanner.scan().getClasses();
}
```
Note that the above code may not work as expected since I don't have the full context of the codebase. It's possible that `DirectoryScanner.getWildcard()` does not return the same value as `TestListResolver.getWildcard()`. You may need to modify the code further based on the actual behavior of these methods.