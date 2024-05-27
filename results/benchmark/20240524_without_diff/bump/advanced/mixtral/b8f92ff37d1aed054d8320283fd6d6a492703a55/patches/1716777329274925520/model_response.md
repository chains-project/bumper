Here is a possible patch for the code:

```java
import static org.apache.maven.surefire.api.util.DefaultScanResult.getWildcard;

static java.util.List<java.lang.String> getClassesLoc(java.io.File testSrcFolder) {
    org.apache.maven.plugin.surefire.util.DirectoryScanner directoryScanner = new org.apache.maven.plugin.surefire.util.DirectoryScanner(testSrcFolder, getWildcard());
    return directoryScanner.scan().getClasses();
}
```

This patch imports the `getWildcard` method from `org.apache.maven.surefire.api.util.DefaultScanResult` and uses it in the `DirectoryScanner` constructor. This should fix the "cannot find symbol" error.