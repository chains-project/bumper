Here is a potential patch for the failing client code:
```java
import org.apache.maven.surefire.api.testset.TestFileSet;

static java.util.List<java.lang.String> getClassesLoc(java.io.File testSrcFolder) {
    org.apache.maven.plugin.surefire.util.DirectoryScanner directoryScanner = new org.apache.maven.plugin.surefire.util.DirectoryScanner(testSrcFolder, new TestFileSet().getInclude());
    return directoryScanner.scan().getClasses();
}
```
In this patch, I have replaced the call to `TestListResolver.getWildcard()` with `new TestFileSet().getInclude()`. This is because the `getWildcard()` method is no longer available in the version of the `surefire-api` library that you are using. Instead, we can use the `getInclude()` method of the `TestFileSet` class to achieve the same functionality.

Note that this patch assumes that you are using a version of the `surefire-api` library that includes the `TestFileSet` class. If this is not the case, you may need to update your library dependencies or use a different approach to achieve the desired functionality.