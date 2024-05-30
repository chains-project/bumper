Here's the patched version of the `getClassesLoc` method that should resolve the error:

```java
static java.util.List<java.lang.String> getClassesLoc(java.io.File testSrcFolder) {
    org.apache.maven.plugin.surefire.util.DirectoryScanner directoryScanner = new org.apache.maven.plugin.surefire.util.DirectoryScanner(testSrcFolder, () -> org.apache.maven.surefire.api.testset.TestListResolver.getWildcard());
    return directoryScanner.scan().getClasses();
}
```

The issue is caused by the deprecated `getWildcard()` method, which has been replaced by a lambda expression that returns the same value.