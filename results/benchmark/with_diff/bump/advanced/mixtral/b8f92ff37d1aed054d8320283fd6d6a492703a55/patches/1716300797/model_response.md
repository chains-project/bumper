Here's the updated method that should fix the error:

```java
static java.util.List<java.lang.String> getClassesLoc(java.io.File testSrcFolder) {
    org.apache.maven.plugin.surefire.util.DirectoryScanner directoryScanner = new org.apache.maven.plugin.surefire.util.DirectoryScanner(testSrcFolder, getTestListResolver().getWildcard());
    return directoryScanner.scan().getClasses();
}

private static org.apache.maven.surefire.api.testset.TestListResolver getTestListResolver() {
    return new org.apache.maven.plugin.surefire.api.testset.TestListResolver();
}
```

The issue is that the `getWildcard()` method is no longer static in the `TestListResolver` class. To fix this, we create a new instance of `TestListResolver` and call `getWildcard()` on that instance.