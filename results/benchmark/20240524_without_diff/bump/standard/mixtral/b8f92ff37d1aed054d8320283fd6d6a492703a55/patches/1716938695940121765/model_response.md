Here's a potential patch for the failing client code:
```java
import static org.apache.maven.surefire.api.testset.TestSetFailedException.getWildcard;

static java.util.List<java.lang.String> getClassesLoc(java.io.File testSrcFolder) {
    org.apache.maven.plugin.surefire.util.DirectoryScanner directoryScanner = new org.apache.maven.plugin.surefire.util.DirectoryScanner(testSrcFolder, getWildcard());
    return directoryScanner.scan().getClasses();
}
```
The patch imports the `getWildcard` method as a static import and uses it in the constructor of `DirectoryScanner`. This assumes that the `getWildcard` method is still available in the version of the Surefire API you are using, but has been moved or renamed in the `TestListResolver` class.