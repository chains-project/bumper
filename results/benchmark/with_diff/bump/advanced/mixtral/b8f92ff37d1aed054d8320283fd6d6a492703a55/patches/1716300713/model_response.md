Here's the updated code that should resolve the error:

```java
static java.util.List<java.lang.String> getClassesLoc(java.io.File testSrcFolder) {
    org.apache.maven.plugin.surefire.util.DirectoryScanner directoryScanner = new org.apache.maven.plugin.surefire.util.DirectoryScanner(testSrcFolder, new org.apache.maven.surefire.api.testset.TestListResolver().getWildcard());
    return directoryScanner.scan().getClasses();
}
```

The issue was caused by the static method `getWildcard()` being removed from `TestListResolver` class. To fix the issue, we create a new instance of `TestListResolver` and call the `getWildcard()` method on it.