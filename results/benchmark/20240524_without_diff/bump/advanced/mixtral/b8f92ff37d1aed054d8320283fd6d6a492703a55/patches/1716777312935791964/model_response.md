Here is a possible patch for the failing method:
```java
import static org.apache.maven.surefire.api.util.DefaultScanResult.getWildcard;

static java.util.List<java.lang.String> getClassesLoc(java.io.File testSrcFolder) {
    org.apache.maven.plugin.surefire.util.DirectoryScanner directoryScanner = new org.apache.maven.plugin.surefire.util.DirectoryScanner(testSrcFolder, getWildcard());
    return directoryScanner.scan().getClasses();
}
```
The patch imports the `getWildcard()` method from `org.apache.maven.surefire.api.util.DefaultScanResult` and uses it in the `DirectoryScanner` constructor. This assumes that the `getWildcard()` method has not been removed or renamed in the version of the dependency that you are using. If it has, you may need to find an alternative way to obtain the wildcard pattern.