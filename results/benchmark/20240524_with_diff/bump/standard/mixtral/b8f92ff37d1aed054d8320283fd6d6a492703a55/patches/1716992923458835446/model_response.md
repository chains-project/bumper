Here's the proposed patch for the failing client code:

```java
static java.util.List<java.lang.String> getClassesLoc(java.io.File testSrcFolder) {
    org.apache.maven.plugin.surefire.util.DirectoryScanner directoryScanner = new org.apache.maven.plugin.surefire.util.DirectoryScanner(testSrcFolder, new org.apache.maven.surefire.api.testset.TestListResolver().getWildcard());
    return directoryScanner.scan().getClasses();
}
```

The patch creates a new instance of `TestListResolver` and then calls the `getWildcard()` method on it. This should resolve the "cannot find symbol" error caused by the removed `getWildcard()` method in the updated library version.