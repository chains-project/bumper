Here's the fixed failing method with the required changes:

```java
static java.util.List<java.lang.String> getClassesLoc(java.io.File testSrcFolder) {
    org.apache.maven.plugin.surefire.util.DirectoryScanner directoryScanner = new org.apache.maven.plugin.surefire.util.DirectoryScanner(testSrcFolder, new org.apache.maven.surefire.api.testset.TestListResolver().getWildcard());
    return directoryScanner.scan().getClasses();
}
```

The change is creating a new instance of `TestListResolver` and then calling the `getWildcard()` method on it.