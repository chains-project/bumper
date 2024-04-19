Here is a potential patch for the given code:
```java
static java.util.List<java.lang.String> getClassesLoc(java.io.File testSrcFolder) {
    org.apache.maven.plugin.surefire.util.DirectoryScanner directoryScanner = new org.apache.maven.plugin.surefire.util.DirectoryScanner(testSrcFolder, new org.apache.maven.surefire.api.testset.TestListResolver().getWildcard());
    return directoryScanner.scan().getClasses();
}
```
The issue seems to be that the `getWildcard()` method is not being called on an instance of `TestListResolver`. The patch creates a new instance of `TestListResolver` and then calls `getWildcard()` on that instance.